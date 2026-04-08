#!/usr/bin/env python3
"""
Extract 3D assets from Warcraft III MPQ files.
Extracts Units, Textures, Abilities, ReplaceableTextures directories.
Uses StormLib (via ctypes) for proper decompression.
Requires: brew install stormlib
"""
import ctypes
import os
import sys

# StormLib 动态库路径
STORMLIB_PATH = "/opt/homebrew/lib/libstorm.dylib"

# MPQ文件路径
MPQ_DIR = "/opt/sourcecode/warcraft_resource/war3/Warcraft III Frozen Throne"
OUTPUT_DIR = "/opt/sourcecode/warcraft_resource/war3/extracted_models"

# 需要提取的MPQ文件
MPQ_FILES = [
    "war3.mpq",      # 混乱之治核心资源（基础英雄、怪物）
    "War3x.mpq",     # 冰封王座扩展资源（新增英雄、怪物）
]

# 需要提取的目录前缀
EXTRACT_PREFIXES = [
    "Units\\",
    "units\\",
    "Textures\\",
    "textures\\",
    "Abilities\\",
    "abilities\\",
    "ReplaceableTextures\\",
    "replaceabletextures\\",
    "SharedModels\\",
    "sharedmodels\\",
    "Environment\\",
    "environment\\",
    "Doodads\\",
    "doodads\\",
]

# 需要提取的文件扩展名
EXTRACT_EXTENSIONS = {
    ".mdx",   # 3D模型文件
    ".mdl",   # 3D模型文本格式
    ".blp",   # 暴雪贴图格式
    ".tga",   # TGA贴图
    ".dds",   # DDS贴图
}

# StormLib 常量
STREAM_FLAG_READ_ONLY = 0x00000100
SFILE_OPEN_FROM_MPQ = 0x00000000
MAX_PATH = 1024


class SFILE_FIND_DATA(ctypes.Structure):
    """StormLib 文件查找数据结构"""
    _fields_ = [
        ('cFileName', ctypes.c_char * MAX_PATH),
        ('szPlainName', ctypes.c_char_p),
        ('dwHashIndex', ctypes.c_uint32),
        ('dwBlockIndex', ctypes.c_uint32),
        ('dwFileSize', ctypes.c_uint32),
        ('dwFileFlags', ctypes.c_uint32),
        ('dwCompSize', ctypes.c_uint32),
        ('dwFileTimeLo', ctypes.c_uint32),
        ('dwFileTimeHi', ctypes.c_uint32),
        ('lcLocale', ctypes.c_uint32),
    ]


def load_stormlib():
    """加载 StormLib 动态库并设置函数签名"""
    lib = ctypes.CDLL(STORMLIB_PATH)

    # SFileOpenArchive
    lib.SFileOpenArchive.restype = ctypes.c_bool
    lib.SFileOpenArchive.argtypes = [
        ctypes.c_char_p, ctypes.c_uint32, ctypes.c_uint32,
        ctypes.POINTER(ctypes.c_void_p)
    ]

    # SFileCloseArchive
    lib.SFileCloseArchive.restype = ctypes.c_bool
    lib.SFileCloseArchive.argtypes = [ctypes.c_void_p]

    # SFileFindFirstFile
    lib.SFileFindFirstFile.restype = ctypes.c_void_p
    lib.SFileFindFirstFile.argtypes = [
        ctypes.c_void_p, ctypes.c_char_p,
        ctypes.POINTER(SFILE_FIND_DATA), ctypes.c_char_p
    ]

    # SFileFindNextFile
    lib.SFileFindNextFile.restype = ctypes.c_bool
    lib.SFileFindNextFile.argtypes = [
        ctypes.c_void_p, ctypes.POINTER(SFILE_FIND_DATA)
    ]

    # SFileFindClose
    lib.SFileFindClose.restype = ctypes.c_bool
    lib.SFileFindClose.argtypes = [ctypes.c_void_p]

    # SFileOpenFileEx
    lib.SFileOpenFileEx.restype = ctypes.c_bool
    lib.SFileOpenFileEx.argtypes = [
        ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint32,
        ctypes.POINTER(ctypes.c_void_p)
    ]

    # SFileGetFileSize
    lib.SFileGetFileSize.restype = ctypes.c_uint32
    lib.SFileGetFileSize.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)]

    # SFileReadFile
    lib.SFileReadFile.restype = ctypes.c_bool
    lib.SFileReadFile.argtypes = [
        ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32,
        ctypes.POINTER(ctypes.c_uint32), ctypes.c_void_p
    ]

    # SFileCloseFile
    lib.SFileCloseFile.restype = ctypes.c_bool
    lib.SFileCloseFile.argtypes = [ctypes.c_void_p]

    return lib


def should_extract(filename):
    """判断文件是否需要提取"""
    if not filename:
        return False
    # 检查是否在目标目录下
    for prefix in EXTRACT_PREFIXES:
        if filename.startswith(prefix):
            # 检查扩展名
            _, ext = os.path.splitext(filename.lower())
            if ext in EXTRACT_EXTENSIONS:
                return True
    return False


def read_file_from_mpq(lib, hMpq, filename):
    """从 MPQ 中读取单个文件的完整内容"""
    hFile = ctypes.c_void_p()
    if not lib.SFileOpenFileEx(hMpq, filename.encode('utf-8'),
                               SFILE_OPEN_FROM_MPQ, ctypes.byref(hFile)):
        return None

    try:
        # 获取文件大小
        high_size = ctypes.c_uint32(0)
        file_size = lib.SFileGetFileSize(hFile, ctypes.byref(high_size))
        if file_size == 0xFFFFFFFF:
            return None

        # 读取文件内容
        buf = ctypes.create_string_buffer(file_size)
        bytes_read = ctypes.c_uint32(0)
        if not lib.SFileReadFile(hFile, buf, file_size,
                                 ctypes.byref(bytes_read), None):
            # 即使读取"失败"，也可能读到了部分数据
            if bytes_read.value == 0:
                return None

        return buf.raw[:bytes_read.value]
    finally:
        lib.SFileCloseFile(hFile)


def extract_from_mpq(lib, mpq_path, output_base):
    """从单个MPQ文件中提取模型资源"""
    mpq_name = os.path.basename(mpq_path)
    print(f"\n{'='*60}")
    print(f"正在处理: {mpq_name}")
    print(f"{'='*60}")

    hMpq = ctypes.c_void_p()
    if not lib.SFileOpenArchive(mpq_path.encode('utf-8'), 0,
                                STREAM_FLAG_READ_ONLY, ctypes.byref(hMpq)):
        print(f"  ❌ 无法打开 {mpq_name}")
        return 0

    try:
        # 枚举所有文件
        find_data = SFILE_FIND_DATA()
        hFind = lib.SFileFindFirstFile(hMpq, b'*',
                                       ctypes.byref(find_data), None)
        if not hFind:
            print(f"  ⚠️  {mpq_name} 中没有文件列表")
            return 0

        # 收集需要提取的文件
        all_files = []
        to_extract = []
        while True:
            name = find_data.cFileName.decode('utf-8', errors='ignore') \
                                      .rstrip('\x00')
            all_files.append(name)
            if should_extract(name):
                to_extract.append((name, find_data.dwFileSize))
            if not lib.SFileFindNextFile(hFind, ctypes.byref(find_data)):
                break
        lib.SFileFindClose(hFind)

        print(f"  📦 总文件数: {len(all_files)}")
        print(f"  🎯 匹配的模型/贴图文件: {len(to_extract)}")

        if not to_extract:
            print("  ⚠️  没有找到匹配的文件")
            return 0

        # 按种族/类型统计
        categories = {}
        for name, _ in to_extract:
            parts = name.replace("\\", "/").split("/")
            if len(parts) >= 3:
                category = parts[1]
            else:
                category = "Other"
            categories[category] = categories.get(category, 0) + 1

        print(f"\n  📊 按种族/类型分布:")
        for cat, count in sorted(categories.items()):
            print(f"     {cat}: {count} 个文件")

        # 开始提取
        extracted = 0
        failed = 0
        failed_list = []
        for name, expected_size in to_extract:
            try:
                data = read_file_from_mpq(lib, hMpq, name)
                if data and len(data) > 0:
                    # 将Windows路径转为本地路径
                    rel_path = name.replace("\\", "/")
                    out_path = os.path.join(
                        output_base,
                        mpq_name.replace(".mpq", ""),
                        rel_path
                    )
                    os.makedirs(os.path.dirname(out_path), exist_ok=True)
                    with open(out_path, 'wb') as f:
                        f.write(data)
                    extracted += 1
                else:
                    failed += 1
                    failed_list.append((name, "读取返回空数据"))
            except Exception as e:
                failed += 1
                failed_list.append((name, str(e)))

        print(f"\n  ✅ 成功提取: {extracted} 个文件")
        if failed:
            print(f"  ❌ 提取失败: {failed} 个文件")
            for name, err in failed_list[:10]:
                print(f"     {name}: {err}")
            if len(failed_list) > 10:
                print(f"     ... 还有 {len(failed_list) - 10} 个")

        return extracted
    finally:
        lib.SFileCloseArchive(hMpq)


def main():
    print("🏰 魔兽争霸3 3D资源提取工具 (StormLib)")
    print(f"📂 输出目录: {OUTPUT_DIR}")

    # 加载 StormLib
    try:
        lib = load_stormlib()
        print(f"✅ StormLib 加载成功: {STORMLIB_PATH}")
    except OSError as e:
        print(f"❌ 无法加载 StormLib: {e}")
        print("   请先安装: brew install stormlib")
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    total_extracted = 0
    for mpq_file in MPQ_FILES:
        mpq_path = os.path.join(MPQ_DIR, mpq_file)
        if not os.path.exists(mpq_path):
            print(f"\n⚠️  文件不存在: {mpq_path}")
            continue
        total_extracted += extract_from_mpq(lib, mpq_path, OUTPUT_DIR)

    print(f"\n{'='*60}")
    print(f"🎉 提取完成！共提取 {total_extracted} 个文件")
    print(f"📂 输出目录: {OUTPUT_DIR}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
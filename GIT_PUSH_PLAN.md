
# Warcraft Resource 项目 Git 提交方案

## 项目分析

项目总大小 **4.5GB**，文件分布如下：

| 目录 | 大小 | 说明 |
|------|------|------|
| `war3/Warcraft III Frozen Throne/` | 1.2GB | 游戏原始文件（含 1.2GB 的 rar、430MB+ 的 mpq 等） |
| `war3/extracted_sounds/` | 1.1GB | 提取的音频文件（mp3/wav） |
| `war3/converted_models/` | 828MB | 转换后的模型文件（glb） |
| `war3/extracted_models/` | 212MB | 提取的模型文件（mdx） |
| `Prompts/` | 6.9MB | Prompt 文件（很小） |

**核心问题**：GitHub 单文件限制 100MB，仓库建议不超过 1GB。有 12 个文件超过 50MB，4 个文件超过 100MB。

## 方案：Git LFS + .gitignore 组合策略

### 第一步：创建 `.gitignore` 排除不必要的文件

```bash
cat > .gitignore << 'EOF'
# IDE 文件
.idea/
.DS_Store
*.DS_Store

# 游戏原始安装文件（可从其他渠道获取，无需纳入版本管理）
war3/Warcraft III Frozen Throne/
EOF
```

### 第二步：安装并配置 Git LFS

```bash
brew install git-lfs
git lfs install
```

### 第三步：用 Git LFS 追踪大文件类型

```bash
git lfs track "*.mp3"
git lfs track "*.wav"
git lfs track "*.mpq"
git lfs track "*.mdx"
git lfs track "*.MDX"
git lfs track "*.glb"
git lfs track "*.blp"
git lfs track "*.w3x"
git lfs track "*.w3m"
git lfs track "*.rar"
git lfs track "*.tga"
git lfs track "*.m3d"
git lfs track "*.png"
```

### 第四步：提交并推送

```bash
git add .gitignore .gitattributes
git commit -m "chore: add .gitignore and Git LFS tracking"

git add .
git commit -m "feat: add warcraft resource files"

git push origin main
```

## ⚠️ 注意事项

| 项目 | 说明 |
|------|------|
| **GitHub LFS 免费额度** | 1GB 存储 + 1GB/月 带宽。资源约 3.3GB（排除游戏安装文件后），需要购买额外的 Data Pack（$5/月，50GB 存储 + 50GB 带宽） |
| **替代托管平台** | 如果不想付费，可以考虑 **Gitee**（单文件限制 100MB，仓库限制 5GB）或自建 **GitLab** |
| **更激进的 .gitignore** | 如果 `extracted_sounds/` 和 `converted_models/` 可以通过脚本重新生成，建议也加入 `.gitignore`，仓库只需管理约 220MB |

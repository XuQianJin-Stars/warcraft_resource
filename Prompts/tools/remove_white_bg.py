"""
去除人物立绘外部白色背景的脚本
使用 flood fill 从图片四个边缘开始，将连通的白色/近白色区域变为透明
"""

import sys
import os
import argparse
from PIL import Image
import numpy as np
from collections import deque


def remove_white_background(input_path, output_path, threshold=30):
    """
    从边缘开始 flood fill 去除白色背景

    Args:
        input_path: 输入图片路径
        output_path: 输出图片路径
        threshold: 白色判定阈值，像素RGB各通道与255的差值小于此值视为白色
    """
    img = Image.open(input_path).convert("RGBA")
    data = np.array(img)
    h, w = data.shape[:2]

    # 判断像素是否为白色/近白色
    def is_white(r, g, b):
        return (255 - r) < threshold and (255 - g) < threshold and (255 - b) < threshold

    # 创建访问标记
    visited = np.zeros((h, w), dtype=bool)
    # 创建需要变透明的标记
    to_remove = np.zeros((h, w), dtype=bool)

    # BFS flood fill 从边缘开始
    queue = deque()

    # 将四条边上的白色像素加入队列
    for x in range(w):
        for y in [0, h - 1]:
            r, g, b = data[y, x, 0], data[y, x, 1], data[y, x, 2]
            if is_white(r, g, b) and not visited[y, x]:
                visited[y, x] = True
                to_remove[y, x] = True
                queue.append((y, x))

    for y in range(h):
        for x in [0, w - 1]:
            r, g, b = data[y, x, 0], data[y, x, 1], data[y, x, 2]
            if is_white(r, g, b) and not visited[y, x]:
                visited[y, x] = True
                to_remove[y, x] = True
                queue.append((y, x))

    print(f"边缘白色种子点数量: {len(queue)}")
    print("开始 flood fill...")

    # BFS 扩展
    count = 0
    while queue:
        cy, cx = queue.popleft()
        count += 1
        if count % 500000 == 0:
            print(f"  已处理 {count} 个像素...")

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < h and 0 <= nx < w and not visited[ny, nx]:
                r, g, b = data[ny, nx, 0], data[ny, nx, 1], data[ny, nx, 2]
                if is_white(r, g, b):
                    visited[ny, nx] = True
                    to_remove[ny, nx] = True
                    queue.append((ny, nx))

    print(f"总共标记 {to_remove.sum()} 个白色像素为透明")

    # 将标记的像素设为透明
    data[to_remove, 3] = 0

    # 保存结果
    result = Image.fromarray(data)
    result.save(output_path)
    print(f"已保存到: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="去除图片外部白色背景")
    parser.add_argument("input", help="输入图片路径")
    parser.add_argument("output", help="输出图片路径")
    parser.add_argument("--threshold", type=int, default=30,
                        help="白色判定阈值(默认30)，值越大容忍的灰度范围越大")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"错误: 输入文件不存在: {args.input}")
        sys.exit(1)

    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    remove_white_background(args.input, args.output, args.threshold)

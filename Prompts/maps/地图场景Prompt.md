# 地图场景美术 Prompt

> **用途**：战斗场景的地图背景和地图元素
> **工具**：Midjourney 生成背景 + GPT-4o 生成地图元素
> **风格**：2D卡通化，俯视/斜45度视角
> **输出格式**：PNG，背景 1920×1080px，元素各异

---

## 地图背景

### 1. 洛丹伦废墟（Lordaeron Ruins）⭐ P0
**文件名**：`map_lordaeron_bg.png`

**Midjourney Prompt：**
```
2D cartoon game map background, top-down isometric view,
Lordaeron Ruins from Warcraft 3, abandoned castle ruins,
gray stone walls crumbling, broken banners and flags,
withered dead trees, cracked stone paths,
dark moody atmosphere with gray and purple tones,
game level background, detailed tileable design,
1920x1080 resolution, cartoon style with thick outlines
--ar 16:9 --style raw --v 6
```

### 2. 灰谷森林（Ashenvale Forest）⭐ P0
**文件名**：`map_ashenvale_bg.png`

**Midjourney Prompt：**
```
2D cartoon game map background, top-down isometric view,
Ashenvale Forest from Warcraft 3, dense magical forest,
giant ancient trees with glowing leaves, mushrooms,
flowing streams and small waterfalls, winding forest paths,
lush green and purple moonlit atmosphere,
night elf forest aesthetic, fireflies and magical particles,
game level background, 1920x1080, cartoon style thick outlines
--ar 16:9 --style raw --v 6
```

### 3. 冰封王座（Frozen Throne）⭐ P1
**文件名**：`map_frozen_throne_bg.png`

**Midjourney Prompt：**
```
2D cartoon game map background, top-down isometric view,
Frozen Throne from Warcraft 3, ice castle fortress,
massive ice pillars and frozen walls, snow covered paths,
snowflakes falling, dark blue and ice white color scheme,
ominous frozen throne in the distance, icy bridges,
cold harsh atmosphere, game level background,
1920x1080, cartoon style thick outlines
--ar 16:9 --style raw --v 6
```

---

## 地图元素

### 路径地砖 ⭐ P0

**洛丹伦路径（GPT-4o）：**
```
请生成一组2D游戏地图路径地砖，俯视视角。
风格：卡通化，灰色破碎石板路，有裂缝和青苔。
包含：直线段、转弯段、交叉段，每块64×64像素。
适合魔兽争霸废墟城堡主题，PNG透明背景。
```

**灰谷路径（GPT-4o）：**
```
请生成一组2D游戏地图路径地砖，俯视视角。
风格：卡通化，泥土小路，两侧有草丛和小花。
包含：直线段、转弯段、交叉段，每块64×64像素。
适合魔幻森林主题，PNG透明背景。
```

**冰封路径（GPT-4o）：**
```
请生成一组2D游戏地图路径地砖，俯视视角。
风格：卡通化，冰雪覆盖的石板路，有冰晶和雪花。
包含：直线段、转弯段、交叉段，每块64×64像素。
适合冰雪城堡主题，PNG透明背景。
```

### 放置点标记 ⭐ P0
**文件名**：`map_placement_point.png`

```
请生成一个2D游戏英雄放置点标记，俯视视角。
风格：卡通化，绿色发光的圆形平台，
有魔法纹路和微弱的上升光粒子效果。
尺寸：64×64像素，PNG透明背景。
提供两种状态：可放置（绿色）和不可放置（红色）。
```

### 起点标记 ⭐ P0

**洛丹伦起点：**
```
请生成一个2D游戏怪物出生点，俯视视角。
风格：卡通化，暗紫色传送门/暗黑漩涡，
散发紫色能量光芒，有骷髅装饰的门框。
尺寸：96×96像素，PNG透明背景。
适合不死族/废墟主题。
```

**灰谷起点：**
```
请生成一个2D游戏怪物出生点，俯视视角。
风格：卡通化，黑暗的树洞/洞穴入口，
周围有发光的蘑菇和藤蔓，散发绿色迷雾。
尺寸：96×96像素，PNG透明背景。
适合魔幻森林主题。
```

**冰封起点：**
```
请生成一个2D游戏怪物出生点，俯视视角。
风格：卡通化，冰蓝色传送门/冰裂缝，
散发冰蓝色寒气，周围有冰柱。
尺寸：96×96像素，PNG透明背景。
适合冰雪主题。
```

### 终点标记 ⭐ P0

**洛丹伦终点：**
```
请生成一个2D游戏防守目标建筑，俯视视角。
风格：卡通化，人类城堡/要塞大门，
金色和蓝色旗帜，石墙城门，需要保护的感觉。
尺寸：128×128像素，PNG透明背景。
```

**灰谷终点：**
```
请生成一个2D游戏防守目标建筑，俯视视角。
风格：卡通化，世界之树/生命之树，
巨大的发光古树，绿色光芒，自然能量。
尺寸：128×128像素，PNG透明背景。
```

**冰封终点：**
```
请生成一个2D游戏防守目标建筑，俯视视角。
风格：卡通化，冰封王座/冰之要塞，
冰蓝色城堡，冰柱装饰，寒冰光芒。
尺寸：128×128像素，PNG透明背景。
```

### 装饰物 ⭐ P1

**通用装饰物（GPT-4o）：**
```
请生成一组2D游戏地图装饰物，俯视视角，卡通风格。
每个装饰物单独输出，PNG透明背景，约32×32~64×64像素。
包含以下装饰物：
1. 枯树（灰色，适合废墟）
2. 绿树（茂密，适合森林）
3. 冰树（冰晶覆盖，适合冰雪）
4. 石头（大中小三种）
5. 草丛（绿色/枯黄两种）
6. 路灯/火把（发光效果）
7. 蘑菇（发光魔幻蘑菇）
8. 骨堆（不死族装饰）
9. 雪堆（冰雪装饰）
10. 破碎旗帜（废墟装饰）
```

### 空中路线标记 ⭐ P1
**文件名**：`map_air_route_marker.png`

```
请生成一个2D游戏飞行路线指示标记。
风格：卡通化，半透明的白色虚线箭头，
带有微弱的发光效果，指示飞行怪物的路线。
尺寸：32×32像素，PNG透明背景。
```

---

## 地图缩略图 ⭐ P1
**文件名**：`map_lordaeron_thumb.png` / `map_ashenvale_thumb.png` / `map_frozen_throne_thumb.png`

```
请将以下地图背景缩小为320×180像素的缩略图，
保持清晰度，添加地图名称文字叠加，
用于主界面关卡选择展示。
```
（注：缩略图可由完整地图背景程序缩放生成）

---

## 📋 生成注意事项

1. 地图背景建议使用 **Midjourney** 生成，大尺寸效果更好
2. 地图元素建议使用 **GPT-4o** 生成，小尺寸精确控制
3. 路径地砖需要能 **无缝拼接**
4. 每张地图的装饰物风格要与地图背景 **统一**
5. 起点/终点标记要足够醒目，玩家一眼能识别
6. 缩略图可以由程序从完整背景缩放生成，不一定需要单独制作

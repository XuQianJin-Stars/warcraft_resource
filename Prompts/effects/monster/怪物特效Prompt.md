# 怪物特殊效果图标 Prompt

> **用途**：怪物特殊能力的视觉标识
> **工具**：GPT-4o 生成
> **风格**：卡通化，小尺寸图标/特效
> **输出格式**：PNG（透明背景）

---

## 特殊效果图标（32×32px）

### 1. 治疗光环 ⭐ P1
**文件名**：`fx_monster_heal_aura.png`
```
请生成一个32×32像素的怪物治疗光环效果图标。
风格：卡通化，绿色发光的圆形光圈，
带有绿色十字/心形标记，柔和的绿色光芒。
PNG透明背景。
```

### 2. 加速光环 ⭐ P1
**文件名**：`fx_monster_speed_aura.png`
```
请生成一个32×32像素的怪物加速光环效果图标。
风格：卡通化，黄色发光的圆形光圈，
带有黄色箭头/闪电标记，动感的黄色光芒。
PNG透明背景。
```

### 3. 分裂效果 ⭐ P1
**文件名**：`fx_monster_split_01.png` ~ `fx_monster_split_04.png`
```
sprite sheet, 4 frames, cartoon split/divide effect,
creature splitting into two, poof smoke cloud,
two smaller copies appearing, game VFX,
transparent background, vibrant colors
--ar 4:1 --style raw --v 6
```

### 4. 隐身效果 ⭐ P1
**文件名**：`fx_monster_stealth.png`
```
请生成一个怪物隐身效果的覆盖层，64×64像素。
风格：半透明的虚影效果，蓝色/紫色色调，
像水波纹一样的扭曲效果，用于叠加在怪物上方。
PNG透明背景。
```

### 5. 护盾效果 ⭐ P1
**文件名**：`fx_monster_shield.png`
```
请生成一个怪物护盾效果图，64×64像素。
风格：卡通化，蓝色半透明的球形护盾，
带有六边形蜂窝纹理，微弱的蓝色光芒。
用于包裹在怪物周围。PNG透明背景。
```

### 6. 复活效果 ⭐ P2
**文件名**：`fx_monster_revive_01.png` ~ `fx_monster_revive_04.png`
```
sprite sheet, 4 frames, cartoon revive/resurrect effect,
golden light rising from ground, sparkles gathering,
creature reforming from light, resurrection magic,
game VFX, transparent background, vibrant golden colors
--ar 4:1 --style raw --v 6
```

---

## 📋 生成注意事项

1. 光环效果需要能 **循环播放** 或作为静态覆盖层使用
2. 隐身效果是覆盖层，需要 **半透明**
3. 护盾效果需要能包裹不同大小的怪物（程序缩放）

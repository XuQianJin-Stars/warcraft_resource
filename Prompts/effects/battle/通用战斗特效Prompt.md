# 通用战斗特效 Prompt

> **用途**：战斗中的通用视觉效果（攻击命中、控制效果、死亡等）
> **工具**：GPT-4o / Midjourney 生成
> **风格**：卡通风格特效，明亮鲜艳
> **输出格式**：PNG（透明背景），每帧 32×32px ~ 64×64px

---

## 攻击命中特效

### 1. 物理攻击命中 ⭐ P0
**文件名**：`fx_hit_physical_01.png` ~ `fx_hit_physical_02.png`

```
sprite sheet, 2 frames, cartoon slash hit effect,
white sword slash with impact sparks,
physical attack hit VFX, game effect sprite,
transparent background, vibrant white colors
--ar 2:1 --style raw --v 6
```

### 2. 魔法攻击命中 ⭐ P0
**文件名**：`fx_hit_magic_01.png` ~ `fx_hit_magic_02.png`

```
sprite sheet, 2 frames, cartoon magic explosion effect,
blue magic burst with sparkles,
magical attack hit VFX, game effect sprite,
transparent background, vibrant blue colors
--ar 2:1 --style raw --v 6
```

### 3. 暴击命中 ⭐ P0
**文件名**：`fx_hit_critical_01.png` ~ `fx_hit_critical_04.png`

```
sprite sheet, 4 frames, cartoon critical hit effect,
large red slash with stars and impact explosion,
"POW" comic style impact, critical hit VFX,
game effect sprite, transparent background, vibrant red gold colors
--ar 4:1 --style raw --v 6
```

---

## 控制效果特效

### 4. 减速效果 ⭐ P0
**文件名**：`fx_slow_01.png` ~ `fx_slow_02.png`

```
sprite sheet, 2 frames, cartoon slow debuff effect,
blue frost mark on ground beneath character,
ice crystals forming, slow movement indicator,
game status effect sprite, transparent background, ice blue colors
--ar 2:1 --style raw --v 6
```

### 5. 眩晕效果 ⭐ P0
**文件名**：`fx_stun_01.png` ~ `fx_stun_04.png`

```
sprite sheet, 4 frames, cartoon stun effect,
yellow stars spinning above character head,
dizzy stars rotating animation, comic style,
game status effect sprite, transparent background, yellow colors
--ar 4:1 --style raw --v 6
```

### 6. 冰冻效果 ⭐ P0
**文件名**：`fx_frozen_01.png` ~ `fx_frozen_02.png`

```
sprite sheet, 2 frames, cartoon freeze effect,
ice block encasing character, blue ice crystal prison,
frozen solid with frost particles,
game status effect sprite, transparent background, ice blue colors
--ar 2:1 --style raw --v 6
```

### 7. 中毒效果 ⭐ P0
**文件名**：`fx_poison_01.png` ~ `fx_poison_04.png`

```
sprite sheet, 4 frames, cartoon poison effect,
green toxic bubbles rising from character,
poison mist with bubbling animation,
game status effect sprite, transparent background, green colors
--ar 4:1 --style raw --v 6
```

---

## 战斗事件特效

### 8. 怪物死亡 ⭐ P0
**文件名**：`fx_enemy_death_01.png` ~ `fx_enemy_death_06.png`

```
sprite sheet, 6 frames, cartoon enemy death explosion,
poof smoke cloud with gold coins flying out,
cartoony disappear effect, sparkles and smoke,
game death VFX, transparent background, gray smoke gold coins
--ar 6:1 --style raw --v 6
```

### 9. 英雄放置 ⭐ P0
**文件名**：`fx_hero_place_01.png` ~ `fx_hero_place_04.png`

```
sprite sheet, 4 frames, cartoon landing dust effect,
character landing on ground, dust cloud poof,
impact dust particles spreading outward,
game placement VFX, transparent background, brown dust colors
--ar 4:1 --style raw --v 6
```

### 10. 英雄升级 ⭐ P0
**文件名**：`fx_hero_levelup_01.png` ~ `fx_hero_levelup_06.png`

```
sprite sheet, 6 frames, cartoon level up effect,
golden light pillar shooting upward,
sparkles and golden particles rising,
level number popping up, celebration effect,
game level up VFX, transparent background, golden colors
--ar 6:1 --style raw --v 6
```

### 11. 金币掉落 ⭐ P0
**文件名**：`fx_gold_drop_01.png` ~ `fx_gold_drop_04.png`

```
sprite sheet, 4 frames, cartoon gold coin drop effect,
spinning gold coin flying upward toward UI,
golden sparkle trail, coin rotation animation,
game gold pickup VFX, transparent background, gold colors
--ar 4:1 --style raw --v 6
```

### 12. 护盾破碎 ⭐ P1
**文件名**：`fx_shield_break_01.png` ~ `fx_shield_break_04.png`

```
sprite sheet, 4 frames, cartoon shield breaking effect,
blue magical shield shattering into fragments,
glass-like blue shards flying outward,
game shield break VFX, transparent background, blue colors
--ar 4:1 --style raw --v 6
```

---

## 📋 生成注意事项

1. 特效素材必须是 **透明背景**
2. 特效风格要统一为 **卡通风格**，色彩鲜明
3. 控制效果特效需要能 **循环播放**（首尾帧衔接）
4. 建议使用 **GPT-4o** 生成小尺寸特效，效果较好
5. 暴击特效要比普通攻击特效 **更大更醒目**

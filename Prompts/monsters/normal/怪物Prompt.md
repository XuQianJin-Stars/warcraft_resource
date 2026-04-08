# 怪物美术 Prompt

> **用途**：战斗场景中沿路径行走的怪物
> **工具**：Midjourney 生成
> **风格**：Q版卡通，小尺寸精灵图，粗描边
> **输出格式**：PNG（透明背景），每帧 48×48px ~ 64×64px
> **动画需求**：行走4帧 + 死亡4帧

---

## 通用 Prompt 模板（Midjourney）

### 静态精灵图（MVP方案B）
```
pixel art style, chibi cartoon, {怪物名称} from Warcraft 3,
{简要外观描述}, tiny enemy sprite, side view,
game sprite, white background, thick outline, vibrant colors
--ar 1:1 --style raw --v 6
```

### 行走动画帧序列
```
sprite sheet, 4 frames, chibi cartoon {怪物名称},
{简要外观描述}, walking animation sequence,
side view, game sprite sheet, white background
--ar 4:1 --style raw --v 6
```

---

## 普通怪物（地面）

### 1. 食尸鬼（Ghoul）⭐ P0
**文件名**：`monster_ghoul_walk_01.png` ~ `monster_ghoul_walk_04.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Ghoul from Warcraft 3,
undead creature, pale green rotting skin, sharp claws,
hunched posture, ragged clothes, glowing yellow eyes,
tiny enemy sprite, side view walking pose,
game sprite, white background, thick outline
--ar 1:1 --style raw --v 6
```

**行走动画：**
```
sprite sheet, 4 frames, chibi cartoon Ghoul,
undead creature, pale green skin, sharp claws,
walking animation, hunched shambling gait,
side view, game sprite sheet, white background
--ar 4:1 --style raw --v 6
```

### 2. 狼骑兵（Wolf Rider）⭐ P0
**文件名**：`monster_wolf_rider_walk_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Wolf Rider from Warcraft 3,
orc riding a large wolf, green skin orc with spear,
gray wolf mount, tribal armor, aggressive pose,
tiny enemy sprite, side view,
game sprite, white background, thick outline
--ar 1:1 --style raw --v 6
```

### 3. 步兵（Footman）⭐ P0
**文件名**：`monster_footman_walk_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Footman from Warcraft 3,
human soldier, blue and silver armor, sword and shield,
blue cape, helmet with visor, marching pose,
tiny enemy sprite, side view,
game sprite, white background, thick outline
--ar 1:1 --style raw --v 6
```

### 4. 暗夜豹骑（Huntress）⭐ P0 （快速型）
**文件名**：`monster_huntress_walk_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Huntress from Warcraft 3,
night elf female riding a nightsaber panther,
purple skin elf, silver armor, throwing glaive,
dark purple panther mount, fast running pose,
tiny enemy sprite, side view,
game sprite, white background, thick outline
--ar 1:1 --style raw --v 6
```

### 5. 风骑士（Wind Rider）⭐ P1 （快速型）
**文件名**：`monster_wind_rider_walk_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Wind Rider from Warcraft 3,
orc riding a wyvern, green skin orc with spear,
brown wyvern with bat wings and scorpion tail,
flying pose, tiny enemy sprite, side view,
game sprite, white background, thick outline
--ar 1:1 --style raw --v 6
```

### 6. 骑士（Knight）⭐ P0 （重甲型）
**文件名**：`monster_knight_walk_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Knight from Warcraft 3,
human heavy cavalry, full plate silver armor,
riding armored warhorse, lance and shield,
blue and gold heraldry, heavy marching pose,
tiny enemy sprite, side view,
game sprite, white background, thick outline
--ar 1:1 --style raw --v 6
```

### 7. 石像鬼-地面（Gargoyle Ground）⭐ P1 （重甲型）
**文件名**：`monster_gargoyle_ground_walk_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Gargoyle from Warcraft 3,
stone creature in ground form, gray stone skin,
folded wings, sharp claws, walking on all fours,
heavy stone body, tiny enemy sprite, side view,
game sprite, white background, thick outline
--ar 1:1 --style raw --v 6
```

### 8. 憎恶（Abomination）⭐ P1 （重甲型）
**文件名**：`monster_abomination_walk_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Abomination from Warcraft 3,
huge undead stitched monster, multiple arms,
exposed guts and stitches, meat cleaver weapon,
bloated body, green toxic aura, shambling walk,
tiny enemy sprite, side view,
game sprite, white background, thick outline
--ar 1:1 --style raw --v 6
```

---

## 飞行怪物

### 9. 双足飞龙（Wyvern）⭐ P0
**文件名**：`monster_wyvern_fly_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Wyvern from Warcraft 3,
two-legged flying dragon, bat-like wings spread,
scorpion tail with poison stinger, brown scales,
flying pose, tiny enemy sprite, side view,
game sprite, white background, thick outline
--ar 1:1 --style raw --v 6
```

### 10. 角鹰兽（Hippogryph）⭐ P1
**文件名**：`monster_hippogryph_fly_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Hippogryph from Warcraft 3,
eagle-stag hybrid creature, large wings spread,
purple and silver feathers, antlers on head,
majestic flying pose, tiny enemy sprite, side view,
game sprite, white background, thick outline
--ar 1:1 --style raw --v 6
```

### 11. 石像鬼-飞行（Gargoyle Air）⭐ P1
**文件名**：`monster_gargoyle_air_fly_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Gargoyle from Warcraft 3,
stone creature in flight form, wings spread wide,
gray stone skin, sharp claws extended,
flying attack pose, tiny enemy sprite, side view,
game sprite, white background, thick outline
--ar 1:1 --style raw --v 6
```

---

## 魔法免疫怪物

### 12. 破法者（Spell Breaker）⭐ P1
**文件名**：`monster_spell_breaker_walk_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Spell Breaker from Warcraft 3,
blood elf warrior, golden and red armor,
double-bladed weapon, anti-magic shield glow,
red cape, pointed elf ears, walking pose,
tiny enemy sprite, side view,
game sprite, white background, thick outline
--ar 1:1 --style raw --v 6
```

### 13. 女妖（Banshee）⭐ P1
**文件名**：`monster_banshee_walk_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Banshee from Warcraft 3,
ghostly undead female, translucent pale blue body,
flowing ghostly hair, tattered robes,
screaming expression, floating above ground,
eerie blue glow, tiny enemy sprite, side view,
game sprite, white background, thick outline
--ar 1:1 --style raw --v 6
```

---

## 通用怪物死亡动画

**文件名**：`fx_monster_death_01.png` ~ `fx_monster_death_06.png`

```
sprite sheet, 6 frames, cartoon explosion poof effect,
enemy death animation, smoke cloud with gold coins flying out,
cartoony "poof" disappear effect, game VFX,
transparent background, vibrant colors
--ar 6:1 --style raw --v 6
```

---

## 📋 生成注意事项

1. **MVP阶段**：优先生成 P0 的 5 种怪物静态精灵图
2. 怪物精灵图建议比英雄稍小（48×48 ~ 64×64），体现体型差异
3. 所有怪物统一使用 **侧面视角**（side view），方便沿路径行走
4. 死亡动画可以使用通用的卡通爆炸烟雾效果
5. 飞行怪物需要有明显的翅膀展开/飞行姿态

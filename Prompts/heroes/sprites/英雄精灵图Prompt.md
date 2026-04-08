# 英雄地图模型动画 Prompt（64×64px ~ 96×96px）

> **用途**：战斗场景中放置在地图上的英雄显示
> **工具**：Midjourney 生成静态帧 → 手动调整为动画帧 / 或程序模拟动画
> **风格**：Q版卡通，像素风/小尺寸精灵图，粗描边
> **输出格式**：PNG（透明背景），每帧 64×64px 或 96×96px
> **动画需求**：待机4帧 + 攻击4-6帧 + 技能释放4-6帧 + 升级特效（通用）

---

## 方案选择

### 方案A：AI生成多帧动画（推荐后期使用）
使用 Midjourney 生成角色的多个姿态，手动拆分为动画帧。

### 方案B：AI生成单帧 + 程序模拟动画（推荐MVP阶段）
只生成1张静态精灵图，通过程序实现简单的缩放/摇摆/闪烁动画。
**MVP阶段强烈推荐此方案，可快速让游戏跑起来。**

---

## 通用 Prompt 模板（Midjourney - 静态精灵图）

```
pixel art style, chibi cartoon, {英雄名称} from Warcraft 3,
{简要外观描述}, tiny character sprite, 
top-down perspective, game sprite sheet,
white background, thick outline, vibrant colors,
64x64 pixel size, transparent background
--ar 1:1 --style raw --v 6
```

## 通用 Prompt 模板（Midjourney - 动画帧序列）

```
sprite sheet, pixel art style, chibi cartoon,
{英雄名称} from Warcraft 3, {简要外观描述},
4 frame animation sequence, idle animation,
tiny character, top-down view, game sprite,
white background, thick outline, vibrant colors
--ar 4:1 --style raw --v 6
```

---

## 🔵 人族英雄精灵图

### 1. 大法师（Archmage）⭐ P0
**文件名**：`hero_archmage_idle_01.png` ~ `hero_archmage_idle_04.png`

**静态精灵图（MVP方案B）：**
```
pixel art style, chibi cartoon, Archmage from Warcraft 3,
blue robe wizard, white beard, magic staff with glowing crystal,
pointed hat, tiny character sprite, top-down perspective,
game sprite, white background, thick outline, vibrant blue colors
--ar 1:1 --style raw --v 6
```

**待机动画帧（方案A）：**
```
sprite sheet, 4 frames, chibi cartoon Archmage,
blue robe, white beard, magic staff,
idle breathing animation, slight staff glow pulse,
tiny character, game sprite sheet, white background
--ar 4:1 --style raw --v 6
```

**攻击动画帧：**
```
sprite sheet, 4 frames, chibi cartoon Archmage,
blue robe, white beard, casting magic spell,
staff raised, blue magic projectile launching,
attack animation sequence, game sprite sheet, white background
--ar 4:1 --style raw --v 6
```

### 2. 山丘之王（Mountain King）⭐ P0
**文件名**：`hero_mountain_king_idle_01.png` ~ `hero_mountain_king_idle_04.png`

**静态精灵图（MVP方案B）：**
```
pixel art style, chibi cartoon, Mountain King from Warcraft 3,
dwarf warrior, golden armor, thunder hammer, viking helmet,
red beard, tiny character sprite, top-down perspective,
game sprite, white background, thick outline, vibrant gold colors
--ar 1:1 --style raw --v 6
```

**攻击动画帧：**
```
sprite sheet, 4 frames, chibi cartoon Mountain King,
dwarf warrior, golden armor, swinging thunder hammer,
hammer smash attack animation, lightning sparks,
game sprite sheet, white background
--ar 4:1 --style raw --v 6
```

### 3. 圣骑士（Paladin）⭐ P0
**文件名**：`hero_paladin_idle_01.png`

**静态精灵图（MVP方案B）：**
```
pixel art style, chibi cartoon, Paladin from Warcraft 3,
silver holy armor, golden hammer, shield with griffin emblem,
blonde hair, holy light aura, tiny character sprite,
game sprite, white background, thick outline, vibrant colors
--ar 1:1 --style raw --v 6
```

### 4. 血法师（Blood Mage）⭐ P1
**文件名**：`hero_blood_mage_idle_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Blood Mage from Warcraft 3,
elf mage, red robe, golden hair, green glowing orb,
pointed ears, fire magic, tiny character sprite,
game sprite, white background, thick outline, vibrant red colors
--ar 1:1 --style raw --v 6
```

---

## 🔴 兽族英雄精灵图

### 5. 剑圣（Blademaster）⭐ P0
**文件名**：`hero_blademaster_idle_01.png`

**静态精灵图（MVP方案B）：**
```
pixel art style, chibi cartoon, Blademaster from Warcraft 3,
orc samurai, green skin, red cape, katana sword,
tribal tattoo, battle stance, tiny character sprite,
game sprite, white background, thick outline, vibrant red colors
--ar 1:1 --style raw --v 6
```

**攻击动画帧：**
```
sprite sheet, 6 frames, chibi cartoon Blademaster,
orc samurai, green skin, katana slash animation,
sword swing sequence with motion blur trail,
game sprite sheet, white background
--ar 6:1 --style raw --v 6
```

### 6. 先知（Far Seer）⭐ P0
**文件名**：`hero_far_seer_idle_01.png`

**静态精灵图（MVP方案B）：**
```
pixel art style, chibi cartoon, Far Seer from Warcraft 3,
orc shaman, green skin, totem staff, lightning glow,
tribal robes, wolf companion nearby, tiny character sprite,
game sprite, white background, thick outline, vibrant colors
--ar 1:1 --style raw --v 6
```

### 7. 牛头人酋长（Tauren Chieftain）⭐ P1
**文件名**：`hero_tauren_chieftain_idle_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Tauren Chieftain from Warcraft 3,
minotaur warrior, brown fur, huge horns, totem halberd,
tribal armor, massive body, tiny character sprite,
game sprite, white background, thick outline, vibrant brown colors
--ar 1:1 --style raw --v 6
```

### 8. 暗影猎手（Shadow Hunter）⭐ P1
**文件名**：`hero_shadow_hunter_idle_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Shadow Hunter from Warcraft 3,
troll hunter, blue skin, voodoo mask, spear, feathers,
tribal light armor, tiny character sprite,
game sprite, white background, thick outline, vibrant purple colors
--ar 1:1 --style raw --v 6
```

---

## 🟣 不死族英雄精灵图

### 9. 死亡骑士（Death Knight）⭐ P0
**文件名**：`hero_death_knight_idle_01.png`

**静态精灵图（MVP方案B）：**
```
pixel art style, chibi cartoon, Death Knight from Warcraft 3,
dark knight, pale skin, ice blue glowing eyes,
dark armor with purple runes, Frostmourne glowing sword,
death energy aura, tiny character sprite,
game sprite, white background, thick outline, vibrant dark purple colors
--ar 1:1 --style raw --v 6
```

### 10. 巫妖（Lich）⭐ P0
**文件名**：`hero_lich_idle_01.png`

**静态精灵图（MVP方案B）：**
```
pixel art style, chibi cartoon, Lich from Warcraft 3,
skeleton mage, floating, purple robe, skull face,
blue flame eyes, ice frost magic glow, tiny character sprite,
game sprite, white background, thick outline, vibrant ice blue colors
--ar 1:1 --style raw --v 6
```

### 11. 恐惧魔王（Dreadlord）⭐ P1
**文件名**：`hero_dreadlord_idle_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Dreadlord from Warcraft 3,
demon lord, bat wings, purple skin, demon horns,
red glowing eyes, dark armor, tiny character sprite,
game sprite, white background, thick outline, vibrant dark purple colors
--ar 1:1 --style raw --v 6
```

### 12. 地穴领主（Crypt Lord）⭐ P1
**文件名**：`hero_crypt_lord_idle_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Crypt Lord from Warcraft 3,
spider lord, dark green carapace, spikes, multiple legs,
venomous fangs, green poison mist, tiny character sprite,
game sprite, white background, thick outline, vibrant dark green colors
--ar 1:1 --style raw --v 6
```

---

## 🌙 暗夜精灵英雄精灵图

### 13. 恶魔猎手（Demon Hunter）⭐ P0
**文件名**：`hero_demon_hunter_idle_01.png`

**静态精灵图（MVP方案B）：**
```
pixel art style, chibi cartoon, Demon Hunter from Warcraft 3,
blindfolded elf, purple skin, twin warglaives,
demon tattoos glowing green, dark blue hair,
tiny character sprite, game sprite, white background,
thick outline, vibrant green and purple colors
--ar 1:1 --style raw --v 6
```

### 14. 丛林守护者（Keeper of the Grove）⭐ P1
**文件名**：`hero_keeper_of_grove_idle_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Keeper of the Grove from Warcraft 3,
treant form, deer antlers with leaves, wooden body,
nature magic green glow, tiny character sprite,
game sprite, white background, thick outline, vibrant green colors
--ar 1:1 --style raw --v 6
```

### 15. 月之女祭司（Priestess of the Moon）⭐ P0
**文件名**：`hero_priestess_of_moon_idle_01.png`

**静态精灵图（MVP方案B）：**
```
pixel art style, chibi cartoon, Priestess of the Moon from Warcraft 3,
night elf female, silver armor, moon bow, white tiger mount,
silver white hair, moon crown, moonlight aura,
tiny character sprite, game sprite, white background,
thick outline, vibrant silver and blue colors
--ar 1:1 --style raw --v 6
```

### 16. 守望者（Warden）⭐ P1
**文件名**：`hero_warden_idle_01.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Warden from Warcraft 3,
night elf assassin, dark blue cloak, silver mask,
throwing knives, shadow energy, tiny character sprite,
game sprite, white background, thick outline, vibrant dark blue colors
--ar 1:1 --style raw --v 6
```

---

## 🌟 通用升级特效

**文件名**：`fx_hero_levelup_01.png` ~ `fx_hero_levelup_06.png`

```
sprite sheet, 6 frames, golden light pillar effect,
level up animation, golden particles rising,
sparkle and glow effect, game VFX sprite sheet,
transparent background, cartoon style
--ar 6:1 --style raw --v 6
```

---

## 📋 生成注意事项

1. **MVP阶段**：每个英雄只需生成1张静态精灵图（方案B），程序模拟动画
2. **后期阶段**：再补充完整的动画帧序列（方案A）
3. 精灵图需要 **透明背景**，生成后用 remove.bg 处理
4. 建议生成时使用 **1:1 比例**，后续缩放到 64×64 或 96×96
5. 如果 Midjourney 生成的精灵图风格不统一，可以用同一个 seed 值保持一致性

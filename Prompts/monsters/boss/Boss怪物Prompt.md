# Boss怪物美术 Prompt

> **用途**：Boss波次中出现的强力敌人
> **工具**：Midjourney 生成
> **风格**：Q版卡通，比普通怪物更大更精细，粗描边
> **输出格式**：PNG（透明背景），每帧 96×96px ~ 128×128px
> **动画需求**：行走6帧 + 技能释放6帧 + 死亡6帧（伊利丹额外+变身6帧）

---

## 通用 Prompt 模板（Midjourney）

```
pixel art style, chibi cartoon, {Boss名称} from Warcraft 3,
{详细外观描述}, large boss character sprite,
imposing and powerful presence, side view,
game boss sprite, white background, thick outline,
vibrant colors, detailed design
--ar 1:1 --style raw --v 6
```

---

### 1. 阿克蒙德（Archimonde）⭐ P0
**文件名**：`boss_archimonde_walk_01.png` ~ `boss_archimonde_walk_06.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Archimonde from Warcraft 3,
massive eredar demon lord, dark purple skin,
huge curved horns, glowing green eyes,
dark robes with fel green energy, clawed hands,
towering imposing figure, green fel fire aura,
large boss character sprite, side view,
game boss sprite, white background, thick outline, vibrant colors
--ar 1:1 --style raw --v 6
```

**技能释放（末日降临）：**
```
sprite sheet, 6 frames, chibi cartoon Archimonde,
casting apocalypse spell, hands raised above head,
dark red energy gathering, massive explosion,
fel green and dark red energy burst,
boss skill animation, game sprite sheet, white background
--ar 6:1 --style raw --v 6
```

---

### 2. 基尔加丹（Kil'jaeden）⭐ P0
**文件名**：`boss_kiljaeden_walk_01.png` ~ `boss_kiljaeden_walk_06.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Kil'jaeden from Warcraft 3,
massive eredar demon lord, crimson red skin,
huge horns, burning fel green eyes,
dark ornate demonic armor, massive clawed hands,
emerging from dark portal, fel fire surrounding body,
large boss character sprite, side view,
game boss sprite, white background, thick outline, vibrant colors
--ar 1:1 --style raw --v 6
```

**技能释放（暗影之手）：**
```
sprite sheet, 6 frames, chibi cartoon Kil'jaeden,
casting shadow hand spell, dark purple giant hand
reaching forward to grab, dark energy tendrils,
boss skill animation, game sprite sheet, white background
--ar 6:1 --style raw --v 6
```

---

### 3. 阿尔萨斯/巫妖王（Arthas / Lich King）⭐ P0
**文件名**：`boss_lich_king_walk_01.png` ~ `boss_lich_king_walk_06.png`

**静态精灵图：**
```
pixel art style, chibi cartoon, Lich King Arthas from Warcraft 3,
death knight in frozen throne armor, ice blue glowing eyes,
Helm of Domination crown, massive Frostmourne sword,
dark blue and ice white armor with frost runes,
ice frost aura surrounding, cape flowing,
large boss character sprite, side view,
game boss sprite, white background, thick outline, vibrant ice blue colors
--ar 1:1 --style raw --v 6
```

**技能释放（霜之哀伤）：**
```
sprite sheet, 6 frames, chibi cartoon Lich King,
swinging Frostmourne in wide arc, ice blue shockwave,
frost explosion spreading across screen,
boss skill animation, game sprite sheet, white background
--ar 6:1 --style raw --v 6
```

---

### 4. 伊利丹（Illidan Stormrage）⭐ P0
**文件名**：`boss_illidan_walk_01.png` ~ `boss_illidan_walk_06.png`

**静态精灵图（普通形态）：**
```
pixel art style, chibi cartoon, Illidan Stormrage from Warcraft 3,
demon hunter, purple skin, blindfolded with green glow,
twin Warglaives of Azzinoth, demon tattoos glowing,
dark blue long hair, pointed elf ears, muscular build,
large boss character sprite, side view,
game boss sprite, white background, thick outline, vibrant green purple colors
--ar 1:1 --style raw --v 6
```

**变身形态（恶魔形态）：**
```
pixel art style, chibi cartoon, Illidan demon form from Warcraft 3,
fully transformed demon, huge bat wings spread,
dark green skin, demon horns, hooves instead of feet,
burning fel green eyes, massive claws,
dark green fel fire aura, terrifying powerful pose,
large boss character sprite, side view,
game boss sprite, white background, thick outline, vibrant dark green colors
--ar 1:1 --style raw --v 6
```

**变身动画：**
```
sprite sheet, 6 frames, chibi cartoon Illidan transformation,
night elf to demon form, wings growing, body changing,
green fel energy explosion, dramatic transformation sequence,
boss transformation animation, game sprite sheet, white background
--ar 6:1 --style raw --v 6
```

---

## 📋 生成注意事项

1. Boss精灵图应该比普通怪物 **大1.5-2倍**（96×96 ~ 128×128px）
2. Boss需要更多细节和更精细的设计，体现其强大感
3. 每个Boss建议生成 **多个变体** 选取最佳
4. 伊利丹需要 **两套** 精灵图（普通形态 + 恶魔变身形态）
5. Boss技能特效可以单独生成，参考 `effects/hero_skills/boss/` 目录

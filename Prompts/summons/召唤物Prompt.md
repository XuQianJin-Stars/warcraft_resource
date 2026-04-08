# 召唤物美术 Prompt

> **用途**：英雄技能召唤出的战斗单位
> **工具**：Midjourney 生成
> **风格**：Q版卡通，小尺寸精灵图，粗描边
> **输出格式**：PNG（透明背景），每帧 48×48px ~ 64×64px
> **动画需求**：待机4帧 + 攻击4帧 + 消散4帧

---

## 通用 Prompt 模板

```
pixel art style, chibi cartoon, {召唤物名称} from Warcraft 3,
{简要外观描述}, summoned creature sprite,
magical glowing aura, game sprite, side view,
white background, thick outline, vibrant colors
--ar 1:1 --style raw --v 6
```

---

### 1. 水元素（Water Elemental）⭐ P0 — 大法师召唤
**文件名**：`summon_water_elemental_idle_01.png`

```
pixel art style, chibi cartoon, Water Elemental from Warcraft 3,
translucent blue water body, humanoid shape made of water,
glowing blue eyes, water droplets splashing around,
magical water aura, summoned creature sprite, side view,
game sprite, white background, thick outline, vibrant blue colors
--ar 1:1 --style raw --v 6
```

### 2. 狼骑兵-召唤（Spirit Wolf）⭐ P0 — 先知召唤
**文件名**：`summon_spirit_wolf_idle_01.png`

```
pixel art style, chibi cartoon, Spirit Wolf from Warcraft 3,
ghostly translucent wolf, blue-white spirit glow,
fierce wolf with glowing eyes, ethereal mist trail,
spirit animal summoned creature, side view,
game sprite, white background, thick outline, vibrant blue white colors
--ar 1:1 --style raw --v 6
```

### 3. 树人（Treant）⭐ P1 — 丛林守护者召唤
**文件名**：`summon_treant_idle_01.png`

```
pixel art style, chibi cartoon, Treant from Warcraft 3,
small walking tree creature, brown bark body,
green leaves as hair, wooden arms and legs,
nature magic green glow, cute tree face,
summoned creature sprite, side view,
game sprite, white background, thick outline, vibrant green brown colors
--ar 1:1 --style raw --v 6
```

### 4. 地狱火（Infernal）⭐ P1 — 恐惧魔王召唤
**文件名**：`summon_infernal_idle_01.png`

```
pixel art style, chibi cartoon, Infernal from Warcraft 3,
massive rock golem on fire, dark stone body,
burning with green fel fire, glowing green cracks,
molten lava veins, imposing rocky figure,
summoned creature sprite, side view,
game sprite, white background, thick outline, vibrant green fire colors
--ar 1:1 --style raw --v 6
```

### 5. 骷髅战士（Skeleton Warrior）⭐ P1 — 死亡骑士召唤
**文件名**：`summon_skeleton_warrior_idle_01.png`

```
pixel art style, chibi cartoon, Skeleton Warrior from Warcraft 3,
animated skeleton soldier, rusty sword and shield,
tattered armor remnants, glowing green eye sockets,
undead green aura, rattling bones,
summoned creature sprite, side view,
game sprite, white background, thick outline, vibrant bone white green colors
--ar 1:1 --style raw --v 6
```

### 6. 腐尸甲虫（Carrion Beetle）⭐ P1 — 地穴领主召唤
**文件名**：`summon_carrion_beetle_idle_01.png`

```
pixel art style, chibi cartoon, Carrion Beetle from Warcraft 3,
large undead scarab beetle, dark green carapace,
glowing green eyes, sharp mandibles,
toxic green aura, crawling insect pose,
summoned creature sprite, side view,
game sprite, white background, thick outline, vibrant dark green colors
--ar 1:1 --style raw --v 6
```

### 7. 毒蛇守卫（Serpent Ward）⭐ P1 — 暗影猎手召唤
**文件名**：`summon_serpent_ward_idle_01.png`

```
pixel art style, chibi cartoon, Serpent Ward from Warcraft 3,
tiki totem pole with snake head on top,
wooden tribal totem, green poison glow,
snake eyes glowing, voodoo decorations,
stationary ward sprite, front view,
game sprite, white background, thick outline, vibrant green purple colors
--ar 1:1 --style raw --v 6
```

### 8. 剑圣镜像（Mirror Image）⭐ P1 — 剑圣召唤
**说明**：复用剑圣精灵图，程序处理为半透明 + 蓝色色调

### 9. 烈焰凤凰（Phoenix）⭐ P1 — 血法师召唤
**文件名**：`summon_phoenix_idle_01.png`

```
pixel art style, chibi cartoon, Phoenix from Warcraft 3,
majestic fire bird, golden and red feathers,
burning with bright flames, long fiery tail,
wings spread in flight, fire trail behind,
summoned creature sprite, side view,
game sprite, white background, thick outline, vibrant fire red gold colors
--ar 1:1 --style raw --v 6
```

### 10. 复仇之魂（Vengeance Spirit）⭐ P1 — 守望者召唤
**文件名**：`summon_vengeance_spirit_idle_01.png`

```
pixel art style, chibi cartoon, Vengeance Spirit from Warcraft 3,
ghostly night elf spirit, translucent green glow,
ethereal female figure, flowing ghostly robes,
green spirit energy trail, vengeful expression,
summoned creature sprite, side view,
game sprite, white background, thick outline, vibrant green colors
--ar 1:1 --style raw --v 6
```

### 11. 猫头鹰哨兵（Owl Scout）⭐ P2 — 月之女祭司召唤
**文件名**：`summon_owl_scout_idle_01.png`

```
pixel art style, chibi cartoon, Owl Scout from Warcraft 3,
small magical owl, silver and purple feathers,
glowing silver eyes, moonlight aura,
flying pose with wings spread, cute cartoon owl,
summoned creature sprite, side view,
game sprite, white background, thick outline, vibrant silver purple colors
--ar 1:1 --style raw --v 6
```

---

## 通用消散特效

**文件名**：`fx_summon_dissolve_01.png` ~ `fx_summon_dissolve_04.png`

```
sprite sheet, 4 frames, magical dissolve effect,
summoned creature disappearing animation,
blue sparkles and fading particles,
game VFX sprite sheet, transparent background
--ar 4:1 --style raw --v 6
```

---

## 📋 生成注意事项

1. 召唤物尺寸应与英雄精灵图相近或稍小
2. 召唤物需要有明显的 **魔法光环/半透明效果**，区别于普通单位
3. 剑圣镜像不需要单独生成，程序处理即可
4. 消散特效可以通用，所有召唤物共用一套

---
name: animated-pixel-art
description: Use when a user provides pixel art or a layered pixel-art scene and wants it turned into a polished looping animation, animated WebP/GIF, keyframes, sprite-like motion, expressive idle movement, environmental animation, or a reusable animation bundle.
---

# Animated Pixel Art

## Overview
Turn static pixel-art assets into polished, seamless animation loops while preserving the original composition, pixel language, silhouettes, and transparency.

## When to Use
Use this skill for animated pixel art, looping pixel-art backgrounds, animated WebP/GIF, expressive idle loops, blinking/breathing/bounce, moving water/clouds/foliage/lights/particles, parallax, keyframes, sprite-like motion, or requests such as “make this feel alive”.

## Core Quality Rules
1. Preserve source identity: composition, palette logic, silhouette, pixel density.
2. Animate by hierarchy: primary subject, secondary motion, environment, lighting, camera.
3. Use anticipation -> action -> settle.
4. Make the first/last transition seamless.
5. Use nearest-neighbor transforms for pixel art; avoid global blur.
6. Blur only glow/bloom layers, not core art.
7. Avoid animating every element with the same timing.
8. Keep calm areas calm so expressive motion reads.

## Workflow
### 1. Inspect source
Determine canvas size, alpha, focal object, motion-capable regions, background/foreground, and likely loop duration.

### 2. Build a motion plan
Choose 3-7 independent channels.

Character/object ideas:
- breathing squash/stretch
- blink
- eye shift
- head nod
- small bounce
- accessory follow-through
- expression change

Environment ideas:
- grass/leaf/vine sway
- water shimmer
- reflection drift
- cloud drift
- mist/snow/rain/smoke
- birds or floating motes

Lighting ideas:
- lantern/fireplace flicker
- star/window twinkle
- light rays
- sparkles/fireflies

### 3. Pick loop timing
- sticker/idle: 2.5-4s
- landscape: 4-8s
- expressive character: 2-4s
- ambient wallpaper: 6-12s

Prefer 24-48 source frames for smooth loops unless stepped animation is intentional.

### 4. Create frames
- keep the original image as visual master
- isolate regions using bounding boxes/masks
- transform only intended regions
- alpha composite layers
- use nearest-neighbor resizing for pixel-art transforms
- generate/redraw true keyframes when motion cannot be faked well

### 5. Add asynchronous timing
Do not peak all elements together. Offset motion phases and use different cycle counts.

### 6. Verify seam
Check position jumps, particle pops, lighting jumps, expression jumps, foliage snaps, and alpha artifacts.

### 7. Export
Preferred output:
- animation.webp
- animation.gif
- frames/frame_01.png...
- keyframes_sheet.png
- animation_plan.md

## Animation Profiles

### Expressive Character / Object
Use 4-7 of:
- 1-3 px body float
- subtle squash/stretch
- 1-2 blink moments
- eye direction shift
- changing smile/mouth
- head nod/bird hop
- accessory motion
- reaction accent
- particles timed to expressions

The animation should feel acted, not mechanically oscillated.

### Mountain / Lake Landscape
Good channels:
- water reflection shimmer
- horizontal glints
- slow cloud drift
- distant mist
- subtle foreground foliage movement
- occasional birds
- tiny atmospheric brightness changes
- optional parallax

Do not heavily warp mountain silhouettes.

### Cozy Pixel Scene
Good channels:
- lantern/fireplace pulse
- warm bloom
- blinking character
- breathing
- steam curls
- drifting fireflies
- subtle leaves/vines
- small object bounce
- star/window twinkle

## Common Mistakes
- Whole-image bobbing only -> separate motion layers.
- Same sine wave everywhere -> offset timing and cycles.
- Too much deformation -> keep core art stable.
- Global blur -> blur only glow.
- Bad seam -> use periodic motion and fade/wrap particles.
- Random sparkles as “complexity” -> prioritize focal expression first.

## Bundle Standard
```text
animated-pixel-art-output/
├── animation.webp
├── animation.gif
├── keyframes_sheet.png
├── animation_plan.md
└── frames/
    ├── frame_01.png
    └── ...
```

Skill package:
```text
animated-pixel-art/
├── SKILL.md
├── scripts/
│   └── animate_pixel_art.py
└── references/
    └── prompt-recipes.md
```

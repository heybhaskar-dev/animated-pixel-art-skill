# Animated Pixel Art Skill

A reusable AI skill for turning static pixel-art assets into polished, seamless animations.

It is designed for workflows where you provide pixel art and want outputs such as:

- animated WebP
- GIF previews
- PNG frame sequences
- keyframe sheets
- expressive idle animations
- environmental motion
- parallax-style landscape animation
- cozy pixel-art loops

## What it focuses on

The skill encourages animation that feels authored rather than mechanically moved.

It uses motion layers such as:

- character breathing
- blinking
- eye movement
- head nods
- bird/object bounce
- foliage sway
- water shimmer
- cloud drift
- lantern glow
- particles and sparkles
- subtle parallax

It also emphasizes:

- seamless loops
- crisp pixel edges
- nearest-neighbor scaling
- clean transparency
- independent timing across animation layers

## Repository structure

```text
animated-pixel-art/
├── SKILL.md
├── scripts/
│   └── animate_pixel_art.py
└── references/
    └── prompt-recipes.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/animated-pixel-art-skill.git
```

Then copy the skill folder into your agent's skills directory.

Common locations include:

```text
~/.agents/skills/
~/.claude/skills/
```

Example:

```bash
cp -r animated-pixel-art-skill/animated-pixel-art ~/.agents/skills/
```

## Example prompt

```text
Animate this transparent pixel-art asset into a premium seamless idle loop.

Keep the original design, palette, composition, and pixel density.

Make the focal character feel alive with blinking, subtle breathing,
small expression changes, secondary object movement, pulsing light,
environmental motion, and restrained particles.

Preserve transparency and crisp pixel edges.

Export:
- animated WebP
- GIF preview
- PNG frames
- keyframe sheet
```

## Landscape example

```text
Turn this pixel-art mountain-and-lake scene into a calm seamless ambient loop.

Keep mountains stable.

Animate:
- lake reflections
- horizontal water glints
- slow cloud drift
- distant mist
- subtle tree movement
- occasional birds
- restrained parallax

Do not distort the mountain silhouettes.
```

## Requirements

The included starter script uses:

```bash
pip install pillow
```

Run it with:

```bash
python animated-pixel-art/scripts/animate_pixel_art.py input.png output
```

The script is intentionally generic. For higher-quality results, adjust motion regions, masks, timing, and animation channels for each source image.

## License

MIT

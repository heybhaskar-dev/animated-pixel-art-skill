#!/usr/bin/env python3
from pathlib import Path
import sys, math
from PIL import Image, ImageDraw

def composite(dst, src, xy):
    dst.alpha_composite(src, dest=xy)

def scale_crop(img, box, sx, sy):
    x0,y0,x1,y1 = box
    crop = img.crop(box)
    nw, nh = max(1, round(crop.width*sx)), max(1, round(crop.height*sy))
    out = crop.resize((nw,nh), Image.Resampling.NEAREST)
    return out, (round((x0+x1)/2-nw/2), y1-nh)

def build(src, out_dir, n=36, frame_ms=85):
    src = Path(src); out_dir = Path(out_dir)
    frames_dir = out_dir/"frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    base = Image.open(src).convert("RGBA")
    W,H = base.size
    box = (round(W*.25), round(H*.25), round(W*.80), round(H*.82))
    frames = []
    for i in range(n):
        t=i/n; a=math.tau*t
        canvas=Image.new("RGBA", base.size, (0,0,0,0))
        gx=round(math.sin(a*2)); gy=round(2*math.sin(a))
        composite(canvas, base, (gx,gy))
        breath=math.sin(a)
        focal,pos=scale_crop(base, box, 1-.006*breath, 1+.010*breath)
        composite(canvas, focal, (pos[0]+gx,pos[1]+gy))
        d=ImageDraw.Draw(canvas,"RGBA")
        for k,(x,y) in enumerate([(round(W*.42),round(H*.48)),(round(W*.60),round(H*.56)),(round(W*.70),round(H*.42))]):
            p=.5+.5*math.sin(a*2+k*1.9)
            if p>.75:
                alpha=round(210*(p-.75)/.25)
                d.rectangle((x-4,y,x+4,y+1),fill=(255,255,240,alpha))
                d.rectangle((x,y-4,x+1,y+4),fill=(255,255,240,alpha))
        frames.append(canvas)
        canvas.save(frames_dir/f"frame_{i+1:02d}.png")
    frames[0].save(out_dir/"animation.webp",save_all=True,append_images=frames[1:],duration=frame_ms,loop=0,lossless=True,method=6)
    print(f"Created {n} frames in {out_dir}")

if __name__=="__main__":
    if len(sys.argv)<3:
        raise SystemExit("Usage: animate_pixel_art.py input.png output_dir")
    build(sys.argv[1], sys.argv[2])

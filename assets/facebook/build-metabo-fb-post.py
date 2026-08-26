import base64, os, subprocess, pathlib

FD = "/root/.claude/skills/synced/canvas-design/canvas-fonts"
OUT = "/home/user/Jimzstudio/assets/facebook"
WORK = "/tmp/claude-0/-home-user-Jimzstudio/6c5953eb-bc85-5597-9463-fd1473ad76f9/scratchpad"

def font(name, family, weight="400", style="normal"):
    b = base64.b64encode(open(f"{FD}/{name}", "rb").read()).decode()
    return (f"@font-face{{font-family:'{family}';font-weight:{weight};font-style:{style};"
            f"src:url(data:font/ttf;base64,{b}) format('truetype');}}")

FONTS = "".join([
    font("Gloock-Regular.ttf", "Display"),
    font("InstrumentSerif-Italic.ttf", "Note", style="italic"),
    font("InstrumentSans-Regular.ttf", "Sans"),
    font("InstrumentSans-Bold.ttf", "Sans", weight="700"),
    font("GeistMono-Regular.ttf", "Mono"),
    font("Italiana-Regular.ttf", "Caps"),
])

# ---- brand palette ---------------------------------------------------------
PINK   = "#E3B9C5"   # pack front
PINK_D = "#D9A9B7"   # pink, one step down (rules on pink)
BROWN  = "#352626"   # pack panel
CREAM  = "#F3E6E9"   # type on brown
BLUSH  = "#EFD6DC"   # pack side / light accent

# ---- left-edge measuring scale (repeated marks) ----------------------------
ticks = []
y = 150
i = 0
while y < 660:
    major = (i % 5 == 0)
    w = 26 if major else 13
    o = ".26" if major else ".14"
    ticks.append(f'<rect x="0" y="{y}" width="{w}" height="1.4" fill="{BROWN}" opacity="{o}"/>')
    y += 17; i += 1
TICKS = "".join(ticks)

# ---- faint concentric arcs (cup rim, seen from above) ----------------------
arcs = "".join(
    f'<circle cx="960" cy="150" r="{r}" fill="none" stroke="{BROWN}" '
    f'stroke-width="1.2" opacity="{0.10 - k*0.008:.3f}"/>'
    for k, r in enumerate(range(120, 460, 26))
)

HTML = f"""<meta charset="utf-8"><style>
{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{background:{PINK}}}
html,body{{width:1080px;height:1350px}}
body{{background:{PINK};position:relative;overflow:hidden;
     -webkit-font-smoothing:antialiased;text-rendering:geometricPrecision}}

.tex{{position:absolute;inset:0;pointer-events:none}}

/* ---------- upper field: the hook ---------- */
.top{{position:absolute;left:84px;right:84px;top:0}}

.brow{{display:flex;justify-content:space-between;align-items:baseline;
      padding-top:72px}}
.brow .l{{font-family:Caps;font-size:23px;letter-spacing:.46em;color:{BROWN};
        opacity:.85;line-height:1}}
.brow .r{{font-family:Mono;font-size:15px;letter-spacing:.24em;color:{BROWN};
        opacity:.5;line-height:1}}
.hair{{height:1px;background:{BROWN};opacity:.22;margin-top:22px}}

.note{{font-family:Note;font-style:italic;font-size:38px;line-height:1.4;
      color:{BROWN};opacity:.6;margin-top:64px}}

.head{{font-family:Display;font-size:130px;line-height:.93;color:{BROWN};
      letter-spacing:-.028em;margin-top:40px}}
.head .b{{display:block;margin-left:-6px}}

.foot{{display:flex;align-items:center;gap:22px;margin-top:46px}}
.foot .rule{{height:1px;background:{BROWN};opacity:.26;flex:1}}
.foot .lab{{font-family:Mono;font-size:15px;letter-spacing:.26em;color:{BROWN};
          opacity:.58;white-space:nowrap;line-height:1}}

/* ---------- lower field: the payoff ---------- */
.panel{{position:absolute;left:0;right:0;top:690px;height:660px;
       background:{BROWN};border-radius:64px 64px 0 0;
       padding:50px 84px 0;display:flex;flex-direction:column}}

.plab{{font-family:Mono;font-size:15px;letter-spacing:.28em;color:{PINK};
      opacity:.6;line-height:1}}
.prule{{height:1px;background:{PINK};opacity:.18;margin-top:22px;flex:none}}

.ben{{display:flex;align-items:baseline;gap:32px;padding:20px 0 18px}}
.ben .n{{font-family:Mono;font-size:16px;letter-spacing:.14em;color:{PINK};
        opacity:.45;width:34px;flex:none}}
.ben .t{{font-family:Display;font-size:54px;line-height:1;color:{CREAM};
        letter-spacing:-.016em}}
.ben .s{{font-family:Sans;font-size:21px;letter-spacing:.02em;color:{PINK};
        opacity:.72;margin-top:9px;line-height:1.35}}

.base{{display:flex;align-items:flex-end;justify-content:space-between;
      margin-top:auto;padding:18px 0 56px}}
.mark .a{{font-family:Sans;font-size:19px;letter-spacing:.42em;color:{PINK};
        opacity:.75;line-height:1}}
.mark .b{{font-family:Display;font-size:37px;color:{CREAM};margin-top:11px;
        letter-spacing:-.01em;line-height:1}}
.mark .c{{font-family:Mono;font-size:14px;letter-spacing:.2em;color:{PINK};
        opacity:.48;margin-top:15px;line-height:1}}

/* ---------- flat pack rendering ---------- */
.pack{{width:142px;height:184px;background:{PINK};border-radius:6px;
      position:relative;flex:none;box-shadow:0 18px 42px rgba(0,0,0,.34);
      outline:1px solid rgba(243,230,233,.16);outline-offset:0}}
.pack .side{{position:absolute;left:0;top:0;bottom:0;width:15px;background:{BLUSH};
           border-radius:6px 0 0 6px}}
.pack .pan{{position:absolute;left:15px;top:0;bottom:0;width:49px;
          background:{BROWN};border-radius:0 16px 16px 0}}
.pack .vt{{position:absolute;left:15px;top:0;width:49px;height:184px;
         display:flex;align-items:center;justify-content:center;overflow:hidden}}
.pack .vt span{{font-family:Display;font-size:20px;color:{PINK};display:block;
              width:184px;text-align:center;transform:rotate(-90deg);
              line-height:1;letter-spacing:.005em}}
.pack .c1{{position:absolute;left:74px;top:44px;font-family:Display;
         font-size:19px;color:{BROWN};line-height:1}}
.pack .c2{{position:absolute;left:74px;top:70px;font-family:Sans;font-size:5px;
         letter-spacing:.05em;color:{BROWN};opacity:.68;line-height:1.7;width:56px}}
.pack .c3{{position:absolute;left:74px;bottom:26px;font-family:Sans;
         font-weight:700;font-size:17px;color:{BROWN};line-height:1}}
.pack .c4{{position:absolute;left:74px;bottom:14px;font-family:Sans;font-size:6px;
         letter-spacing:.14em;color:{BROWN};opacity:.75;line-height:1}}
</style>

<svg class="tex" width="1080" height="1350" viewBox="0 0 1080 1350">
  {arcs}
  {TICKS}
</svg>

<div class="top">
  <div class="brow"><div class="l">PRINSES</div><div class="r">METABO+ / 01</div></div>
  <div class="hair"></div>

  <div class="note">I didn&rsquo;t change my diet.<br>I didn&rsquo;t change my schedule.</div>

  <div class="head">I changed<span class="b">one cup.</span></div>

  <div class="foot"><div class="rule"></div>
    <div class="lab">ONE SACHET &middot; 30 SECONDS</div></div>
</div>

<div class="panel">
  <div class="plab">WHAT IT DOES</div>
  <div class="prule"></div>

  <div class="ben"><div class="n">01</div>
    <div><div class="t">Supports metabolism</div>
    <div class="s">Clean, steady energy &mdash; without the crash</div></div></div>
  <div class="prule"></div>

  <div class="ben"><div class="n">02</div>
    <div><div class="t">Easy digestion</div>
    <div class="s">Lighter mornings, less heaviness after meals</div></div></div>
  <div class="prule"></div>

  <div class="base">
    <div class="mark">
      <div class="a">METABO+</div>
      <div class="b">Coffee</div>
      <div class="c">15 SACHETS &middot; NET 210G</div>
    </div>
    <div class="pack">
      <div class="side"></div><div class="pan"></div>
      <div class="vt"><span>METABO+</span></div>
      <div class="c1">Coffee</div>
      <div class="c2">SUPPORTS METABOLISM<br>&amp; HEALTHY LIFESTYLE</div>
      <div class="c3">15</div><div class="c4">SACHETS</div>
    </div>
  </div>
</div>
"""
pathlib.Path(f"{WORK}/post.html").write_text(HTML)

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu",
                "--hide-scrollbars", "--force-device-scale-factor=2",
                "--window-size=1080,1620",
                f"--screenshot={WORK}/raw.png",
                f"file://{WORK}/post.html"], check=True,
               capture_output=True)

from PIL import Image
im = Image.open(f"{WORK}/raw.png").convert("RGB").crop((0, 0, 2160, 2700))
print("rendered", im.size)
im.resize((1080, 1350), Image.LANCZOS).save(f"{OUT}/metabo-fb-post-1080x1350.png",
                                            optimize=True)
px = im.load()
for probe, want in [((1080, 2698), "brown-bottom"), ((2158, 2698), "brown-corner")]:
    r, g, b = px[probe]
    assert (r, g, b) == (0x35, 0x26, 0x26), f"{want} leaked: {probe} -> {(r,g,b)}"
for x in range(1700, 2100, 20):
    assert sum(px[x, 2660]) < 200, f"pack overruns bottom margin at x={x}"
print("saved + panel reaches bottom + base row inside its margin")

# METABO+ Coffee — Facebook Carousel (1:1)

Four-slide carousel on the everyday benefits of METABO+ Coffee, built to match the
Prinses packaging (blush pink / espresso brown, high-contrast serif).

## Files

| File | Purpose |
| --- | --- |
| `carousel.html` | Source design — all 4 slides, 1080×1080 each |
| `render.js` | Playwright renderer → PNG at 2× |
| `exports/metabo-carousel-01…04.png` | Final assets, 2160×2160 (1:1, 2× for retina) |

## Re-rendering after an edit

```bash
cd design/metabo-carousel
NODE_PATH=$(npm root -g) node render.js
```

## Design system

| Token | Value | Use |
| --- | --- | --- |
| Blush | `#F5C9D8` | Panels, icon circles, CTA |
| Blush soft | `#FBE4EC` | Top wash on benefit slides |
| Cream | `#FBF4F1` | Slide background |
| Espresso | `#3B2A26` | Type, brand panel, slide 4 background |

Type: **Playfair Display** (headlines, product name) · **Jost** (eyebrows, body, labels).
Margins are 74 px on a 1080 grid — safely inside Facebook's crop on every placement.

## Slide sequence

1. **Hook** — product hero, "Your daily coffee, upgraded." + swipe cue
2. **Benefits 01–02** — Flatter, lighter tummy · Energy that lasts
3. **Benefits 03–04** — Weight management · A metabolism in motion
4. **Ritual + CTA** — dark slide, 3-step how-to, "Message us to order", disclaimer

---

## Ad copy

### Primary text (main post caption)

> Your morning cup is already a habit. Make it work for you. ☕️
>
> METABO+ Coffee is a rich, creamy daily coffee formulated to support your
> metabolism, your energy and your weight-management goals — one sachet, every
> morning, no extra effort.
>
> ✨ A flatter, lighter tummy
> ✨ Smooth energy without the 3 p.m. crash
> ✨ Easier portion control between meals
> ✨ Daily metabolism support
>
> 15 sachets per box — that's 15 days of showing up for yourself.
> 👉 Message us to order.
>
> *Food supplement. Not a substitute for a balanced diet and healthy lifestyle. Individual results may vary.*

### Per-card headline + description

| Card | Headline (≤40 char) | Description (≤20 char) |
| --- | --- | --- |
| 1 | Your Daily Coffee, Upgraded | Swipe to see why |
| 2 | Flatter Tummy, Real Energy | Benefits 01 & 02 |
| 3 | Manage Weight, Fire Metabolism | Benefits 03 & 04 |
| 4 | 15 Days. One Simple Ritual. | Order today |

**Call to action button:** Send Message (or Shop Now if linking to a store)

### Hashtags

`#MetaboPlusCoffee #PrinsesBeauty #CoffeeLovers #MetabolismSupport #HealthyLifestyle #WeightManagement #SlimmingCoffee #DailyRitual`

## Compliance note

Copy is written around *support* language (supports metabolism, helps manage
weight) rather than guaranteed outcomes, and every slide carries either
"Dietary Supplement" or the full disclaimer. Meta rejects ads implying
guaranteed weight loss or using before/after body imagery — avoid adding those.

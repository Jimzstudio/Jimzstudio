# METABO+ — Ad Image Prompt Pack

Image-generation prompts built around this approved copy:

> **Your coffee wakes you up. Ours has two more jobs. ☕**
>
> METABO+ supports a healthy metabolism and easy digestion — in the same cup you already drink every morning.
>
> **Lighter days. Steady energy. 30 seconds.**

---

## 1. Copy → layout map

| Slot | Text | Treatment |
|---|---|---|
| Headline | `Your coffee wakes you up.` / `Ours has two more jobs.` | Two lines, large, tight leading. Line 2 in the accent color. |
| Body | `METABO+ supports a healthy metabolism and easy digestion — in the same cup you already drink every morning.` | Small, 2–3 lines, max ~60% of frame width. |
| Kicker | `Lighter days. Steady energy. 30 seconds.` | All caps or small caps, letter-spaced, separated by a hairline rule or dot separators. |
| Icon | ☕ | Render as a **drawn cup mark**, not as an emoji glyph — image models mangle emoji. Or drop it from the frame and keep it only in the caption text. |

**Text-rendering rules for any model:** put each text block in the prompt inside straight quotes, spell it exactly, keep total on-image words under ~40, and use an em dash (—) not a hyphen. If the model garbles letters, generate the image *without* text and set the type in Canva/Figma over the negative space.

---

## 2. Primary prompt — hero product ad (4:5, feed)

```
Premium wellness product advertisement photograph. A warm ceramic mug of black
coffee on a light oak table, gentle steam curling upward, caught in soft morning
window light with long natural shadows. Beside the mug, a matte cream-and-deep-
espresso METABO+ stick sachet stands upright, one more sachet lying flat, label
clean and minimal. A few coffee beans and a folded linen napkin dressed loosely
in the foreground. Shallow depth of field, 85mm lens look, creamy bokeh, soft
diffused daylight from camera left, airy warm color grade, cream and caramel and
deep brown palette with a single sage-green accent. Generous empty space in the
upper third of the frame for text.

Text on image, rendered cleanly in a modern geometric sans-serif:
Top, large, two lines: "Your coffee wakes you up." / "Ours has two more jobs."
Below, small: "METABO+ supports a healthy metabolism and easy digestion — in the
same cup you already drink every morning."
Bottom, small caps, letter-spaced: "LIGHTER DAYS. STEADY ENERGY. 30 SECONDS."

Editorial DTC brand advertising, high-end e-commerce quality, photorealistic,
sharp product label, 4:5 vertical.
```

**Negative / avoid:** `cluttered background, harsh flash, cold blue light, plastic
texture, distorted or misspelled text, extra limbs, warped mug handle, watermark,
stock-photo smile, medical or clinical imagery, before-and-after body shots`

---

## 3. Variant A — lifestyle / UGC (9:16, Reels & Stories)

```
Authentic lifestyle phone-camera photo, vertical 9:16. A woman in her 30s in a
soft oatmeal knit sweater stirs a METABO+ stick sachet into a mug of coffee at a
sunlit kitchen counter, hands and mug in focus, face partly out of frame or
softly out of focus. Real morning kitchen: plants, a wooden board, a linen towel.
Warm golden window light, slight lens haze, natural skin texture, candid unposed
moment, subtle grain, no studio lighting. Clear empty space at the top of frame.

Text overlay, clean sans-serif, high contrast:
Top: "Your coffee wakes you up. Ours has two more jobs."
Bottom: "LIGHTER DAYS. STEADY ENERGY. 30 SECONDS."

UGC creator content aesthetic, believable and unpolished, photorealistic.
```

---

## 4. Variant B — "two more jobs" concept (1:1, static ad)

*This is the square version that was rendered (Nano Banana Pro, 1:1). Exact prompt used:*

```
Minimal conceptual advertising still life, square composition. A single ceramic
mug of black coffee shot top-down on a warm cream background, soft ring of crema,
gentle steam. Around the cup, three clean thin-stroke line-art icons in deep
espresso brown arranged in an evenly spaced row: a sunrise, a flame, a leaf. A
matte cream-and-espresso "METABO+" stick sachet lies at a slight angle at the
lower right, label clean and minimal. Bold negative space, soft studio lighting
with a warm morning feel, no clutter, modern Scandinavian brand design, palette
of cream #F4EBE0, caramel #C08A4A, espresso #3A2A20 with a single sage-green
accent.

Text rendered cleanly and correctly spelled in a modern geometric sans-serif:
Headline centered near the top, two lines, large and bold: "Your coffee wakes you
up." / "Ours has two more jobs."
Small body text below the headline, two lines: "METABO+ supports a healthy
metabolism and easy digestion - in the same cup you already drink every morning."
Footer line at the bottom, small caps and letter-spaced: "LIGHTER DAYS. STEADY
ENERGY. 30 SECONDS."

High-end DTC brand advertising, editorial e-commerce quality, photorealistic
product, crisp legible typography, sharp label. No misspelled or warped text, no
watermarks, no scales, no tape measures, no before-and-after body shots, no pills
or capsules, no lab coats or medical imagery.
```

Icon meanings for the three marks: sunrise = wake up, flame = metabolism, leaf =
easy digestion. Shorter alternative for the body line if the model crowds the
frame: `"Metabolism. Digestion. Same cup."`

---

## 5. Variant C — 30-second proof shot (4:5)

```
Close-up macro advertising photo, 4:5. A METABO+ stick sachet being torn open
above a full mug of hot coffee, fine powder mid-pour catching the light, steam
rising, motion frozen at 1/1000s. Dark espresso surface with a soft ring of
crema. Dramatic warm side light against a deep brown backdrop, rich contrast,
glossy highlights on the sachet foil. Space at the top for a headline.

Text: "Ours has two more jobs." large at top; "30 SECONDS. SAME CUP." small at
bottom, letter-spaced.

Luxury food-and-beverage advertising photography, macro detail, photorealistic.
```

---

## 6. Brand direction (keep consistent across the set)

- **Palette:** cream `#F4EBE0`, caramel `#C08A4A`, espresso `#3A2A20`, sage accent `#8A9A7B`.
- **Type:** geometric sans (Poppins / Söhne / Neue Haas Grotesk feel). Headline bold, body regular, kicker medium + ~8% letter-spacing.
- **Light:** always warm morning daylight — never cold, never clinical.
- **Mood words to reuse:** *warm, calm, unhurried, clean, editorial, believable.*

## 7. Compliance guardrails

This is a supplement, so the imagery must stay in "supports" territory:

- No weight-loss visuals: no scales, tape measures, before/after bodies, waist shots.
- No medical cues: no lab coats, pills, capsules, doctors, stethoscopes, charts.
- Keep claim wording exactly as approved — "supports a healthy metabolism and easy digestion." Don't let a model rewrite it to "burns fat" or "detox."
- If a rendered image adds text you didn't ask for, discard it rather than editing it — invented claims are the risk.

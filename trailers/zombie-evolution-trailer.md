# "PATIENT ZERO" — 30-Second Zombie Evolution Trailer

Production package for a 30-second cinematic horror trailer in which an ordinary
zombie mutates into a full zombie monster. Everything below is ready to run
through the Higgsfield generation tools as-is.

- **Runtime:** 30s — 6 shots x 5s
- **Aspect ratio:** 16:9 (cinematic). For TikTok / Reels / Shorts, regenerate at `9:16` or run `reframe` on the finished cut.
- **Resolution:** 1080p
- **Audio:** native audio on (the model scores each shot: breathing, bone crunch, roar)

---

## Story arc

| Beat | Time | Shot | Purpose |
|---|---|---|---|
| 1 | 0:00–0:05 | Dead city, one infected under a streetlight | Establish the world. Quiet. |
| 2 | 0:05–0:10 | Face close-up, it notices the camera and screams | Meet the threat. First scare. |
| 3 | 0:10–0:15 | Survivors in a parking garage, horde swarms | Raise the stakes. Human cost. |
| 4 | 0:15–0:20 | **The mutation** — spine cracks, body swells | The turn. This is the promise of the title. |
| 5 | 0:20–0:25 | Full monster revealed, towering over the squad | The payoff. Scale reveal. |
| 6 | 0:25–0:30 | Monster charges the camera, smash to black + title | The button. Leave them wanting more. |

The edit accelerates: shots 1–2 are slow pushes, 3–4 go handheld and chaotic,
5 is a locked-off low angle for scale, 6 is pure impact.

---

## Look & continuity bible

Repeat these lines inside every shot prompt so the six clips grade and cut together:

> Desaturated teal-and-sickly-amber color grade, crushed blacks, heavy 35mm film
> grain, anamorphic lens flares, volumetric fog, shallow depth of field,
> handheld weight, practical flashlight and sodium-streetlight sources only.

**Creature continuity — the zombie (shots 1–4):** adult male, gaunt, grey-green
mottled skin, blackened veins spidering up the neck and jaw, milky white eyes
with no iris, torn hospital scrubs stained rust-brown, exposed collarbone,
jaw hanging slightly loose.

**Creature continuity — the monster (shots 4–6):** the same creature at ~3.5m
tall, hunched, elongated limbs, spine erupted into bony blade-like spurs,
exposed sinew and glistening muscle over a splintered ribcage, arms too long
for the body, jaw split vertically into four mandibles, the same milky eyes
sunk deep in the skull, shreds of the rust-brown scrubs still hanging off it.

---

## Recommended pipeline

1. **Lock the creature first.** Generate one hero still of the zombie and one of
   the monster (`generate_image`, model `nano_banana_pro` or `soul_2`, 16:9).
2. **Pass those stills as references** into every video shot via
   `medias: [{role: "image_references", value: "<image job_id>"}]` — this is what
   keeps the same creature across all six shots instead of six different zombies.
3. **Fire the six shots in parallel** with `generate_video_batch` (one request per
   shot, indices 1–6), then `jobs_wait`, then one `show_generation_by_ids`.
4. **Assemble** in order 1→6. Cut on the impact frames, not on the motion.

**Model:** `seedance_2_5` — `duration: 5`, `resolution: "1080p"`,
`aspect_ratio: "16:9"`, `generate_audio: true`.

**Alternate:** `cinematic_studio_3_0` with `genre: "horror"` for a more graded,
film-stock look, or `kling3_0` (`mode: "pro"`) if you want stronger creature
physics on the mutation shot.

**Cost:** ~32.5 credits per 5s shot at these settings → **~195 credits for the
full 30 seconds**, plus ~2 stills for the creature references.

---

## Shot prompts (copy-paste ready)

### Shot 1 — 0:00–0:05 · The dead world
> Cinematic horror trailer shot. A fog-choked abandoned city street at dawn,
> overturned cars, drifting ash, traffic lights blinking over an empty
> intersection. A lone infected figure stands twitching beneath a flickering
> sodium streetlight, head hanging at a broken angle, arms limp. Slow dolly
> push-in from behind. Total silence except wind and a distant dripping.
> Desaturated teal-and-sickly-amber grade, crushed blacks, heavy 35mm grain,
> anamorphic flare, volumetric fog, shallow depth of field.

### Shot 2 — 0:05–0:10 · It sees you
> Extreme close-up on the infected man's face: grey-green mottled skin,
> blackened veins spidering up his jaw, milky white eyes with no iris, torn
> rust-stained hospital scrubs. He is perfectly still — then his head snaps
> toward the lens and he screams, jaw unhinging, spittle catching the light.
> Camera jolts back a few inches. Desaturated teal-and-amber grade, crushed
> blacks, heavy grain, shallow depth of field, flickering practical light.

### Shot 3 — 0:10–0:15 · The survivors
> Handheld shaky camera. Four survivors in tactical gear sweep a flooded
> underground parking garage, flashlight beams cutting through thick fog and
> catching floating dust. One raises a rifle as dozens of infected pour from the
> darkness between the pillars, sprinting. Muzzle flash strobes the walls.
> Chaotic body-cam energy, motion blur, desaturated teal grade, crushed blacks,
> heavy grain, volumetric light shafts.

### Shot 4 — 0:15–0:20 · The evolution
> The infected man convulses on the concrete floor as the survivors' flashlights
> pin him. His spine arches violently and cracks upward, bony blade-like spurs
> erupting through the skin of his back. Muscle mass swells and tears across his
> shoulders, his arms stretch too long, his ribcage splinters outward, and his
> jaw splits vertically into four mandibles. Steam rises off the transforming
> body. Slow-motion push-in, wet practical sound of bone and sinew. Desaturated
> teal-and-amber grade, crushed blacks, heavy grain, backlit fog.

### Shot 5 — 0:20–0:25 · The monster
> Low-angle wide shot looking up. A three-and-a-half-meter zombie monster rises
> to full height in the parking garage — hunched, elongated limbs, spine erupted
> into bony spurs, exposed glistening sinew over a splintered ribcage, jaw split
> into four mandibles, milky sunken eyes, shreds of rust-brown scrubs hanging
> off it. Four tiny flashlight beams shake across its chest as it roars, and
> dust falls from the ceiling. Locked-off camera, epic scale, desaturated
> teal-and-amber grade, crushed blacks, heavy grain, volumetric light.

### Shot 6 — 0:25–0:30 · Impact
> The zombie monster charges directly at the camera through the parking garage,
> smashing a concrete support pillar apart in an explosion of dust and rebar,
> mandibles flaring open, arms swinging. The camera is knocked to the ground and
> everything cuts to black. Violent handheld motion, debris flying past the
> lens, hard flashlight backlight, desaturated teal grade, crushed blacks, heavy
> grain, anamorphic flare.

---

## Title card

Over the black at 0:28, hold two seconds:

```
PATIENT ZERO
it doesn't stop at dead
```

Build it as a still (`generate_image`, 16:9, black field, distressed condensed
sans in bone-white with a faint blood-red underglow) and tail it onto the cut,
or add it in your editor.

## Sound

Native model audio covers the diegetic layer (breath, screams, gunfire, bone).
For the trailer bed, add a low sub-drone rising across shots 1–4, a hard
silence beat right before shot 5's roar, and a single braaam on the shot 6
impact. `generate_audio` (Higgsfield) or `audio_music_generate` (Magnific) can
score this to the 30-second timing.

import { readFileSync, writeFileSync } from 'node:fs';

const scene = readFileSync('scene.svg.frag', 'utf8').trimEnd();
const VB = '10 88 620 412';

const C = {
  paper: '#F2E8D8', paperLite: '#F7F1E6', espresso: '#2A1A12',
  bean: '#3B2418', crema: '#C8783A', tissue: '#E0906E',
  grease: '#6E5C2F', jade: '#2E9270',
};

const slab = "'Alfa Slab One', Rockwell, Georgia, serif";
const sans = "'Work Sans', 'Helvetica Neue', Arial, sans-serif";

const head = (extra = '') => `<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Work+Sans:wght@400;500;600${extra}&display=swap">
  <style>
    body { margin: 0; background: ${C.paper}; -webkit-font-smoothing: antialiased; }
    a { color: ${C.crema}; text-decoration: none; }
    a:hover { color: #8A5024; }
  </style>
</helmet>`;

const foot = `</x-dc>
</body>
</html>
`;

const sceneSvg = (extraStyle = '') => `<svg viewBox="${VB}" width="100%" height="100%" preserveAspectRatio="xMidYMid meet" style="display: block;${extraStyle}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A coffee bean with a scrub brush cleaning a greasy stretch of gut until it is bright and clean">
${scene}
</svg>`;

const moon = (size) => `<svg width="${size}" height="${size}" viewBox="0 0 48 48" style="display: block; flex: none;" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <circle cx="22" cy="26" r="15" fill="${C.espresso}"></circle>
    <circle cx="31" cy="18" r="14" fill="${C.paper}"></circle>
    <path d="M 41 8 l 3 7 l 7 3 l -7 3 l -3 7 l -3 -7 l -7 -3 l 7 -3 z" transform="translate(-4,-4) scale(0.8)" fill="${C.jade}"></path>
  </svg>`;

const pill = (text, fs) => `<div style="display: inline-flex; align-items: center; background: ${C.espresso}; color: ${C.paper}; border-radius: 999px; padding: ${Math.round(fs * 0.6)}px ${Math.round(fs * 1.2)}px; font-size: ${fs}px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase;">${text}</div>`;

/* ---------------- Main — Instagram feed 1080 x 1350 ---------------- */
writeFileSync('Main.dc.html', `${head()}
<div style="width: 1080px; height: 1350px; background: ${C.paper}; box-sizing: border-box; padding: 64px 72px 0; display: flex; flex-direction: column; font-family: ${sans}; color: ${C.espresso};">

  <div style="display: flex; align-items: center; justify-content: space-between; gap: 24px;">
    ${pill('After that oily meal', 24)}
    ${moon(64)}
  </div>

  <div style="margin-top: 36px; font-family: ${slab}; font-size: 100px; line-height: 0.98; text-transform: uppercase; letter-spacing: -0.005em;">
    <div>Your gut&#39;s</div>
    <div style="color: ${C.crema};">Clean-up</div>
    <div style="color: ${C.crema};">Crew.</div>
  </div>

  <div style="flex: 1 1 auto; min-height: 0; display: flex; align-items: center; margin: 8px -28px 0;">
    ${sceneSvg()}
  </div>

  <p style="margin: 4px 0 34px; font-size: 30px; line-height: 1.45; max-width: 880px; text-wrap: pretty;">[PRODUCT] scrubs down that heavy, greasy after-dinner feeling &mdash; so your stomach settles and the night comes easy.</p>

  <div style="margin: 0 -72px; padding: 30px 72px; background: ${C.espresso}; color: ${C.paper}; display: flex; align-items: center; justify-content: space-between; gap: 24px; font-size: 24px; font-weight: 600; letter-spacing: 0.16em; text-transform: uppercase;">
    <span>Easy digestion &middot; Easy sleep</span>
    <span style="color: ${C.crema};">[BRAND]</span>
  </div>

</div>
${foot}`);

/* ---------------- Facebook — link/feed 1200 x 630 ---------------- */
writeFileSync('Facebook.dc.html', `${head()}
<div style="width: 1200px; height: 630px; background: ${C.paper}; box-sizing: border-box; display: flex; font-family: ${sans}; color: ${C.espresso};">

  <div style="flex: 0 0 596px; box-sizing: border-box; padding: 48px 24px 48px 64px; display: flex; flex-direction: column; justify-content: center; gap: 24px;">
    ${pill('After that oily meal', 17)}
    <div style="font-family: ${slab}; font-size: 52px; line-height: 1; text-transform: uppercase; letter-spacing: -0.005em;">
      <div>Your gut&#39;s</div>
      <div style="color: ${C.crema};">Clean-up</div>
      <div style="color: ${C.crema};">Crew.</div>
    </div>
    <p style="margin: 0; font-size: 21px; line-height: 1.5; max-width: 440px; text-wrap: pretty;">[PRODUCT] scrubs down the heavy, greasy after-dinner feeling &mdash; so your stomach settles and the night comes easy.</p>
    <div style="display: flex; align-items: center; gap: 20px; flex-wrap: wrap;">
      <div style="background: ${C.espresso}; color: ${C.paper}; border-radius: 999px; padding: 16px 32px; font-size: 19px; font-weight: 600; letter-spacing: 0.06em;">Shop [PRODUCT]</div>
      <div style="font-size: 16px; font-weight: 500; letter-spacing: 0.14em; text-transform: uppercase; color: ${C.grease};">[YOUR OFFER]</div>
    </div>
  </div>

  <div style="flex: 1 1 auto; min-width: 0; box-sizing: border-box; padding: 28px 40px 28px 0; display: flex; align-items: center;">
    ${sceneSvg()}
  </div>

</div>
${foot}`);

/* ---------------- Story — Instagram/Facebook story 1080 x 1920 ---------------- */
writeFileSync('Story.dc.html', `${head()}
<div style="width: 1080px; height: 1920px; background: ${C.paper}; box-sizing: border-box; padding: 264px 72px 296px; display: flex; flex-direction: column; font-family: ${sans}; color: ${C.espresso};">

  <div style="display: flex; align-items: center; justify-content: space-between; gap: 24px;">
    ${pill('After that oily meal', 26)}
    ${moon(72)}
  </div>

  <div style="margin-top: 44px; font-family: ${slab}; font-size: 144px; line-height: 0.92; text-transform: uppercase; letter-spacing: -0.01em;">
    <div>Scrub</div>
    <div>the</div>
    <div style="color: ${C.crema};">grease.</div>
  </div>

  <div style="flex: 1 1 auto; min-height: 0; display: flex; align-items: center; margin: 0 -28px;">
    ${sceneSvg()}
  </div>

  <p style="margin: 0 0 40px; font-size: 34px; line-height: 1.4; max-width: 860px; text-wrap: pretty;">One bean, taken after dinner. [PRODUCT] settles the heavy feeling so the night comes easy.</p>

  <div style="display: flex; align-items: center; justify-content: space-between; gap: 24px;">
    <span style="display: flex; flex-direction: column; gap: 10px; font-size: 25px; font-weight: 600; letter-spacing: 0.16em; text-transform: uppercase;">
      <span style="color: ${C.crema};">[BRAND]</span>
      <span>Easy digestion<br>Easy sleep</span>
    </span>
    <span style="background: ${C.espresso}; color: ${C.paper}; border-radius: 999px; padding: 22px 40px; font-size: 26px; font-weight: 600; letter-spacing: 0.08em;">Tap to shop</span>
  </div>

</div>
${foot}`);
console.log('wrote Main / Facebook / Story');

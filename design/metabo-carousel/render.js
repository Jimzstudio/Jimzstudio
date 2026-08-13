const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const dir = __dirname;
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1080, height: 1080 },
    deviceScaleFactor: 2,
  });
  await page.goto('file://' + path.join(dir, 'carousel.html'));
  await page.waitForTimeout(1200);

  for (let i = 1; i <= 4; i++) {
    const el = await page.$('#slide-' + i);
    const out = path.join(dir, 'exports', `metabo-carousel-0${i}.png`);
    await el.screenshot({ path: out });
    console.log('rendered', out);
  }
  await browser.close();
})();

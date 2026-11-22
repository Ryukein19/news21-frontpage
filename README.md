[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# Saturday 21 November 2026 — The World's News in One Picture

An entry for the [make.fun bounty "Sum up the world's news of Saturday 21 November 2026 in one image"](https://make.fun/bounty/news-image-20261121): a single front page with 36 stories from Saturday 21 November 2026, across 7 regions.

The lead is the day's biggest story: **Iran strikes US bases in Bahrain** (1.5× wider, biggest headline and drawing), with COP31 in overtime and the burning Russian ship Sparta II as leads #2 and #3. The number strip is canonical (2 bases · 11 dead in the Mexico raid · 6.8 Peru quake · 60 wounded in Kryvyi Rih · −5.3% Nasdaq · 36 missing in the Java fire). Drawn stories 4–13 are the "El Chapo Isidro" capture, the Kryvyi Rih triple-tap, three Houthi missiles stopped over Riyadh, the Peru quake, the US stocks correction, the EU–Indonesia trade deal, the UK–EU signing, the candy-factory fire near Jakarta, the dengue mosquitoes in Brazil, and the AI-assisted Riemann proof claim. The ALSO list adds 23 more verified stories, and a "THE DAY IN UTC" strip runs the day hour by hour (00:09 Peru quake · 02:00 Mexico raid · 06:45 Sparta II hit · 10:34 Finnish airspace · 16:00 ICE in Seattle · night Bahrain strikes). Every story carries a status badge (OFFICIAL / CONFIRMED / REPORTED, colour-coded; the ALSO list uses colour-coded numbers with a legend). The dark world map pins only the 13 drawn stories. Every story is attributed to its source.

**Verification:** every story on the page was confirmed by at least two independent reputable outlets, with its date checked against Saturday 21 November 2026. Friday items that other round-ups list as Saturday news are excluded and named in the DATE CHECK box: Kyiv bridges, Cyclone Akvan, the Anthropic IPO debut, the Senate Iran vote, the ICJ Myanmar ruling, GTA VI's $3.79bn sales, the PIF Tower damage, the Bayer Roundup approval, the Virginia measles death, the Daraxonrasib results, Mamdani's Rikers plan, the Poland missile landings (reactions Saturday), and the COP31 approval vote (Sunday 06:00 GMT). Friday-night events — the Kryvyi Rih strike and the Mexico raid — are presented with explicit Friday-night dating; the tolls are Saturday's news. Iran's claim that it hit two US Patriot radars is marked unconfirmed; the Riemann proof is presented as a claim, not a confirmed proof.

## How it works

`frontpage.html` is the source the image was rendered from (the dark world map with the 13 pins is drawn inline as SVG). `entry.png` is the finished 1024×1024 front page (under 1 MiB). `main.py` (Python 3, standard library only, no network) copies `entry.png` to the output directory, checking first that it is a PNG, 1024×1024, and under the 1 MiB limit:

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

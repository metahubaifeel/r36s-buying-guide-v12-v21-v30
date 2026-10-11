# R36S V12 vs V21 vs V30 — which revision, which colours, and who should not buy one

**English** · **[中文](README.zh-CN.md)**

> **Short answer.** V12, V21 and V30 are **supplier board revisions of the same handheld**, not performance tiers — same RK3326 platform, same shell, same controls. What actually differs is **which finishes you can order** and **whether built-in WiFi is offered**:
>
> | Revision | Finishes | Built-in WiFi |
> |---|---|---|
> | **V12** | 13 finishes | not offered — use the USB dongle |
> | **V21** | 4 finishes: Transparent Purple, Transparent Black, White, Yellow | optional |
> | **V30** | 4 finishes: Transparent Purple, Transparent Black, White, Transparent Pink | optional |
>
> **A shell colour is not proof of the board inside**, and neither is a marketplace listing that says "V12". The revision is printed on the board itself: our sample boards read `R36S-V21 2024-12-18` and `R36S-V30 2025-11-18`.
>
> **Who should not buy one:** anyone who wants PSP / N64 / DS / Saturn / PS2 / GameCube to run well, anyone who expects phone-style standby, anyone who needs guaranteed save files, anyone who wants games and a memory card in the box, and anyone who wants a certified non-clone guarantee. That list is longer than the sales copy you will read elsewhere, and it is the point of this page — [jump to it](#who-should-not-buy-an-r36s).

---

## The questions buyers actually ask

Verbatim messages from Chinese handheld QQ groups, taken from a read-only export of 22,869 unique group messages. Group name only — the export cannot reliably attribute a message to a person.

| Group | What was said (verbatim, Chinese) |
|---|---|
| 安伯尼克掌机交流群 | `请问现在477v掌机8+128，二手，1250块钱值不值` |
| 玩机社5群 | `请问一下，有没有500以下的开源掌机推荐啊，` |
| 玩机社5群 | `500元性价比最高的主机或掌机有什么🤔` |
| 开源掌机中文社区⑤群 | `500块钱预算买一个竖版掌机，有推荐的吗` |
| r36s（开源掌机）交流1群 | `群友们，这r36s有踩坑吗` |
| r36s（开源掌机）交流1群 | `我前几天刚买的R36MAX2，第一次接触掌机，不知道买的好不好，想找个群了解了解，问问性价比怎么样，还有好多不明白` |
| r36s（开源掌机）交流1群 | `以前也是看的R36S这款，今年再看的时候，看到了这款R36max2，屏幕大一点了，贵了100，就买了现在这个` |

**About this data.** No date range, no per-message timestamps, no speaker attribution, and at least three related groups were captured only by name and announcement. Quoted as extracted; nothing paraphrased.

### And the reputation is genuinely two-sided

We sell this handheld, so we are going to quote the negative ones too.

| | Verbatim (Chinese) | Group |
|---|---|---|
| Positive | `听我的，寨机就买个r36s足够了` | r36s（开源掌机）交流1群 |
| Positive | `gba的话，r36s就够了` | r36s（开源掌机）交流1群 |
| Negative | `r36s现在一堆推广` | r36s（开源掌机）交流1群 |
| Negative | `B站里面全是R36S的玩机技巧，这款的全是广告宣传` | r36s（开源掌机）交流1群 |
| Negative | `r36s感觉太多了 怕翻车` | r36s（开源掌机）交流1群 |
| Negative | `r36s掉存档了` — two separate messages | 开源掌机中文社区⑤群 |
| Negative | `不过果然r36s正版v12接上wifi后就有噪音了` | R36S掌机爱好者 |

Both halves are true. It is a cheap, repairable, well-documented 4:3 handheld — *and* it is a device with an enormous amount of affiliate content around it, reports of lost save files, and a speaker hum on WiFi builds. Each of those is addressed below, including the ones we cannot explain.

---

## Why the version confusion exists

Three reasons, and none of them are the buyer's fault.

1. **The revision names come from the board, not from the shop or from a marketing plan.** They are supplier board revisions. The name is silkscreened on the PCB, next to a date: our own sample boards read `R36S-V21` / `2024-12-18` and `R36S-V30` / `2025-11-18`.
2. **Sellers list the colour, buyers read the revision into it — wrongly.** The same finish is built on more than one board: Transparent Purple, Transparent Black and White exist on all three revisions. So "I bought the purple one" tells you nothing certain about the board.
3. **The revision matters for one practical reason: firmware and the `.dtb`.** Community firmware images ship with multiple device trees, and picking the one that matches your board is the step that goes wrong. That is why the revision number is all over the community conversation — it is a *software pairing* question far more often than a hardware-quality one.

---

## What actually differs

### The finish matrix, copied from our own catalogue

![R36S finishes x board revisions](docs/03-finish-revision-matrix.png)

*Generated directly from the shop's own catalogue data (`storefront/src/lib/catalog.ts`): 14 finishes, 3 revisions, and which combinations can be ordered. Not a render and not a guess.*

| | V12 | V21 | V30 |
|---|---|---|---|
| **Finishes** | 13 | 4 | 4 |
| **Transparent Purple** | yes | yes | yes |
| **Transparent Black** | yes | yes | yes |
| **White** | yes | yes | yes |
| **Yellow** | yes | yes | — |
| **Transparent Pink** | — | — | yes |
| **Bright Pink** | yes | — | — |
| **Soft Blue** | yes | — | — |
| **Solid Purple** | yes | — | — |
| **Transparent Green** | yes | — | — |
| **Transparent Red** | yes | — | — |
| **Transparent Lake Blue** | yes | — | — |
| **Solid Red** | yes | — | — |
| **Transparent Orange** | yes | — | — |
| **Transparent Blue** | yes | — | — |
| **Built-in WiFi** | not offered | optional | optional |
| **USB WiFi dongle + adapter** | yes | yes | yes |

**If you want an unusual colour, you want a V12.** That is the whole reason V12 still exists in the line-up: 13 finishes against the newer boards' four.

**If you want built-in WiFi, you want V21 or V30.** And read the disclosure before you decide you want it:

- WiFi builds have a **faint speaker hum**. Our own product page states this before purchase, and the group message quoted above is somebody noticing the same thing on their own unit.
- **Disabling USB or network settings may require reflashing to get WiFi back.** That is not a scare line; it is a recovery limitation we would rather tell you about than have you discover.
- A **USB WiFi dongle + adapter** is available for any revision, including V12, which sidesteps both.

> ⚠️ Unresolved: the group message says a **V12** developed WiFi noise. In our own catalogue, built-in WiFi is not offered on V12 at all — so that unit was either using a dongle, or came from a batch we do not source. We are not going to explain it away; we simply do not know which.

### What does *not* differ

This matters more than the version table, because it is what people actually want to know:

- **Same SoC family.** The boards in our photographs carry a **Rockchip RK3326**, on both the V21 and the V30 sample.
- **Same memory class.** Our own photo of the vendor System Info screen on a real unit reports **`Total: 895 MB`** — a machine sold as 1 GB, reporting 895 MB of total memory, with the remainder reserved by the vendor kernel. ⚠️ We did not verify how that reservation is accounted for; we report the number we photographed.
- **Same form factor.** Portrait 3.5-inch 4:3 screen, D-pad, four face buttons, **two analog sticks**, four shoulder buttons, two card slots.
- **No revision is a performance upgrade.** If a listing implies V30 is "faster", it is not a difference you can buy. The revisions differ in availability, colour range and WiFi option.

![V21 sample board, silkscreen reading R36S-V21 2024-12-18](docs/01-v21-board-silkscreen.jpg)

*A V21 sample board from our stock: silkscreen `R36S-V21`, `2024-12-18`. Supplier sample, shown unaltered.*

![V30 sample board, silkscreen reading R36S-V30 2025-11-18](docs/02-v30-board-silkscreen.jpg)

*A V30 sample board from our stock: silkscreen `R36S-V30`, `2025-11-18`. Same layout family, same SoC marking. Supplier sample, shown unaltered.*

![Vendor System Info screen on a real unit: total memory 895 MB](docs/04-system-info-memory.jpg)

*The vendor's own System Info screen (`R36S System Info by Jason`) on a real unit: `Total: 895 MB`, `Used: 318 MB`, and a 119.88 GB card showing 110.79 GB used and 7.52 GB free. This is a photograph of a screen, not a specification sheet — and it is the single most useful number in this article, because it tells you what the machine is actually like rather than what a listing claims.*

---

## How to choose

![Should you buy an R36S?](docs/05-should-you-buy-flowchart.png)

1. **Decide the revision by what you cannot live without.** Built-in WiFi → V21 or V30. A specific unusual colour → V12. Neither matters to you → choose by finish and price, because the platform is the same.
2. **Decide whether you want WiFi at all.** It brings a faint speaker hum and a recovery limitation. If you only want to play, skipping it removes a whole category of annoyance.
3. **Choose the finish you will still like in a year.** Transparent shells show dust; solid shells hide the internals that make this thing fun to own. That is taste, not performance.
4. **Decide where the games come from, before you pay.** A bare handheld ships with no games, no card and no charging cable. If "it just works out of the box with games on it" is your requirement, a bare device is the wrong purchase — and so is this shop.
5. **Write the configuration into the order.** Board revision, finish, WiFi or not, dongle or not — in writing, before payment. "Left" and "V30-ish" are not order specifications.

---

## How to verify what you actually received

1. **Read the board.** With the back shell off, the silkscreen gives revision and date: `R36S-V12`, `R36S-V21`, `R36S-V30`, followed by a date code. This is the only method we treat as conclusive, and it is why we publish board photographs.
2. **Check the WiFi option.** If built-in WiFi was part of the deal, confirm it exists on the unit you were sent. Per our own catalogue, built-in WiFi is a V21/V30 option.
3. **Read the system information screen.** Our own units carry a vendor page titled `R36S System Info by Jason`, with `Display`, `Memory`, `SD Card 1/2` and `System` blocks. Useful — and note the caveat below.
4. **Do not trust the colour.** Purple, black and white exist on all three revisions.
5. **Photograph what arrived** before you open anything, and keep the packing. It makes any conversation trivially easy.

> ⚠️ 未实测 / honest limitation on the software route: a running system reports the **device tree it booted**, not necessarily the board it is sitting on. If a previous owner flashed a V21 `.dtb` onto a V30 board, a software check will happily report V21. We therefore do **not** publish a "type this command to learn your revision" recipe as a verified method — the silkscreen is the method we stand behind.
>
> ⚠️ Also unverified by us: our System Info photograph comes from a unit in our own stock, and the `ArkOS Version:` row on that screen is blank on that build. We are not going to fill in a version number we did not read.

---

## Who should *not* buy an R36S

This section costs us money. It is also the only section most buyers actually need.

**Do not buy it if you want to play PSP, N64, DS, Saturn, PS2, Dreamcast or GameCube.** RK3326 is a 4-core Cortex-A35 class chip with a Mali-G31-class GPU and about 1 GB of RAM. 8-bit and 16-bit systems are what this machine is for; PS1 generally runs well on this chip class; anything above that is a compromise you will notice in the first hour. We publish **no frame-rate benchmarks** — treat that as a boundary we are drawing, not a measurement we took. The community reaches the same conclusion in its own words:

- `专用的可以特别优化，R36那种充其量只是整合的一堆模拟器` — *"a dedicated machine can be specially optimised; an R36 is at best a pile of emulators bundled together."* (r36s（开源掌机）交流1群)
- `我这个为啥psp模拟器没有呢` — *"why doesn't mine have a PSP emulator?"* (r36s（开源掌机）交流1群)
- `你猜猜为什么土星模拟器不行` — *"guess why the Saturn emulator doesn't work."* (安伯尼克掌机交流群)

**Do not buy it if you want a device that behaves like a phone.** `开源是没待机` — there is no true standby. You shut it down, or you find it flat.

**Do not buy it if losing a save file would ruin your week.** `r36s掉存档了` appears twice in one group's messages, and one of the two appends `正常` — "normal" — as if it were unremarkable. That is the community's own framing, not ours. We have **no verified root cause** to give you.

> ⚠️ 未实测：we have not reproduced a lost save, so we cannot tell you the cause. What we can tell you is what reduces exposure: save in-game *and* use a save state, exit games through the emulator's own quit path rather than switching the unit off, never remove the card while the system is running, and keep a copy of your saves on a computer. None of that is a guarantee.

**Do not buy it if you need a memory card, a charging cable or games in the box.** Our listings are bare by design: no card, no ROM library, no charging cable. No copyrighted ROMs are sold, here or anywhere legitimate.

**Do not buy it if "is it a genuine, non-clone unit?" is a question you need answered with a certificate.** Our position is stated on our own product page: board photographs show what is visible on *those samples*, and **a photo of one sample does not certify every shipped batch, and we do not make a clone claim.** If a seller tells you a photo proves authenticity, they are overselling it.

**Do not buy it if the lowest possible price is your only criterion.** In the domestic Chinese market these have been seen around ¥260 with a card bundled (`拼多多那时候买的游戏机，带内存卡也才260多`, R36S掌机爱好者), second-hand units move for less, and the cheapest US listing we recorded in our own October 2026 market research was **$52** — below our own starting price, though we did not verify what that listing actually includes. If price is the whole decision, shop those instead: that is a legitimate choice, and this shop is not the answer to it. What a shop like ours charges for is a stated configuration in writing, disclosed tradeoffs, a bare unit with no bundled ROMs, and a 7-day change-of-mind return with direct support. If that is not worth anything to you, it is not worth anything to you.

**Do not buy it if you want an OLED screen, HDMI out, a bigger panel, or modern 3D.** None of that is what this is. The group's own line about the market above it, from 安伯尼克掌机交流群: `其他掌机都比去年更贵` — *the other handhelds all got more expensive than last year* — and if that is what you want, that is what you should buy.

---

## Price: what the numbers actually are

| Number | What it is | Where it comes from |
|---|---|---|
| **$69** | Starting price of a **bare V12** handheld in this shop | Our own published entry price for a bare V12 |
| Delivery total in writing | Board, add-ons, tracked shipping and import-charge responsibility | Our own order terms — the $69 is not a delivered price |
| $79.99 | R36S **with a 128 GB card and games** on a public US marketplace listing | Recorded in our own October 2026 market research |
| $52.00 | Cheapest R36S listing we recorded, transparent purple, no bundle stated | Same research — ⚠️ we did not verify what that listing includes |
| ~¥260 | Card-bundled unit, domestic Chinese marketplace | QQ group message (R36S掌机爱好者) — ⚠️ community report, unverified by us |
| 1250元 | A second-hand 8+128 Android handheld, i.e. a *different, higher class* of machine | QQ group message (安伯尼克掌机交流群) — included because "is it worth it" questions are usually about that class, not about an R36S |

**Read that table honestly and it says: a bare R36S at $69 is not automatically the cheapest R36S.** We recorded a $52 listing and a $79.99 card-and-games bundle in the same market, and domestically these go for far less. What you are choosing is a bare device with a stated configuration and disclosed tradeoffs, versus a bundle whose card, card quality and ROM contents you did not choose. Both are legitimate purchases. Do not let any shop — including us — tell you the second option does not exist.

---

## How not to get burned

Ask these five questions, in writing, before paying. The answers are cheap; discovering them afterwards is not.

1. **Which board revision, exactly?** V12, V21 or V30, in the order record.
2. **Built-in WiFi or not?** And if yes: is the speaker hum disclosed, and are you told that network settings may need a reflash to recover?
3. **What is delivered, and what does it cost delivered?** Item, shipping, and who pays import charges.
4. **What is the return window, and who pays return postage?**
5. **How do I get help when it goes wrong?** A named channel, not "contact us".

Then apply the same scrutiny to any review you read, because of the message quoted earlier: `B站里面全是R36S的玩机技巧，这款的全是广告宣传` — *Bilibili is full of R36S tips; this model is all advertising.* A useful video measures something (runtime, temperature, frame rates), shows a drawback, or opens the shell. A video that only unboxes it and says "very cost-effective" is an advert, whether or not it is labelled as one. That criticism is fair, it applies to this product more than to most, and the correct response is not to argue with it but to be the exception.

---

## What we measured, what we did not

| Claim | How we know |
|---|---|
| V12 = 13 finishes; V21 and V30 = 4 each; those exact 4 | **Our own catalogue data**, published in this repo as an image and a table |
| Built-in WiFi is a V21/V30 option; dongle available for all | **Our own catalogue data** |
| V21 and V30 silkscreen, with dates `2024-12-18` and `2025-11-18` | **Our own board photographs** |
| Both boards carry a Rockchip RK3326 | **Our own board photographs** |
| A real unit reports 895 MB total memory | **Our own photograph** of the vendor System Info screen |
| Starting price is $69 for a bare V12 | **Our own published price**; delivered total is quoted in writing |
| $79.99 card-and-games and $52.00 lowest US listings | **Our own market-research records**, October 2026. ⚠️ We did not verify the $52 listing's contents |
| ~¥260 domestic bundled price | QQ group message (R36S掌机爱好者). ⚠️ **Community report, not verified by us** |
| WiFi builds hum; network settings may need a reflash | Our own product disclosure and our own FAQ |
| Lost save files happen | QQ group messages. ⚠️ **No verified root cause**, and we say so |
| The V12-with-WiFi-noise message | ⚠️ **Unresolved** — built-in WiFi is not a V12 option in our own catalogue |
| A software check can identify the board | ⚠️ **We do not publish one as verified.** A device tree reports the `.dtb` that booted, not the board |
| Anything about PSP/N64/PS2 performance | **Stated as a limitation, not benchmarked by us.** We claim no frame rates |

The two diagrams in this article are drawn by `tools/make-diagrams.py` from the finish data reproduced in that
script, not by an image model. The three photographs are real photographs of supplier sample boards and of a real
unit's screen, cropped and downscaled only, and each caption says which it is.

Group quotations are verbatim, including their typos, attributed only to the group, because the source export cannot attribute them to a person. No price, version number, part number, command or file path in this article is invented.

---

## Related

- The bare R36S: choose a board revision, a finish, and whether you want WiFi → <https://r36s.space/products/r36s>
- First-steps guide, including what "bare" actually includes → <https://r36s.space/guide>
- Shop FAQ, including the WiFi hum and charging disclosures → <https://r36s.space/faq>
- Before-you-buy checklist → <https://r36s.space/blog/bare-r36s-checklist>
- Charging, battery and standby drain — the companion repository `r36s-charging-and-battery`
- Returns, including the 7-day change-of-mind window → <https://r36s.space/returns>
- Questions before you pay → <https://r36s.space/contact> or the Discord linked from the shop

*Written by the shop behind [r36s.space](https://r36s.space). We sell this handheld. The "who should not buy one" section is deliberately the longest honest list we could write, because a buyer who arrives informed does not ask for a refund. Licensed MIT.*

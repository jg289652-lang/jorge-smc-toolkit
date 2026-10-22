# Dehancer Pro Preservation Checklist

A practical, lawful checklist for keeping a paid Dehancer Pro license usable and your work portable. It uses only vendor-supported features and your own files. No cracking, patching, or bypassing activation. See [`legal-research-memo.md`](legal-research-memo.md) for the reasoning.

Suggested archive folder layout (keep it on two drives, and one copy off-site or in the cloud):

```
dehancer-archive/
├── 01-proof-of-purchase/     invoice, order email, checkout screenshots
├── 02-license-terms/         dated EULA + Terms of Service PDFs
├── 03-account/               account/license-widget screenshots, seat list
├── 04-installers/            official installers, one folder per version
├── 05-compatibility.md       which Dehancer version runs on which host/OS
├── 06-luts/                  exported .cube LUTs + a README of settings used
├── 07-reference-renders/     short test renders of each look you rely on
└── 08-correspondence/        support emails, written answers from Dehancer
```

## 1. Proof of what you bought
- [ ] Save the **invoice / order confirmation** (PDF). It should show the price ($449), date, and plan name (lifetime vs. subscription).
- [ ] Screenshot the **checkout page wording** if you still have it, or note it from memory with the date. Words like "buy", "license", and "lifetime" matter under California AB 2426.
- [ ] Save the payment record (card statement line or PayPal receipt).

## 2. The terms you agreed to
- [ ] Download the **EULA** and **Terms of Service** PDFs from `dehancer.com/legal/agreement`. Each shows an edition date.
- [ ] Re-download them whenever Dehancer announces a terms change, and keep the old ones. You want the version in force **when you bought**.
- [ ] Note the clauses on: governing law, reverse engineering, termination, LUT/output rights, transfer, and service discontinuation.

## 3. Account and seats
- [ ] Screenshot the **license widget / user profile** showing the plan type and seats. Lifetime is 2 seats on 2 devices.
- [ ] Record which machines hold which seat (machine name, OS, date activated).
- [ ] **Before** replacing a computer or reinstalling the OS, **deactivate** inside the plugin. Deactivations are unlimited.
- [ ] **Do not** accept a lifetime-to-subscription "exchange" offer unless you mean to: Dehancer's FAQ says the **lifetime license is revoked**.

## 4. Installers and compatibility
- [ ] Keep the **official installer** for every Dehancer version you've used, downloaded from Dehancer only.
- [ ] Record which Dehancer version works with which **host version** (e.g., DaVinci Resolve, Premiere Pro, FCP) and **OS version**. Host updates can break older OFX/plug-in builds.
- [ ] Before a major host or OS upgrade, confirm Dehancer supports it. If you're unsure, keep one machine (or a bootable backup) on a known-good combination.

## 5. Interoperability: export your looks
- [ ] With an activated **full Pro** license, use the **LUT Generator** to export `.cube` LUTs for each look you depend on. It is disabled in Lite, trials, and unactivated mode.
- [ ] For each LUT, write down: film profile, print stock, exposure/settings, input color space, and output color space.
- [ ] Remember the limit: a LUT is **color only**. Grain, halation, bloom, film damage, and overscan won't be in it. For those, keep **reference renders** (below) so you can rebuild the look elsewhere.
- [ ] Until the EULA confirms otherwise, treat exported LUTs as **for your own projects**. Don't sell or share them.
- [ ] Test each LUT in a second app (e.g., Resolve and Premiere). Color-space mismatches are the usual cause of different results.

## 6. Reference renders
- [ ] Render a short **test clip** (a color chart and a skin-tone shot are ideal) through each look you rely on, with all effects on. This is your visual record of the full look.
- [ ] Keep **final masters** of finished projects, not just project files. A project that depends on a plugin you can no longer activate will re-render with a watermark.

## 7. Get it in writing
- [ ] Send the questions in [`support-request-template.md`](support-request-template.md) to Dehancer support.
- [ ] Save every reply in `08-correspondence/`.

## 8. Recurring checks (every 6 months, or before upgrades)
- [ ] Is your seat still active? Does the plugin still work after a full restart **offline**? Record the result, because no Dehancer documentation on offline grace periods was found.
- [ ] Any new terms, price changes, or product-discontinuation notices?
- [ ] Any update on the 2027 DMCA §1201 exemption cycle (`copyright.gov/1201/2027/`)?

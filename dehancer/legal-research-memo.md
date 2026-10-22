# Dehancer Pro ($449): Preservation & Interoperability — Legal Research Memo

**Prepared:** October 22, 2026
**Subject:** What rights a buyer of a $449 Dehancer Pro license has to *preserve* (keep using, back up, archive) the software and to *interoperate* (move looks/work into other tools), and what consumer-protection law applies to Dehancer's lifetime and subscription plans.

> **Not legal advice.** This is research for self-help and for a conversation with a lawyer. Several points are marked **VERIFY** because the primary source could not be opened from the research environment (see [Research limits](#research-limits)).

---

## 1. Short answers

| Question | Short answer |
|---|---|
| What did $449 buy? | $449 matches Dehancer's published **lifetime** price for Dehancer Pro (a deal price, down from $549, that ran until 25 May 2025). Subscriptions at the time were priced separately (e.g., 1 year $299). **Check your invoice**: lifetime and subscription buyers have different rights, so everything below turns on which one you have. |
| Do you "own" it? | Probably **not** in the copyright sense. Dehancer sells a *license* that it can restrict. In the Ninth Circuit (California), *Vernor v. Autodesk* treats a buyer whose license restricts transfer and use as a **licensee**, not an owner. That limits the statutory "owner of a copy" rights (first sale, §117 archival copies). |
| Can you keep a backup? | Keeping the installers, your invoice, and your license records is low-risk and strongly recommended. A formal *statutory* backup right is uncertain in the U.S. for licensees, but clear in the U.K. for a "lawful user" (CDPA s. 50A), and the U.K. voids contract terms that override it (s. 296A). Dehancer is a U.K. company. |
| Can you bypass activation to "preserve" it if Dehancer's servers go away? | **No safe route today for an individual.** Circumventing license activation is an access-control circumvention under 17 U.S.C. §1201(a)(1). In the Ninth Circuit (*MDY v. Blizzard*) that is actionable even without copyright infringement. The 2024 software-preservation exemption covers **eligible libraries, archives and museums**, not individual users. |
| Interoperability: can you move your looks to other software? | Yes, through the **built-in LUT Generator**. It is the lawful, vendor-sanctioned interoperability path. It requires an activated full Pro license (or the Video & Photo subscription) and exports standard `.cube` LUTs. Technical limit: a LUT captures **color only**, not grain, halation, bloom or film damage. Check the EULA for any restriction on using exported LUTs after a subscription ends (**VERIFY**). |
| Does reverse-engineering law help? | Only narrowly. U.S. fair use allows reverse engineering *to build an independent, interoperable program* (*Sega*, *Connectix*), and §1201(f) has a matching exception. But U.S. courts enforce EULA bans on reverse engineering (*Bowers*, *Davidson v. Jung*). U.K./EU law voids those bans for decompilation that meets strict interoperability conditions. None of this authorizes cracking activation to keep using Dehancer itself. |
| Subscription protections? | **U.S.:** ROSCA and state auto-renewal laws apply. California's amended ARL (AB 2863, in force July 1, 2025) requires easy online cancellation, express consent and annual reminders. The FTC's "click-to-cancel" rule was **vacated** (8th Cir., July 2025), and the FTC has restarted rulemaking. **U.K.:** the DMCC Act subscription regime is not yet in force (January 2027 or spring 2027, depending on the source). |
| Biggest practical trap | Dehancer's FAQ says you can exchange a lifetime license for a subscription, but the **lifetime license is revoked** in the exchange. Don't accept a "special offer" swap unless you mean to give up the perpetual license. |

---

## 2. Facts found

### 2.1 The vendor
- **DEHANCER LTD**, England, Companies House registration **15154995**. Dehancer's legal pages list two different registered-office addresses (Walton-on-Thames KT12 2SD and Iden, Rye TN31 7UY). **VERIFY** on Companies House.
- Dehancer's Legal Centre publishes a Terms of Service, an **End-User Licence Agreement (EULA)**, a Privacy Policy and Appendices A–D as dated PDFs at `dehancer.com/legal/agreement`. **The EULA text, including its governing-law clause, was not retrievable for this memo.** Getting it is action item #1.

### 2.2 Pricing and plans
- Shop page (cached): Dehancer Pro **lifetime $449** (deal; regular $549; deal ran until 25.05.2025). Time-limited plans were 3 months $149, 6 months $199, 1 year $299. Dehancer Lite lifetime was $199.
- **May 19, 2025:** Dehancer introduced subscriptions: Individual plans (3 seats) and a Studio plan. The announcement said lifetime pricing would rise on May 25.
- **June 3, 2026:** a separate **Dehancer Desktop Lifetime** plan (standalone app) was announced. It is a different product from the Pro plugin.

### 2.3 License mechanics (Dehancer help pages)
- **Lifetime:** 2 independent seats on 2 different devices. **Individual subscription:** 3 seats across 3 host applications.
- **Activation requires an internet connection.** Offline activation exists **only for the Production plan**, through a local Production License Server.
- Without activation, the plugin is fully functional except that it **watermarks preview and renders**, and the **LUT Generator is disabled**.
- Deactivate inside the plugin before changing computers or reinstalling the OS. Deactivations are unlimited.
- **License transfer** to another account is possible: "You completely hand over control of the License to another account. All your seats will be deactivated."
- **Updates:** Dehancer "currently do[es] not charge for updates" but "may discontinue outdated products," and unlimited updates "cannot be guaranteed." Subscription activation "may not work with legacy versions."
- **Lifetime → subscription exchange:** the amount paid for the lifetime license is credited, and the **lifetime license is revoked**.
- **Not found:** whether an activated seat re-checks the server periodically, or how long it works offline; and what happens to exported LUTs or rendered work after a subscription lapses.

---

## 3. Analysis

### 3.1 License or sale? Why it matters

Copyright law gives some rights only to the **"owner of a copy"**:
- **17 U.S.C. §109(a)** (first sale): the right to resell or give away your copy.
- **17 U.S.C. §117(a)**: the right to make a copy or adaptation that is (1) an *essential step* in using the program on a machine, or (2) for *archival purposes*.

**Ninth Circuit test.** *Vernor v. Autodesk, Inc.*, 621 F.3d 1102 (9th Cir. 2010): a user is a **licensee, not an owner**, when the copyright owner (1) specifies that the user is granted a license, (2) significantly restricts transfer, and (3) imposes notable use restrictions. Dehancer's model is account-bound activation, a seat cap, and transfer only by handing over the whole account license. It likely meets all three factors. If so, §117 and §109 are probably unavailable as *statutory* rights. What you have instead are the **contract** rights in the EULA.

*Contrast (VERIFY):* the Second Circuit's *Krause v. Titleserv, Inc.*, 402 F.3d 119 (2d Cir. 2005), looks at "incidents of ownership", such as a one-time payment and the right to keep the copy indefinitely. A one-time-fee lifetime license looks more like ownership under that test. It is persuasive outside the Second Circuit, not binding.

**U.K./EU angle.** Under the CJEU's *UsedSoft GmbH v. Oracle International Corp.*, C-128/11 (2012), a one-time fee for a license of **unlimited duration** for downloaded software is a "sale", and the distribution right is exhausted, so the copy may be resold. That decision binds EU courts. Because it predates Brexit, it is retained (now "assimilated") case law in the U.K. and binds lower courts unless an appellate court departs from it (**VERIFY** current U.K. treatment). A **lifetime** license is the strongest case for UsedSoft-style reasoning. A **subscription** is not.

### 3.2 Preservation

#### (a) What's clearly fine
- Keeping your **invoice, order confirmation, license/account screenshots, and the dated EULA PDF**.
- Keeping **copies of the official installers** for the versions you use, together with the host-app versions they work with (Resolve, Premiere, FCP, etc.).
- **Exporting LUTs** and keeping **rendered masters** of your own work.
- Using license **deactivation/transfer** as Dehancer documents it.

#### (b) Statutory backup rights
- **U.S.:** §117(a)(2) archival copies are clearest for an *owner of a copy* (see 3.1). As a practical matter, keeping a vendor-distributed installer for your own reinstall is low-risk. The software still needs activation, so the backup alone doesn't preserve access.
- **U.K.:** CDPA 1988 **s. 50A** lets a *lawful user*, which expressly includes a licensee, make a back-up copy "necessary ... for the purposes of his lawful use". **s. 296A** makes any contract term that restricts this **void**. If the EULA chooses English law, as is likely for a U.K. company but **VERIFY**, this is a real right.
- **EU:** Software Directive 2009/24/EC, **Art. 5(2)**: a backup copy can't be prevented by contract where necessary for use. **Art. 8** voids contrary terms.

#### (c) The activation problem (where preservation breaks)
Dehancer activation is online-only for non-Production plans. If the license server ever goes away, or a future OS or host update forces a reinstall, a backup installer may run only in **watermarked** demo mode.

- **17 U.S.C. §1201(a)(1)(A)** bars circumventing a technological measure that "effectively controls access" to a work. Online license activation is the classic example.
- **Ninth Circuit:** *MDY Industries, LLC v. Blizzard Entertainment, Inc.*, 629 F.3d 928 (9th Cir. 2010), holds that §1201(a) creates a right **independent of infringement**. In California's federal circuit, having paid for the software is not, by itself, a defense to circumventing its activation.
- **Federal Circuit:** *Chamberlain Group, Inc. v. Skylink Technologies, Inc.*, 381 F.3d 1178 (Fed. Cir. 2004), requires a **nexus to infringement**. That circuit split is unresolved, but it doesn't help a California resident whose case would be in the Ninth Circuit.
- **Current exemptions:** the Librarian of Congress's 2024 rule (37 C.F.R. §201.40; 89 Fed. Reg., Oct. 28, 2024, Docket No. 2023-5) runs **until October 28, 2027**. It renewed the **computer-program and video-game preservation** exemptions (**VERIFY** the scope of any 2024 changes), but those cover **eligible libraries, archives and museums**, not individual end users. An institution such as a college library may qualify for preserving software in its own collection. An individual protecting a personal license does not.
- **Tenth triennial (2027) cycle:** the Copyright Office opened it on **June 9, 2026** (Docket No. 2026-4). New-exemption petitions closed **Aug. 24, 2026**, and renewal comments closed **Sept. 28, 2026**. The next step is a **notice of proposed rulemaking** with public comment, and new exemptions would take effect around **October 2027**. If a proposed class covers server-dependent or abandoned software, individual users can file comments. Watch `copyright.gov/1201/2027/`.

**Bottom line:** the lawful preservation strategy is **contractual and practical**, not technical. Get written commitments from Dehancer, export what can be exported, and keep a working, activated setup.

### 3.3 Interoperability

#### (a) The sanctioned route: LUT Generator
- It is available with an activated **full Pro license** or the **Video & Photo subscription**. It is disabled in Lite, trials, and unactivated mode.
- It produces `.cube` 3D LUTs, the de facto interchange format read by DaVinci Resolve, Premiere Pro, Final Cut Pro, OBS, Photoshop, etc. Results can differ slightly between apps because of color-space settings.
- **Technical limit:** a 3D LUT is a per-pixel color mapping. It **cannot** carry spatial or temporal effects: grain, halation, bloom, film damage, gate weave, or overscan. Those parts of the "look" can only be preserved as rendered footage or rebuilt in other tools.
- **Legal open question (VERIFY in EULA):** whether exported LUTs may be (i) used commercially, (ii) used after a subscription ends, and (iii) shared or sold. Until confirmed, treat exported LUTs as **for your own projects only**.

#### (b) Reverse engineering for interoperability: U.S.
- **Fair use:** *Sega Enterprises Ltd. v. Accolade, Inc.*, 977 F.2d 1510 (9th Cir. 1992), holds disassembly is fair use where it is the only way to reach unprotected functional elements and there's a legitimate reason. *Sony Computer Entertainment, Inc. v. Connectix Corp.*, 203 F.3d 596 (9th Cir. 2000), protects intermediate copying while building a non-infringing, interoperable product.
- **§1201(f):** a person who has lawfully obtained the right to use a program may circumvent **for the sole purpose** of identifying and analyzing elements needed for interoperability of an **independently created program**. The elements must not be **previously readily available**, and the act must not be infringing. The Copyright Office's 2017 §1201 report revised its earlier view and acknowledged that (f) can cover a consumer's own circumvention for interoperability (**VERIFY** against the report text).
- **Contract override:** *Bowers v. Baystate Technologies, Inc.*, 320 F.3d 1317 (Fed. Cir. 2003), enforced a shrinkwrap **ban on reverse engineering** and held it was not preempted, following *ProCD v. Zeidenberg*, 86 F.3d 1447 (7th Cir. 1996). *Davidson & Associates v. Jung*, 422 F.3d 630 (8th Cir. 2005), rejected a §1201(f) defense because the circumvention enabled infringement, and held the EULA contract claims were not preempted.
- **Takeaway:** in the U.S., a typical EULA "no reverse engineering" clause is likely enforceable as a contract even where fair use would otherwise apply. And §1201(f) is about *building an independent compatible program*, not about keeping Dehancer running without activation.

#### (c) Reverse engineering for interoperability: U.K./EU
- **U.K. CDPA s. 50B** (decompilation): a lawful user may decompile when necessary to obtain information to create an **independent program** that interoperates. The conditions are strict: the information can't be readily available, use is limited to that purpose, and it can't be used to make a substantially similar program. **s. 50BA** lets a lawful user observe, study and test a program's functioning while running it normally. **s. 296A** voids contract terms restricting either.
- **EU:** Directive 2009/24/EC **Art. 6** is the decompilation-for-interoperability right, and **Art. 8** voids contrary terms. *Top System SA v. Belgian State*, C-13/20 (CJEU 2021), lets a lawful acquirer decompile when needed to **correct errors** affecting operation (**VERIFY** case number). It was decided after Brexit, so it is only persuasive in the U.K.
- **Caution:** these rights do **not** authorize distributing cracks or circumvention tools. The U.K. separately regulates circumvention devices for computer programs (CDPA s. 296, **VERIFY** scope).

### 3.4 Subscriptions and consumer protection

#### (a) If your $449 was a lifetime license
- **Don't accept the lifetime-to-subscription exchange** unless you intend to: the lifetime license is **revoked**.
- **Updates and product lifecycle:** Dehancer reserves the right to discontinue products. A "lifetime" license is realistically **lifetime of the product version and its host compatibility**, not a guarantee of future updates. Preserve working versions (see the checklist).
- **California AB 2426 (Cal. Bus. & Prof. Code §17500.6, effective Jan. 1, 2025):** a seller that advertises a revocable digital-goods license using words like "buy" or "purchase" must either get the buyer's affirmative acknowledgment that it's a license, or give a clear pre-purchase disclosure that "buying" confers a license, plus a link to the terms. The exemptions reportedly include **subscriptions** and goods provided for **permanent offline use**. Whether an online-activated "lifetime" plugin falls inside or outside the statute is **an open question (VERIFY statute text)**. If you bought in California after Jan. 1, 2025 and the checkout said "buy" with no license disclosure, note it. It may matter if Dehancer later revokes access.

#### (b) If it was (or becomes) a subscription
- **Federal:** the Restore Online Shoppers' Confidence Act (**ROSCA**, 15 U.S.C. §§8401–8405) and FTC Act §5 still govern negative-option billing. The FTC's 2024 "click-to-cancel" Negative Option Rule was **vacated in its entirety by the Eighth Circuit in July 2025**, and the FTC has since restarted rulemaking (ANPRM stage in 2026). Enforcement continues under ROSCA and §5.
- **California Automatic Renewal Law** (Cal. Bus. & Prof. Code §§17600 et seq.), as amended by **AB 2863** for contracts entered, amended or extended **on/after July 1, 2025**, requires:
  - express affirmative consent to renewal terms, with records kept;
  - online cancellation through the same medium used to sign up;
  - **annual reminders** with cost and cancellation information;
  - clear notice of material price or terms changes.
  Dehancer's Studio plan is described as "billed $588/year auto-renews", so it is squarely an auto-renewal.
- **U.K.:** the **DMCC Act 2024** subscription-contracts regime (pre-contract information, renewal reminders, easy exit, cooling-off on renewals) is **not yet in force**. The government's April 2, 2026 consultation response targeted spring 2027. A later report (Wiggin tracker, Oct. 14, 2026) says the Prime Minister's Office announced **January 2027** (**VERIFY** on gov.uk). The DMCC Act's general unfair-commercial-practices provisions have applied since **April 2025**.
- **U.K. Consumer Rights Act 2015** (if English law governs and you're a consumer; **VERIFY** reach for non-U.K. buyers): digital content must be of **satisfactory quality, fit for purpose and as described** (ss. 34–36). Remedies are repair or replacement (s. 43), price reduction (s. 44), and refund in some cases (s. 45). **s. 46** covers damage to your device or other digital content caused by lack of reasonable care.

### 3.5 What not to do
These carry real legal risk (DMCA §1201 civil liability, contract breach, account termination) and are **outside the scope of this toolkit**:
- using cracked builds, keygens, or "patched" plugins, including from discount "lifetime key" resellers (one such reseller was listing Dehancer Pro "lifetime" at about €52; treat it as suspect);
- sharing your account or activations beyond your seat count;
- distributing exported LUTs or Dehancer profile data as your own product before confirming the EULA allows it.

---

## 4. Action items (in order)

1. **Pull your invoice.** Confirm lifetime vs. subscription, purchase date, price, and the exact checkout wording ("buy", "license", "lifetime").
2. **Download the dated EULA and Terms of Service PDFs** from `dehancer.com/legal/agreement` and save them with your invoice. Read and note:
   - the governing-law and jurisdiction clause;
   - the reverse-engineering clause and any "except as permitted by law" carve-out;
   - termination and suspension;
   - rights in **exported LUTs** and rendered output;
   - end-of-life or server-shutdown provisions;
   - transfer.
3. **Send the support request** in [`support-request-template.md`](support-request-template.md) to get written answers to the open questions. A written vendor statement is the strongest preservation tool you have.
4. **Run the preservation checklist** in [`preservation-checklist.md`](preservation-checklist.md).
5. **Decline any lifetime-to-subscription swap** unless you have decided to give up the perpetual license.
6. **Watch the 2027 §1201 cycle** (`copyright.gov/1201/2027/`). Comment on the NPRM if a proposed class covers server-dependent or abandoned software.
7. **If Dehancer revokes access, changes terms, or makes the product unusable**, bring this memo, your invoice, the dated EULA and the support correspondence to a consumer-protection or IP attorney. California consumers can also complain to the state Attorney General, and U.K. consumers can use Trading Standards or the CMA.

---

## 5. Authorities

### U.S. statutes and regulations
- 17 U.S.C. §107 (fair use); §109(a) (first sale); §117(a) (essential-step and archival copies)
- 17 U.S.C. §1201(a)(1)(A) (anti-circumvention); §1201(a)(2) (trafficking); §1201(f) (reverse engineering for interoperability)
- 37 C.F.R. §201.40 (2024 exemptions, effective Oct. 28, 2024 – Oct. 28, 2027) — [Federal Register 2024-24563](https://www.federalregister.gov/documents/2024/10/28/2024-24563/exemption-to-prohibition-on-circumvention-of-copyright-protection-systems-for-access-control)
- Tenth Triennial §1201 Proceeding, Docket No. 2026-4 — [Federal Register 2026-11545 (June 9, 2026)](https://www.federalregister.gov/documents/2026/06/09/2026-11545/exemptions-to-permit-circumvention-of-access-controls-on-copyrighted-works); [copyright.gov/1201/2027](https://www.copyright.gov/1201/2027/)
- U.S. Copyright Office, *Section 1201 of Title 17* (June 2017) — [copyright.gov/policy/1201](https://www.copyright.gov/policy/1201/)
- 15 U.S.C. §§8401–8405 (ROSCA)
- Cal. Bus. & Prof. Code §17500.6 (AB 2426, digital goods license disclosures)
- Cal. Bus. & Prof. Code §§17600 et seq. (Automatic Renewal Law), as amended by AB 2863

### U.S. cases
- *Sega Enterprises Ltd. v. Accolade, Inc.*, 977 F.2d 1510 (9th Cir. 1992)
- *ProCD, Inc. v. Zeidenberg*, 86 F.3d 1447 (7th Cir. 1996)
- *Sony Computer Entertainment, Inc. v. Connectix Corp.*, 203 F.3d 596 (9th Cir. 2000) — [opinion](https://law.resource.org/pub/us/case/reporter/F3/203/203.F3d.596.99-15852.html)
- *Bowers v. Baystate Technologies, Inc.*, 320 F.3d 1317 (Fed. Cir. 2003)
- *Chamberlain Group, Inc. v. Skylink Technologies, Inc.*, 381 F.3d 1178 (Fed. Cir. 2004)
- *Krause v. Titleserv, Inc.*, 402 F.3d 119 (2d Cir. 2005)
- *Davidson & Associates v. Jung*, 422 F.3d 630 (8th Cir. 2005) — [opinion](https://law.resource.org/pub/us/case/reporter/F3/422/422.F3d.630.04-3654.html)
- *Vernor v. Autodesk, Inc.*, 621 F.3d 1102 (9th Cir. 2010)
- *MDY Industries, LLC v. Blizzard Entertainment, Inc.*, 629 F.3d 928 (9th Cir. 2010)
- Eighth Circuit vacatur of the FTC Negative Option Rule (July 2025) — see [Cooley](https://www.cooley.com/news/insight/2025/2025-07-11-click-to-cancel-just-got-cancelled-eighth-circuit-vacates-entirety-of-ftcs-negative-option-rule), [Gibson Dunn](https://www.gibsondunn.com/ftc-restarts-negative-option-rulemaking-after-eighth-circuit-vacatur-enforcement-under-rosca-continues/), [Jones Day (May 2026)](https://www.jonesday.com/en/insights/2026/05/ftc-revives-clicktocancel-rule-new-risks-for-subscription-businesses)

### U.K. / EU
- Copyright, Designs and Patents Act 1988, ss. 50A, 50B, 50BA, 296A — [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/1988/48/part/I/chapter/III/crossheading/computer-programs-lawful-users)
- Consumer Rights Act 2015, ss. 34–46 — [legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2015/15/section/46)
- Digital Markets, Competition and Consumers Act 2024 (subscription contracts) — [Taylor Wessing (Apr. 2026)](https://www.taylorwessing.com/en/insights-and-events/insights/2026/04/subscription-contracts), [Wiggin tracker](https://www.wiggin.co.uk/insight/digital-markets-competition-and-consumer-act-tracker/)
- Directive 2009/24/EC (Software Directive), Arts. 5, 6, 8
- *UsedSoft GmbH v. Oracle International Corp.*, C-128/11 (CJEU 2012)
- *Top System SA v. Belgian State*, C-13/20 (CJEU 2021)

### Dehancer sources
- [Legal Centre](https://www.dehancer.com/legal) · [EULA/agreements](https://www.dehancer.com/legal/agreement)
- [License Basics](https://www.dehancer.com/learn/article/license-basics) · [License Activation](https://www.dehancer.com/learn/article/license) · [Offline License Activation (Production plan only)](https://www.dehancer.com/learn/article/offline-license-activation)
- [Payments & Upgrades FAQ](https://www.dehancer.com/learn/article/faq-prices-and-tariffs) · [Shop](https://dehancer.com/shop) · [Pricing](https://www.dehancer.com/pricing)
- [Introducing Dehancer subscriptions (May 19, 2025)](https://blog.dehancer.com/2025/05/19/introducing-dehancer-subscriptions/) · [Dehancer Desktop Lifetime (June 3, 2026)](https://blog.dehancer.com/2026/06/03/new-plan-dehancer-desktop-lifetime/)

### Secondary
- Eric Goldman on *Vernor* — [blog.ericgoldman.org](https://blog.ericgoldman.org/archives/2009/10/vernor_v_autode_1.htm)
- Project DisCo on interoperability in the 2017 §1201 report — [project-disco.org](https://project-disco.org/intellectual-property/070617-interoperability-and-the-copyright-offices-section-1201-report/)
- AB 2426 summaries — [Greenberg Glusker](https://www.greenbergglusker.com/publications/new-california-law-ab-2426-licensing-disclosures-for-digital-goods), [Cooley](https://www.cooley.com/news/insight/2024/2024-10-01-new-california-law-requires-disclosures-for-selling-online-digital-goods)
- AB 2863 summary — [Davis Wright Tremaine](https://dwt.com/insights/2024/10/ab-2863-updates-california-automatic-renewal-law)

---

## Research limits

- **Dehancer's EULA was not read.** `dehancer.com` was blocked by the research environment's network policy, so Dehancer facts come from search-indexed copies of its help, shop and blog pages. Governing law, the reverse-engineering clause, termination, and LUT-output rights are therefore **unconfirmed**.
- **Case-law database not available.** The CourtListener and Descrybe connectors failed to connect, so case holdings were checked against secondary sources and published opinions where available. Check pin cites and subsequent history (e.g., on CourtListener or Google Scholar) before citing in anything formal.
- **Moving targets:** the 2027 §1201 cycle, the FTC negative-option rulemaking, and the U.K. DMCC subscription commencement date were all changing as of October 2026.

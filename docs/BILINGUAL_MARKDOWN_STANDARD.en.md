# Bilingual AWS Micro-Lab Markdown & RTL standard v1.1

[فارسی](BILINGUAL_MARKDOWN_STANDARD.fa.md)

Applies to **all future AWS micro-labs** published on this profile repository.

## File conventions

- Each English page `README.md`, `manual.en.md`, `cleanup.en.md`, etc. has an equivalent `README.fa.md`, `manual.fa.md`, `cleanup.fa.md`.
- Both versions contain **equivalent goals, steps, safety checks, cost trade-offs and cleanup verification**; neither language is a summary-only edition.
- Each Persian `.fa.md` **must** begin with a GitHub-safe RTL container and end with a closing `</div>`; put blank lines around the Markdown inside so GitHub renders headings and lists correctly:

```html
<div dir="rtl" align="right">

# عنوان فارسی

متن فارسی با نام سرویس `AWS Lambda`.

</div>
```

- For multiline code or shell blocks inside RTL pages, use a left-to-right explicit `<pre dir="ltr" align="left"><code> ... </code></pre>` and HTML-escape `<`, `>`, `&` inside code. This prevents command/code mirroring. Inline names should remain wrapped with backticks.
- Tables/lists should inherit RTL from the wrapper; check GitHub **Preview** on mobile and desktop. Do not rely on CSS or JavaScript, which GitHub sanitizes.
- In Persian documents keep prose Persian script; service labels remain official English names. Use short links rather than long raw Latin URLs in Persian paragraphs.
- Add reciprocal language links at the top. Include source links and note AWS console UI labels can change.

## Mandatory kit components

1. Source question plus diagram and any answer-key ambiguity.
2. No-create **console tour of all services appearing in every option and reference diagram**, with tab names and explicit STOP points.
3. Optional smallest executable lab, with a written explanation of *why it differs* from reference architecture.
4. Service-by-service cost model comparison, Region/account caveats and official links.
5. English/Persian manual, preflight, Terraform path (if relevant), Draw.io task, cleanup, evidence.
6. AWS test never claimed before actual run; cleanup separately verified.

Run the repository's `scripts/check_micro_lab_locales.py` validator; maintain equivalent links and coverage with human review.

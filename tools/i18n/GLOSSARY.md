# JaiDeeClear Thai glossary + style (use for every /th/ page)

Voice: polite, confident, plain Thai for homeowners and property managers. Short sentences. Use คุณ, never ท่าน.
No particles like ค่ะ/ครับ in page copy. No machine-translation phrasing - write it the way a Thai sales page reads.

## Fixed terms
| English | Thai |
|---|---|
| window film / window tinting (general) | ฟิล์มกรองแสง |
| tint the glass / window film for glass (house) | ติดฟิล์มกระจกบ้าน / ฟิล์มติดกระจกบ้าน |
| building film | ฟิล์มอาคาร / ฟิล์มกรองแสงอาคาร |
| ceramic film | ฟิล์มเซรามิค (spell with ค - the searched form) |
| safety / security film | ฟิล์มนิรภัย |
| free on-site measurement | วัดพื้นที่หน้างานฟรี |
| quote | ใบเสนอราคา |
| written warranty | รับประกันเป็นลายลักษณ์อักษร (never promise a blanket "7 ปี") |
| heat rejection | กันความร้อน |
| UV blocked 99% | กัน UV ได้ 99% |
| glare | แสงจ้า |
| privacy (outside can't see in) | ความเป็นส่วนตัว / ข้างนอกมองไม่เห็น |
| sq ft | ตร.ฟุต |
| installed (price) | รวมค่าติดตั้ง |
| on-site / we come to you | ถึงหน้างาน / เราไปหาคุณถึงที่ |
| technicians | ช่างผู้ชำนาญ |
| building management (condo juristic) | นิติบุคคลอาคาร |
| villa | วิลล่า · condo คอนโด · house บ้าน · office สำนักงาน · hotel โรงแรม |
| Bangkok กรุงเทพฯ · Phuket ภูเก็ต · Chonburi ชลบุรี · Pattaya พัทยา | |

Keep in English: brand JaiDeeClear, film series names (Carbon Series, Metallic Series, Ceramic Nano, Ceramic UV400,
Titanium Series, Sputtering Film, Safety Film 0.2mm...), UVR/IRR/TSER, WhatsApp, Instagram, Google, @handles,
prices/numbers, people's names.

## Rules
- Output a JSON object {english_string: thai_string} covering EVERY string in the source list, same keys verbatim.
- Keep HTML entities that appear in the source (&amp; &rarr; &#128205; &nbsp; &middot;) - the value is inserted raw into HTML,
  so a literal ampersand must stay as &amp;. Never add raw < or >.
- Some headings are split into fragments across <span>/<em> tags (e.g. "Window Tinting for" + "Villas" + "in Thailand").
  Read the source .html to see how fragments join, and translate each fragment so the joined Thai reads naturally.
- Reviews/testimonials: translate faithfully, keep the names and places.
- Do not invent facts, numbers, claims or guarantees that the English does not make.
- <title> and meta description: rewrite for Thai search using the page's target keywords (below), not a literal translation.
  Title ≤ 60 chars incl. " | JaiDeeClear". Meta description ≤ 150 Thai characters.
- The H1 must contain the primary keyword.

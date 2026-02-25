#!/usr/bin/env python3
"""
JaiDeeClear — Programmatic SEO City Page Generator
Generates 7 city-specific HTML landing pages for window tinting services.
"""

import os
import json
from urllib.parse import quote

# ──────────────────────────────────────────────
# CONSTANTS
# ──────────────────────────────────────────────
WHATSAPP = "+66655079694"
FORMSPREE = "https://formspree.io/f/xovkoeap"
LINE_URL = "https://line.me/ti/p/[PLACEHOLDER-LINE-ID]"
FACEBOOK = "https://www.facebook.com/Jaideeclear"
INSTAGRAM = "https://www.instagram.com/jaideeclear"
SELINE_TOKEN = "900711a10bdeff9"
LOGO = "jdclogo.jpg"

# WhatsApp SVG icon path (shared across header + mobile menu)
WA_SVG = '<svg class="whatsapp-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>'

# Will be populated by build_cities()
CITIES = []


def build_cities():
    """Return the list of all 7 city data dictionaries."""
    return [
        _city_bangkok(),
        _city_phuket(),
        _city_pattaya(),
        _city_chiang_rai(),
        _city_samui(),
        _city_krabi(),
        _city_hua_hin(),
    ]


# ══════════════════════════════════════════════
# CITY DATA FUNCTIONS
# ══════════════════════════════════════════════

def _city_bangkok():
    return {
        "name": "Bangkok",
        "slug": "bangkok",
        "province": "Bangkok",
        "lat": "13.7563",
        "lng": "100.5018",
        "meta_desc": "Professional window tinting in Bangkok. 99% UV protection, up to 30% energy savings. On-site installation for condos, townhouses & offices. Free quote — WhatsApp us today.",
        "hero_sub": "Bangkok's relentless urban heat, year-round UV index above 12, and glass-heavy high-rise skyline make quality window film essential. JaiDeeClear delivers professional on-site installation across the city — from Sukhumvit condos to Sathorn office towers and Ladprao townhouses.",
        "stat_uv": "UV 13",
        "stat_uv_label": "Bangkok's Peak UV Index",
        "film_carbon_desc": "Our entry-level option — solid basic UV protection at a budget-friendly price point. Ideal for rental condos along Sukhumvit or On Nut where cost is the primary consideration.",
        "film_nano_desc": "The top choice for Bangkok condos and townhouses. Nano-ceramic technology delivers excellent heat and glare reduction without a metallic appearance — keeping your city views crystal clear.",
        "film_nano_local_note_bold": "Bangkok favourite:",
        "film_nano_local_note": "The go-to choice for Bangkok high-rise condos — blocks intense afternoon heat while preserving panoramic city views from floor-to-ceiling glass.",
        "film_uv400_desc": "Enhanced UV400 blocking for maximum skin and furniture protection. Ideal for west-facing condos along the Chao Phraya River and townhouses with large sliding doors catching Bangkok's brutal afternoon sun.",
        "film_sputtering_desc": "Premium magnetron-sputtered film for maximum solar control. The preferred choice for CBD office buildings, luxury condos on Wireless Road, and commercial properties requiring the highest TSER performance.",
        "quick_guide_premium_label": "Premium / commercial / CBD",
        "process_title": "Professional Installation Across Bangkok",
        "process_sub": "We come to you anywhere in Bangkok — no need to remove windows or visit a workshop.",
        "process_step1_text": "WhatsApp us or use our online form with your property type and location — whether you're in Sukhumvit, Silom, or Ladprao.",
        "process_step2_text": "Our technician visits your property — from an Asok high-rise condo to a Bangna townhouse — to measure all windows at no charge.",
        "property_types_subtitle": "From high-rise condos to CBD offices — we tailor every installation to the property.",
        "property_types": [
            {
                "emoji": "🏢",
                "title": "Condos & Apartments",
                "subtitle": "High-rise condos · Serviced apartments · Rental units",
                "desc": "Bangkok's glass-tower condos trap enormous amounts of heat — especially units facing west along Sukhumvit and the river. A single installation typically done in 3-5 hours can drop indoor temperatures noticeably and slash your monthly electricity bill.",
                "testimonial": "\"Our electricity bill dropped about \\u0E3F3,000/month after tinting our 2-bed condo. The afternoon sun used to make the living room unusable — now it's comfortable all day.\"",
                "testimonial_author": "— Condo owner, Sukhumvit 24"
            },
            {
                "emoji": "🏠",
                "title": "Houses & Townhouses",
                "subtitle": "Townhouses · Detached homes · Moobaan estates",
                "desc": "Bangkok townhouses with large sliding glass doors and skylights face relentless heat gain. We install films that reduce heat without darkening rooms — ideal for family homes across Ladprao, Bangna, and Ratchada where natural light matters.",
                "testimonial": "\"Three-storey townhouse in Rama 9 area. They did every window in one day — bedrooms are noticeably cooler and the kids' playroom no longer overheats in the afternoon.\"",
                "testimonial_author": "— Homeowner, Rama 9"
            },
            {
                "emoji": "🏬",
                "title": "Offices & Commercial",
                "subtitle": "CBD offices · Co-working spaces · Retail shopfronts",
                "desc": "Office buildings in Silom, Sathorn, and Asok face massive cooling costs from floor-to-ceiling glass facades. We handle multi-floor installations with flexible scheduling — zero business disruption, commercial-grade film, and volume pricing.",
                "testimonial": "\"Had our 3-floor co-working space in Sathorn done over a weekend. Staff immediately noticed the difference on Monday — less glare on screens and the AC runs less.\"",
                "testimonial_author": "— Office manager, Sathorn"
            }
        ],
        "faq_title": "Common Questions About Window Tinting in Bangkok",
        "faqs": [
            {"q": "How much does window tinting cost in Bangkok?", "a": "Window tinting in Bangkok ranges from \\u0E3F50-70/sq.ft for carbon film to \\u0E3F155+/sq.ft for premium sputtering film. A typical 2-bedroom condo costs \\u0E3F5,400-11,000 depending on glass area and film choice. We provide free on-site measurements and quotes."},
            {"q": "Do you cover all areas of Bangkok?", "a": "Yes — we serve all Bangkok districts including Sukhumvit, Silom, Sathorn, Ladprao, Bangna, Thonburi, Asok, Ratchada, Chatuchak, and surrounding areas like Nonthaburi. Our technicians travel to your property for free measurement and installation."},
            {"q": "How long does window film installation take?", "a": "A typical condo takes 3-5 hours. A townhouse takes one full day. Larger commercial projects or office buildings take 1-3 days. You can stay in the property during installation."},
            {"q": "Which window film do you recommend for Bangkok condos?", "a": "For most Bangkok condos, our Ceramic Nano film offers the best balance of heat rejection, UV protection, and clarity — it maintains city views while blocking intense urban heat. For west-facing units, Ceramic UV400 provides extended UV spectrum blocking. For offices and commercial, our Sputtering Series delivers maximum performance."},
            {"q": "How much will I save on electricity with window film?", "a": "Most Bangkok customers see a 20-30% reduction in monthly electricity bills. High-rise condos with heavy AC usage see the biggest savings — some condo owners in Sukhumvit and Silom report saving \\u0E3F1,500-3,000+ per month during hot season."},
            {"q": "Does window film block natural light?", "a": "Our Ceramic Nano and Ceramic UV400 films maintain high visible light transmission — rooms stay bright and natural-looking. You'll notice a dramatic reduction in heat and glare without losing light quality. This is especially important for Bangkok condos where natural light is a premium."},
            {"q": "What's the warranty on your window film?", "a": "All films carry a manufacturer-backed warranty: 2 years for Carbon Series, 5 years for Ceramic Nano and Ceramic UV400, and 7 years for Sputtering Series. Covers peeling, bubbling, discoloration, and delamination."},
            {"q": "Can condo management approve window film installation?", "a": "Window film is installed on the interior surface of glass, so it typically does not require juristic office approval. However, we recommend checking with your building management. We can provide technical specifications and samples to help with any approval process."},
            {"q": "Can window film be removed or replaced?", "a": "Yes — window film is fully removable. If you want to upgrade or replace end-of-life film, we strip the old film and install new. Old film removal costs \\u0E3F20-30/sq.ft additional."}
        ],
        "pricing_title": "The Real Cost of Window Tinting in Bangkok",
        "pricing_rows": [
            ("Studio / 1-bed condo", "30-60 sq.ft", "\\u0E3F2,700-6,600"),
            ("2-bed condo", "60-100 sq.ft", "\\u0E3F5,400-11,000"),
            ("3-bed townhouse", "120-200 sq.ft", "\\u0E3F10,800-22,000"),
            ("Large house (4+ bed)", "200-350 sq.ft", "\\u0E3F18,000-38,500+"),
            ("Small office", "100-200 sq.ft", "\\u0E3F9,000-22,000"),
        ],
        "reviews_title": "What Bangkok Customers Say",
        "reviews_sub": "Real feedback from property owners across Bangkok.",
        "reviews": [
            {"text": "Had our corner unit condo on Sukhumvit 39 done with Ceramic Nano. The west-facing windows used to make the living room a sauna after 2pm — now the temperature is consistent all day. Installer finished in under 4 hours, very professional.", "author": "James R.", "meta": "Condo owner · Sukhumvit, Bangkok · Ceramic Nano"},
            {"text": "We tinted our entire 3-storey townhouse in Ladprao. Five bedrooms, living room, all sliding doors. Took one full day and the team was meticulous. Our monthly electricity dropped by about 25% — the house feels completely different.", "author": "Khun Nida S.", "meta": "Homeowner · Ladprao, Bangkok · Ceramic UV400"},
            {"text": "Office in Sathorn with floor-to-ceiling glass — the glare on screens was terrible and cooling costs were through the roof. Sputtering film solved both problems. Staff productivity genuinely improved.", "author": "Tom K.", "meta": "Office manager · Sathorn, Bangkok · Sputtering Series"}
        ],
        "areas": ["Sukhumvit", "Silom", "Sathorn", "Ladprao", "Bangna", "Thonburi", "Asok", "Ari", "Ekkamai", "On Nut", "Ratchada", "Phrom Phong", "Rama 9", "Chatuchak", "Thong Lo", "Prakanong", "Wongwian Yai", "Bang Sue", "Nonthaburi", "Phra Khanong"],
        "nearby_cities": [("Pattaya", "pattaya"), ("Hua Hin", "hua-hin"), ("Phuket", "phuket")],
        "cta_title": "Ready to Tint Your Bangkok Property?",
        "cta_sub": "Get a free on-site measurement and no-obligation quote. We serve all areas across Bangkok.",
        "contact_district_placeholder": "e.g. Sukhumvit, Silom, Ladprao...",
        "related_locations": [("Pattaya", "pattaya"), ("Hua Hin", "hua-hin"), ("Phuket", "phuket"), ("Chiang Rai", "chiang-rai")],
    }


def _city_phuket():
    return {
        "name": "Phuket",
        "slug": "phuket",
        "province": "Phuket",
        "lat": "7.8804",
        "lng": "98.3923",
        "meta_desc": "Professional window tinting in Phuket. 99% UV protection, up to 30% energy savings. On-site installation for villas, condos & resorts. Free quote — WhatsApp us today.",
        "hero_sub": "Phuket's year-round tropical sun, intense coastal UV, and booming villa and resort market demand the highest-quality window film. JaiDeeClear delivers professional on-site installation across the island — from beachfront condos to luxury villas and resort properties.",
        "stat_uv": "UV 12+",
        "stat_uv_label": "Phuket Peak UV Index",
        "film_carbon_desc": "Our entry-level option — solid basic UV protection at a budget-friendly price point. Ideal for short-term rental properties and Airbnb villas in Patong or Kata where cost is the primary consideration.",
        "film_nano_desc": "The top choice for Phuket condos and villas. Nano-ceramic technology delivers excellent heat and glare reduction without a metallic appearance — preserving your Andaman Sea views.",
        "film_nano_local_note_bold": "Phuket favourite:",
        "film_nano_local_note": "The go-to choice for Phuket villas — blocks intense coastal UV while preserving sea views from floor-to-ceiling glass.",
        "film_uv400_desc": "Enhanced UV400 blocking for maximum skin and furniture protection. Ideal for Phuket villas with large west-facing windows catching the intense Andaman sunset exposure.",
        "film_sputtering_desc": "Premium magnetron-sputtered film for maximum solar control. The preferred choice for Phuket luxury villas, five-star resorts, and commercial properties requiring the highest TSER performance.",
        "quick_guide_premium_label": "Premium / commercial / resort",
        "process_title": "Professional Installation Across Phuket Island",
        "process_sub": "We come to you anywhere on Phuket — no need to remove windows or visit a workshop.",
        "process_step1_text": "WhatsApp us or use our online form with your property type and location — whether you're in Patong, Rawai, or Cherng Talay.",
        "process_step2_text": "Our technician visits your property — from a Kamala beachfront condo to a Bang Tao hillside villa — to measure all windows at no charge.",
        "property_types_subtitle": "From private villas to five-star resorts — we tailor every installation to the property.",
        "property_types": [
            {
                "emoji": "\U0001f3e1",
                "title": "Villas",
                "subtitle": "Pool villas \u00b7 Hillside estates \u00b7 Airbnb properties",
                "desc": "Phuket's villas feature expansive floor-to-ceiling glass designed to capture ocean views — but that glass also traps enormous amounts of heat. We install films that reject heat without compromising the views your property was built for.",
                "testimonial": "\"Our electricity bill dropped by about \u0e3f3,500/month after the install. The villa stays cool without running AC all day — guests love it.\"",
                "testimonial_author": "\u2014 Villa owner, Rawai"
            },
            {
                "emoji": "\U0001f3e8",
                "title": "Hotels & Resorts",
                "subtitle": "Boutique hotels \u00b7 Five-star resorts \u00b7 Serviced apartments",
                "desc": "Guest comfort drives reviews, and reviews drive bookings. We handle multi-room installations floor by floor with flexible scheduling — zero guest disruption, commercial-grade film, and volume pricing for large properties.",
                "testimonial": "\"They worked around our guest schedule perfectly. 40+ rooms done in under a week, and we've seen a measurable drop in cooling costs across the property.\"",
                "testimonial_author": "\u2014 Hotel GM, Kata Beach"
            },
            {
                "emoji": "\U0001f3e2",
                "title": "Condos",
                "subtitle": "Sea-view condos \u00b7 Retirement units \u00b7 Investment properties",
                "desc": "Condo units with west-facing or south-facing glass get hit hardest by Phuket's afternoon sun. A single installation — typically done in 3-5 hours — can drop indoor temperatures noticeably and protect furniture from rapid UV fading.",
                "testimonial": "\"My afternoon temperature used to hit 36\u00b0C near the windows. After the Ceramic Nano install it barely reaches 30\u00b0C. Wish I'd done it sooner.\"",
                "testimonial_author": "\u2014 Condo owner, Patong"
            }
        ],
        "faq_title": "Common Questions About Window Tinting in Phuket",
        "faqs": [
            {"q": "How much does window tinting cost in Phuket?", "a": "Window tinting in Phuket ranges from \u0e3f50-70/sq.ft for carbon film to \u0e3f155+/sq.ft for premium sputtering film. A typical 3-bedroom villa costs \u0e3f15,000-45,000 depending on glass area and film choice. We provide free on-site measurements and quotes."},
            {"q": "Do you cover all areas of Phuket island?", "a": "Yes \u2014 we serve the entire island including Patong, Kata, Karon, Kamala, Bang Tao, Cherng Talay, Rawai, Chalong, Phuket Town, Kathu, Wichit, Rassada, and Cape Panwa. Our technicians travel to your property for free measurement and installation."},
            {"q": "How long does window film installation take?", "a": "A typical condo takes 3-5 hours. A 3-4 bedroom villa takes one full day. Larger commercial projects or resort properties take 1-3 days. You can stay in the property during installation."},
            {"q": "Which window film do you recommend for Phuket?", "a": "For most homes and condos in Phuket, our Ceramic Nano film offers the best balance of heat rejection, UV protection, and clarity \u2014 it preserves sea views while blocking intense coastal UV. For large west-facing windows, Ceramic UV400 provides extended UV spectrum blocking. For luxury villas and resort properties, our Sputtering Series delivers maximum performance."},
            {"q": "How much will I save on electricity with window film?", "a": "Most Phuket customers see a 20-30% reduction in monthly electricity bills. Properties with large glass areas and heavy AC usage see the biggest savings \u2014 some villa owners in Rawai and Kamala report saving \u0e3f2,000-4,000+ per month during hot season."},
            {"q": "Does window film block natural light?", "a": "Our Ceramic Nano and Ceramic UV400 films maintain high visible light transmission \u2014 rooms stay bright and natural-looking. You'll notice a dramatic reduction in heat and glare without losing light quality. This is especially important for Phuket properties designed to maximise sea views."},
            {"q": "What's the warranty on your window film?", "a": "All films carry a manufacturer-backed warranty: 2 years for Carbon Series, 5 years for Ceramic Nano and Ceramic UV400, and 7 years for Sputtering Series. Covers peeling, bubbling, discoloration, and delamination."},
            {"q": "Is window film effective during Phuket's monsoon season?", "a": "Yes. Film provides year-round benefits \u2014 it blocks solar heat during Phuket's hot season (February-May) and continues blocking UV even on overcast monsoon days (May-October). UV rays penetrate cloud cover, so protection is consistent regardless of weather. Safety films also hold glass in place during monsoon storms."},
            {"q": "Can window film be removed or replaced?", "a": "Yes \u2014 window film is fully removable. If you want to upgrade or replace end-of-life film, we strip the old film and install new. Old film removal costs \u0e3f20-30/sq.ft additional."}
        ],
        "pricing_title": "The Real Cost of Window Tinting in Phuket",
        "pricing_rows": [
            ("Studio / 1-bed condo", "30-60 sq.ft", "\u0e3f2,700-6,600"),
            ("2-bed condo", "60-100 sq.ft", "\u0e3f5,400-11,000"),
            ("3-bed villa", "150-250 sq.ft", "\u0e3f13,500-27,500"),
            ("Large villa (4+ bed)", "250-400 sq.ft", "\u0e3f22,500-44,000+"),
            ("Small office", "100-200 sq.ft", "\u0e3f9,000-22,000"),
        ],
        "reviews_title": "What Phuket Customers Say",
        "reviews_sub": "Real feedback from property owners across Phuket island.",
        "reviews": [
            {"text": "Had our 4-bedroom pool villa in Rawai done with Ceramic Nano. The difference is night and day \u2014 the living room used to be unbearable after 2pm, now we barely touch the AC. Installer was on time, clean, finished in one day. Very happy.", "author": "Michael T.", "meta": "Villa owner \u00b7 Rawai, Phuket \u00b7 Ceramic Nano"},
            {"text": "We manage a 42-room boutique hotel near Kata Beach. JaiDeeClear handled the entire project with zero guest disruption \u2014 worked floor by floor over 3 days. Our monthly electricity dropped noticeably and guests comment on how comfortable the rooms feel.", "author": "Khun Somsak P.", "meta": "Hotel GM \u00b7 Kata, Phuket \u00b7 Sputtering Series"},
            {"text": "My sea-view condo in Patong was like a greenhouse every afternoon. After the Ceramic UV400 install, the temperature dropped immediately and my furniture stopped fading. Took about 4 hours \u2014 quick, professional, no mess.", "author": "Sarah L.", "meta": "Condo owner \u00b7 Patong, Phuket \u00b7 Ceramic UV400"}
        ],
        "areas": ["Patong", "Kata", "Karon", "Rawai", "Chalong", "Kamala", "Surin", "Bang Tao", "Cherng Talay", "Thalang", "Phuket Town", "Kathu", "Wichit", "Rassada", "Cape Panwa", "Laguna", "Nai Harn", "Mai Khao", "Nai Yang", "Ao Po"],
        "nearby_cities": [("Krabi", "krabi"), ("Samui", "samui"), ("Pattaya", "pattaya")],
        "cta_title": "Ready to Tint Your Phuket Property?",
        "cta_sub": "Get a free on-site measurement and no-obligation quote. We serve all areas across Phuket island.",
        "contact_district_placeholder": "e.g. Rawai, Patong, Kamala...",
        "related_locations": [("Bangkok", "bangkok"), ("Krabi", "krabi"), ("Samui", "samui"), ("Pattaya", "pattaya")],
    }


def _city_pattaya():
    return {
        "name": "Pattaya",
        "slug": "pattaya",
        "province": "Chonburi",
        "lat": "12.9236",
        "lng": "100.8825",
        "meta_desc": "Professional window tinting in Pattaya. 99% UV protection, up to 30% energy savings. On-site installation for condos, pool villas & resorts. Free quote — WhatsApp us today.",
        "hero_sub": "Pattaya's beachfront high-rises, pool villa communities, and booming retirement property market face relentless coastal sun year-round. JaiDeeClear delivers professional on-site installation across the city — from Jomtien condos to Pratumnak Hill villas and Na Jomtien resort properties.",
        "stat_uv": "UV 12",
        "stat_uv_label": "Pattaya's Peak UV Index",
        "film_carbon_desc": "Our entry-level option — solid basic UV protection at a budget-friendly price. Ideal for rental condos in Jomtien or Central Pattaya where cost is the primary consideration.",
        "film_nano_desc": "The top choice for Pattaya condos and pool villas. Nano-ceramic technology delivers excellent heat and glare reduction without a metallic appearance — keeping your ocean and bay views pristine.",
        "film_nano_local_note_bold": "Pattaya favourite:",
        "film_nano_local_note": "The go-to choice for Pattaya beachfront condos — blocks intense coastal heat while preserving panoramic sea views that make these properties valuable.",
        "film_uv400_desc": "Enhanced UV400 blocking for maximum skin and furniture protection. Ideal for retirement condos in Wong Amat and pool villas with large west-facing windows catching Pattaya's intense afternoon sun.",
        "film_sputtering_desc": "Premium magnetron-sputtered film for maximum solar control. The preferred choice for luxury villas on Pratumnak Hill, five-star hotels, and commercial properties requiring the highest TSER performance.",
        "quick_guide_premium_label": "Premium / commercial / hotel",
        "process_title": "Professional Installation Across Pattaya",
        "process_sub": "We come to you anywhere in Pattaya and surrounding areas — no need to remove windows or visit a workshop.",
        "process_step1_text": "WhatsApp us or use our online form with your property type and location — whether you're in Jomtien, Pratumnak, or East Pattaya.",
        "process_step2_text": "Our technician visits your property — from a Wong Amat beachfront condo to a Mabprachan pool villa — to measure all windows at no charge.",
        "property_types_subtitle": "From beachfront condos to retirement villas — we tailor every installation to the property.",
        "property_types": [
            {
                "emoji": "\U0001f3e2",
                "title": "Condos & Apartments",
                "subtitle": "Beachfront condos \u00b7 Sea-view apartments \u00b7 Retirement units",
                "desc": "Pattaya's beachfront condos with floor-to-ceiling glass capture stunning sea views but also trap massive heat. We install films that maintain those views while cutting heat gain dramatically — especially important for retirees managing electricity costs.",
                "testimonial": "\"My Jomtien sea-view condo was like an oven every afternoon. After Ceramic Nano, the temperature dropped immediately and my electricity bill went down about \u0e3f2,000/month. Best investment I've made here.\"",
                "testimonial_author": "\u2014 Condo owner, Jomtien"
            },
            {
                "emoji": "\U0001f3e1",
                "title": "Houses & Pool Villas",
                "subtitle": "Pool villas \u00b7 Retirement homes \u00b7 Gated communities",
                "desc": "Pattaya's pool villas in East Pattaya, Mabprachan, and Huay Yai feature large glass areas overlooking gardens and pools. Our films reduce heat without darkening rooms — keeping interiors cool while protecting wooden floors and furniture from UV damage.",
                "testimonial": "\"Three-bedroom pool villa in East Pattaya. They did every window including the pool-facing sliding doors. The house is noticeably cooler and the wooden floors have stopped fading.\"",
                "testimonial_author": "\u2014 Villa owner, East Pattaya"
            },
            {
                "emoji": "\U0001f3e8",
                "title": "Hotels & Resorts",
                "subtitle": "Beach hotels \u00b7 Boutique resorts \u00b7 Serviced residences",
                "desc": "Pattaya's hotel market is fiercely competitive — guest comfort directly impacts reviews and repeat bookings. We handle multi-room installations with zero disruption, using commercial-grade film and flexible scheduling around occupancy.",
                "testimonial": "\"Had our 28-room boutique hotel on Pratumnak done over 4 days. Guests haven't noticed any disruption but they've definitely noticed cooler, more comfortable rooms. Worth every baht.\"",
                "testimonial_author": "\u2014 Hotel owner, Pratumnak Hill"
            }
        ],
        "faq_title": "Common Questions About Window Tinting in Pattaya",
        "faqs": [
            {"q": "How much does window tinting cost in Pattaya?", "a": "Window tinting in Pattaya ranges from \u0e3f50-70/sq.ft for carbon film to \u0e3f155+/sq.ft for premium sputtering film. A typical 2-bedroom condo costs \u0e3f5,400-11,000 depending on glass area and film choice. We provide free on-site measurements and quotes."},
            {"q": "Do you cover all areas of Pattaya?", "a": "Yes \u2014 we serve all Pattaya areas including Jomtien, Na Jomtien, Pratumnak Hill, Wong Amat, Naklua, Central Pattaya, South Pattaya, East Pattaya, Mabprachan, Sattahip, and Bang Saray. Our technicians travel to your property for free measurement and installation."},
            {"q": "How long does window film installation take?", "a": "A typical condo takes 3-5 hours. A pool villa takes one full day. Larger commercial projects or hotel properties take 1-3 days. You can stay in the property during installation."},
            {"q": "Which window film do you recommend for Pattaya?", "a": "For most Pattaya condos and homes, our Ceramic Nano film offers the best balance of heat rejection, UV protection, and clarity \u2014 it preserves sea views while blocking intense coastal heat. For pool villas with west-facing glass, Ceramic UV400 provides extended UV spectrum blocking. For hotels, our Sputtering Series delivers maximum performance."},
            {"q": "How much will I save on electricity with window film?", "a": "Most Pattaya customers see a 20-30% reduction in monthly electricity bills. Beachfront condos and pool villas with heavy AC usage see the biggest savings \u2014 some owners in Jomtien and Pratumnak report saving \u0e3f1,500-3,500+ per month during hot season."},
            {"q": "Does window film block natural light?", "a": "Our Ceramic Nano and Ceramic UV400 films maintain high visible light transmission \u2014 rooms stay bright and natural-looking. You'll notice a dramatic reduction in heat and glare without losing light quality. This is especially important for Pattaya's sea-view condos."},
            {"q": "What's the warranty on your window film?", "a": "All films carry a manufacturer-backed warranty: 2 years for Carbon Series, 5 years for Ceramic Nano and Ceramic UV400, and 7 years for Sputtering Series. Covers peeling, bubbling, discoloration, and delamination."},
            {"q": "Is window film good for retirement properties?", "a": "Absolutely. Many of our Pattaya customers are retirees who want comfortable indoor temperatures without running AC at full blast all day. Film reduces heat gain, lowers electricity costs, and blocks harmful UV \u2014 important health and lifestyle benefits for long-term residents."},
            {"q": "Can window film be removed or replaced?", "a": "Yes \u2014 window film is fully removable. If you want to upgrade or replace end-of-life film, we strip the old film and install new. Old film removal costs \u0e3f20-30/sq.ft additional."}
        ],
        "pricing_title": "The Real Cost of Window Tinting in Pattaya",
        "pricing_rows": [
            ("Studio / 1-bed condo", "30-60 sq.ft", "\u0e3f2,700-6,600"),
            ("2-bed condo", "60-100 sq.ft", "\u0e3f5,400-11,000"),
            ("3-bed pool villa", "150-250 sq.ft", "\u0e3f13,500-27,500"),
            ("Large villa (4+ bed)", "250-400 sq.ft", "\u0e3f22,500-44,000+"),
            ("Small hotel / office", "100-200 sq.ft", "\u0e3f9,000-22,000"),
        ],
        "reviews_title": "What Pattaya Customers Say",
        "reviews_sub": "Real feedback from property owners across Pattaya.",
        "reviews": [
            {"text": "Retired here two years ago and the electricity bills were killing me. Had my Jomtien condo done with Ceramic Nano \u2014 the difference is massive. Rooms are cooler, bills are lower, and I can actually sit near the windows now without sweating.", "author": "David H.", "meta": "Condo owner \u00b7 Jomtien, Pattaya \u00b7 Ceramic Nano"},
            {"text": "Our pool villa in East Pattaya has huge glass doors facing the pool. The afternoon heat was unbearable. After Ceramic UV400 installation, we can enjoy the pool view without the greenhouse effect. Done in one day, very clean work.", "author": "Khun Pornchai W.", "meta": "Villa owner \u00b7 East Pattaya \u00b7 Ceramic UV400"},
            {"text": "We run a small boutique resort near Na Jomtien. JaiDeeClear tinted all guest rooms over 3 days with zero complaints from guests. Our cooling costs dropped and guest comfort scores went up. Win-win.", "author": "Anna M.", "meta": "Resort manager \u00b7 Na Jomtien, Pattaya \u00b7 Sputtering Series"}
        ],
        "areas": ["Jomtien", "Na Jomtien", "Pratumnak Hill", "Wong Amat", "Naklua", "Central Pattaya", "South Pattaya", "East Pattaya", "Mabprachan", "Sattahip", "Bang Saray", "Ban Amphur", "Huay Yai", "Silverlake", "Nong Prue", "North Pattaya", "Khao Chi Chan", "Phra Tamnak", "The Vineyard", "Phoenix Golf"],
        "nearby_cities": [("Bangkok", "bangkok"), ("Hua Hin", "hua-hin"), ("Samui", "samui")],
        "cta_title": "Ready to Tint Your Pattaya Property?",
        "cta_sub": "Get a free on-site measurement and no-obligation quote. We serve all areas across Pattaya.",
        "contact_district_placeholder": "e.g. Jomtien, Pratumnak, East Pattaya...",
        "related_locations": [("Bangkok", "bangkok"), ("Hua Hin", "hua-hin"), ("Samui", "samui"), ("Phuket", "phuket")],
    }


def _city_chiang_rai():
    return {
        "name": "Chiang Rai",
        "slug": "chiang-rai",
        "province": "Chiang Rai",
        "lat": "19.9105",
        "lng": "99.8406",
        "meta_desc": "Professional window tinting in Chiang Rai. 99% UV protection, up to 30% energy savings. On-site installation for houses, villas & boutique resorts. Free quote — WhatsApp us today.",
        "hero_sub": "Chiang Rai's scorching dry season, high-altitude UV exposure, and growing expat villa community make quality window film essential. JaiDeeClear delivers professional on-site installation across the province — from mountain-view homes to boutique resorts and modern condominiums.",
        "stat_uv": "UV 11",
        "stat_uv_label": "Chiang Rai's Peak UV Index",
        "film_carbon_desc": "Our entry-level option — solid basic UV protection at a budget-friendly price. Ideal for rental houses in Mueang district or guesthouses where cost is the primary consideration.",
        "film_nano_desc": "The top choice for Chiang Rai homes and villas. Nano-ceramic technology delivers excellent heat and glare reduction without a metallic appearance — maintaining clear views of the surrounding mountains and rice fields.",
        "film_nano_local_note_bold": "Chiang Rai favourite:",
        "film_nano_local_note": "The go-to choice for expat villas and modern homes — blocks intense dry-season heat while preserving the mountain and countryside views Chiang Rai is known for.",
        "film_uv400_desc": "Enhanced UV400 blocking for maximum skin and furniture protection. Ideal for homes with large picture windows facing west, where the intense afternoon sun accelerates furniture fading and drives up cooling costs.",
        "film_sputtering_desc": "Premium magnetron-sputtered film for maximum solar control. The preferred choice for luxury estates, boutique resorts near the Golden Triangle, and commercial properties requiring the highest TSER performance.",
        "quick_guide_premium_label": "Premium / boutique resort / estate",
        "process_title": "Professional Installation Across Chiang Rai",
        "process_sub": "We come to you anywhere in Chiang Rai province — no need to remove windows or visit a workshop.",
        "process_step1_text": "WhatsApp us or use our online form with your property type and location — whether you're in Mueang, Rimkok, or Mae Sai.",
        "process_step2_text": "Our technician visits your property — from a Rop Wiang family home to a hillside villa near Doi Hang — to measure all windows at no charge.",
        "property_types_subtitle": "From family homes to mountain retreats — we tailor every installation to the property.",
        "property_types": [
            {
                "emoji": "\U0001f3e1",
                "title": "Houses & Villas",
                "subtitle": "Expat villas \u00b7 Family homes \u00b7 Mountain retreats",
                "desc": "Chiang Rai's modern homes and expat villas often feature large glass areas to capture mountain views and natural light. During the hot season (March-May), these become heat traps. Our films cut heat gain while preserving the views that drew you to the north.",
                "testimonial": "\"We built our retirement home in Rimkok with huge windows facing the mountains. Beautiful views, but unbearable heat March through May. After tinting, the house stays comfortable and our electricity bill dropped by about \u0e3f2,500/month.\"",
                "testimonial_author": "\u2014 Homeowner, Rimkok"
            },
            {
                "emoji": "\U0001f3e8",
                "title": "Boutique Hotels & Resorts",
                "subtitle": "Boutique resorts \u00b7 Mountain lodges \u00b7 Guesthouses",
                "desc": "Chiang Rai's tourism boom means more boutique properties competing on guest comfort. We handle installations around guest schedules with zero disruption — important for small properties where every room counts and every review matters.",
                "testimonial": "\"Our 16-room resort near Chiang Saen gets brutally hot in April. Window film has made a real difference in guest comfort — and our TripAdvisor scores reflect it. Professional install, done in 2 days.\"",
                "testimonial_author": "\u2014 Resort owner, Chiang Saen"
            },
            {
                "emoji": "\U0001f3e2",
                "title": "Condos & Apartments",
                "subtitle": "Modern condos \u00b7 Town apartments \u00b7 Serviced residences",
                "desc": "Chiang Rai's newer condo developments in the town centre face significant heat gain from afternoon sun exposure. A single installation — typically done in 3-5 hours — noticeably drops indoor temperatures and protects furnishings from UV fading.",
                "testimonial": "\"Small condo in town but the afternoon sun made it miserable. Four hours of work and the difference is incredible — cooler, more comfortable, and my wooden furniture has stopped discolouring.\"",
                "testimonial_author": "\u2014 Condo owner, Mueang Chiang Rai"
            }
        ],
        "faq_title": "Common Questions About Window Tinting in Chiang Rai",
        "faqs": [
            {"q": "How much does window tinting cost in Chiang Rai?", "a": "Window tinting in Chiang Rai ranges from \u0e3f50-70/sq.ft for carbon film to \u0e3f155+/sq.ft for premium sputtering film. A typical 3-bedroom house costs \u0e3f10,800-27,000 depending on glass area and film choice. We provide free on-site measurements and quotes."},
            {"q": "Do you cover all areas of Chiang Rai province?", "a": "Yes \u2014 we serve all Chiang Rai areas including Mueang, Rop Wiang, Rimkok, Mae Sai, Chiang Saen, Mae Chan, Wiang Pa Pao, and surrounding districts. Our technicians travel to your property for free measurement and installation."},
            {"q": "How long does window film installation take?", "a": "A typical condo or small house takes 3-5 hours. A larger villa takes one full day. Boutique resort properties take 1-3 days. You can stay in the property during installation."},
            {"q": "Which window film do you recommend for Chiang Rai?", "a": "For most homes in Chiang Rai, our Ceramic Nano film offers the best balance of heat rejection, UV protection, and clarity \u2014 it maintains mountain views while blocking intense dry-season heat. For homes with large west-facing windows, Ceramic UV400 provides extended UV spectrum blocking. For resorts and luxury estates, our Sputtering Series delivers maximum performance."},
            {"q": "How much will I save on electricity with window film?", "a": "Most Chiang Rai customers see a 20-30% reduction in monthly electricity bills during hot season. Houses with large glass areas and heavy AC usage see the biggest savings \u2014 some homeowners report saving \u0e3f1,500-3,000+ per month from March to May."},
            {"q": "Does window film help during Chiang Rai's burning season?", "a": "While window film doesn't filter smoke particles (that requires air purifiers), it does block UV rays that penetrate even through haze. During the burning season (February-April), UV levels remain dangerously high despite reduced visibility \u2014 film provides consistent UV protection regardless of air quality."},
            {"q": "What's the warranty on your window film?", "a": "All films carry a manufacturer-backed warranty: 2 years for Carbon Series, 5 years for Ceramic Nano and Ceramic UV400, and 7 years for Sputtering Series. Covers peeling, bubbling, discoloration, and delamination."},
            {"q": "Is Chiang Rai's UV really that strong?", "a": "Yes \u2014 Chiang Rai sits at a higher elevation than Bangkok and receives intense UV exposure, especially during the dry season (November-May). The UV index regularly reaches 11+ during peak hours. Combined with the hot season heat, unprotected glass creates significant indoor temperature problems."},
            {"q": "Can window film be removed or replaced?", "a": "Yes \u2014 window film is fully removable. If you want to upgrade or replace end-of-life film, we strip the old film and install new. Old film removal costs \u0e3f20-30/sq.ft additional."}
        ],
        "pricing_title": "The Real Cost of Window Tinting in Chiang Rai",
        "pricing_rows": [
            ("Condo / apartment", "30-60 sq.ft", "\u0e3f2,700-6,600"),
            ("2-3 bed house", "80-150 sq.ft", "\u0e3f7,200-16,500"),
            ("3-bed villa", "150-250 sq.ft", "\u0e3f13,500-27,500"),
            ("Large estate (4+ bed)", "250-400 sq.ft", "\u0e3f22,500-44,000+"),
            ("Boutique resort / office", "100-200 sq.ft", "\u0e3f9,000-22,000"),
        ],
        "reviews_title": "What Chiang Rai Customers Say",
        "reviews_sub": "Real feedback from property owners across Chiang Rai.",
        "reviews": [
            {"text": "Built our dream retirement home near Rimkok with panoramic mountain views. The heat in April was unbearable until we had Ceramic Nano installed. Now the house is comfortable year-round and we've cut our electricity usage significantly.", "author": "Richard & Sue B.", "meta": "Homeowners \u00b7 Rimkok, Chiang Rai \u00b7 Ceramic Nano"},
            {"text": "Our boutique resort near the Golden Triangle needed a solution for guest comfort during hot season. JaiDeeClear installed Sputtering film across 16 rooms in just 2 days. Guests are happier and our energy costs dropped.", "author": "Khun Arunee T.", "meta": "Resort owner \u00b7 Chiang Saen, Chiang Rai \u00b7 Sputtering Series"},
            {"text": "Small house in Mueang district with afternoon sun hammering the living room. Ceramic UV400 made an immediate difference \u2014 no more glare, noticeably cooler, and my teak furniture has stopped fading. Installation took half a day.", "author": "Khun Somchai K.", "meta": "Homeowner \u00b7 Mueang, Chiang Rai \u00b7 Ceramic UV400"}
        ],
        "areas": ["Mueang Chiang Rai", "Rop Wiang", "Rimkok", "Wiang Chai", "Mae Sai", "Chiang Saen", "Mae Chan", "Wiang Pa Pao", "Mae Suai", "Thoeng", "Phan", "Mae Fah Luang", "Ban Du", "Tha Sud", "Doi Hang", "Sansai", "Wiang Chiang Rai", "Mae Lao", "Rob Wiang"],
        "nearby_cities": [("Bangkok", "bangkok"), ("Phuket", "phuket")],
        "cta_title": "Ready to Tint Your Chiang Rai Property?",
        "cta_sub": "Get a free on-site measurement and no-obligation quote. We serve all areas across Chiang Rai province.",
        "contact_district_placeholder": "e.g. Mueang, Rimkok, Mae Sai...",
        "related_locations": [("Bangkok", "bangkok"), ("Phuket", "phuket"), ("Pattaya", "pattaya")],
    }


def _city_samui():
    return {
        "name": "Koh Samui",
        "slug": "samui",
        "province": "Surat Thani",
        "lat": "9.5120",
        "lng": "100.0136",
        "meta_desc": "Professional window tinting in Koh Samui. 99% UV protection, up to 30% energy savings. On-site installation for villas, resorts & condos. Free quote — WhatsApp us today.",
        "hero_sub": "Koh Samui's tropical island climate, fierce Gulf of Thailand UV, and luxury villa market demand premium window film. JaiDeeClear delivers professional on-site installation across the island — from Chaweng beachfront condos to Bophut hillside villas and boutique resort properties.",
        "stat_uv": "UV 12+",
        "stat_uv_label": "Samui's Peak UV Index",
        "film_carbon_desc": "Our entry-level option — solid basic UV protection at a budget-friendly price. Ideal for rental bungalows in Chaweng or Lamai where cost is the primary consideration.",
        "film_nano_desc": "The top choice for Samui villas and condos. Nano-ceramic technology delivers excellent heat and glare reduction without a metallic appearance — preserving your Gulf of Thailand sea views.",
        "film_nano_local_note_bold": "Samui favourite:",
        "film_nano_local_note": "The go-to choice for Samui pool villas — blocks fierce tropical heat while preserving the panoramic ocean views that define island living.",
        "film_uv400_desc": "Enhanced UV400 blocking for maximum skin and furniture protection. Ideal for villas in Bophut and Maenam with large west-facing windows catching the intense Gulf sunset exposure.",
        "film_sputtering_desc": "Premium magnetron-sputtered film for maximum solar control. The preferred choice for luxury beachfront estates, five-star resorts, and high-end commercial properties on Samui requiring the highest TSER performance.",
        "quick_guide_premium_label": "Premium / luxury resort / estate",
        "process_title": "Professional Installation Across Koh Samui",
        "process_sub": "We come to you anywhere on Samui — no need to remove windows or visit a workshop.",
        "process_step1_text": "WhatsApp us or use our online form with your property type and location — whether you're in Chaweng, Bophut, or Lamai.",
        "process_step2_text": "Our technician visits your property — from a Fisherman's Village townhouse to a hillside villa in Plai Laem — to measure all windows at no charge.",
        "property_types_subtitle": "From beach villas to island resorts — we tailor every installation to the property.",
        "property_types": [
            {
                "emoji": "\U0001f3e1",
                "title": "Villas & Pool Villas",
                "subtitle": "Beachfront villas \u00b7 Hillside pool villas \u00b7 Airbnb properties",
                "desc": "Samui's luxury villas are designed around ocean views with expansive glass walls. That glass captures stunning scenery but also traps extreme tropical heat. We install films that preserve those views while cutting heat gain dramatically — essential for both comfort and electricity costs.",
                "testimonial": "\"Our hillside pool villa in Bophut has floor-to-ceiling glass on three sides. The AC was running non-stop. After Ceramic Nano, we save around \u0e3f4,000/month on electricity and the villa is actually comfortable without constant AC.\"",
                "testimonial_author": "\u2014 Villa owner, Bophut"
            },
            {
                "emoji": "\U0001f3e8",
                "title": "Boutique Hotels & Resorts",
                "subtitle": "Beach resorts \u00b7 Boutique hotels \u00b7 Wellness retreats",
                "desc": "On an island where guest experience drives bookings, room comfort is everything. We handle multi-room installations with zero guest disruption — working around occupancy schedules with commercial-grade film designed for Samui's harsh tropical conditions.",
                "testimonial": "\"We run a 22-room beachfront boutique hotel in Chaweng. JaiDeeClear did the entire property in 3 days with no guest complaints. Rooms are cooler, guests are happier, and our cooling costs have dropped measurably.\"",
                "testimonial_author": "\u2014 Hotel manager, Chaweng"
            },
            {
                "emoji": "\U0001f3e2",
                "title": "Condos & Apartments",
                "subtitle": "Sea-view condos \u00b7 Investment units \u00b7 Long-stay apartments",
                "desc": "Samui's condo developments in Chaweng and Bophut feature large glass balcony doors to maximise views. West and south-facing units suffer from intense afternoon heat. A single installation — typically done in 3-5 hours — makes a dramatic difference in comfort and energy costs.",
                "testimonial": "\"Sea-view condo in Chaweng Noi. The balcony glass turned my apartment into an oven every afternoon. After installation, I can actually enjoy the view without melting. Done in under 4 hours.\"",
                "testimonial_author": "\u2014 Condo owner, Chaweng Noi"
            }
        ],
        "faq_title": "Common Questions About Window Tinting in Koh Samui",
        "faqs": [
            {"q": "How much does window tinting cost in Koh Samui?", "a": "Window tinting in Samui ranges from \u0e3f50-70/sq.ft for carbon film to \u0e3f155+/sq.ft for premium sputtering film. A typical 3-bedroom pool villa costs \u0e3f15,000-45,000 depending on glass area and film choice. We provide free on-site measurements and quotes."},
            {"q": "Do you cover all areas of Koh Samui?", "a": "Yes \u2014 we serve the entire island including Chaweng, Lamai, Bophut, Fisherman's Village, Maenam, Nathon, Lipa Noi, Taling Ngam, Bangrak, Choeng Mon, and all surrounding areas. Our technicians travel to your property for free measurement and installation."},
            {"q": "How long does window film installation take?", "a": "A typical condo takes 3-5 hours. A pool villa takes one full day. Larger resort properties take 1-3 days. You can stay in the property during installation."},
            {"q": "Which window film do you recommend for Samui?", "a": "For most Samui villas and condos, our Ceramic Nano film offers the best balance of heat rejection, UV protection, and clarity \u2014 it preserves sea views while blocking fierce island UV. For villas with west-facing glass, Ceramic UV400 provides extended UV spectrum blocking. For resorts, our Sputtering Series delivers maximum performance."},
            {"q": "How much will I save on electricity with window film?", "a": "Most Samui customers see a 20-30% reduction in monthly electricity bills. Pool villas with heavy AC usage see the biggest savings \u2014 some villa owners in Bophut and Chaweng report saving \u0e3f2,500-4,500+ per month during hot season."},
            {"q": "Does window film block natural light?", "a": "Our Ceramic Nano and Ceramic UV400 films maintain high visible light transmission \u2014 rooms stay bright and natural-looking. You'll notice a dramatic reduction in heat and glare without losing light quality. This is critical for Samui properties built around ocean views."},
            {"q": "What's the warranty on your window film?", "a": "All films carry a manufacturer-backed warranty: 2 years for Carbon Series, 5 years for Ceramic Nano and Ceramic UV400, and 7 years for Sputtering Series. Covers peeling, bubbling, discoloration, and delamination."},
            {"q": "Does the salt air affect window film durability?", "a": "Our films are installed on the interior surface of glass, so they are not exposed to salt air. The adhesive and film materials are designed for tropical climates and are unaffected by coastal humidity. Exterior glass cleaning can be done normally without damaging the film."},
            {"q": "Can window film be removed or replaced?", "a": "Yes \u2014 window film is fully removable. If you want to upgrade or replace end-of-life film, we strip the old film and install new. Old film removal costs \u0e3f20-30/sq.ft additional."}
        ],
        "pricing_title": "The Real Cost of Window Tinting in Koh Samui",
        "pricing_rows": [
            ("Studio / 1-bed condo", "30-60 sq.ft", "\u0e3f2,700-6,600"),
            ("2-bed condo / bungalow", "60-100 sq.ft", "\u0e3f5,400-11,000"),
            ("3-bed pool villa", "150-250 sq.ft", "\u0e3f13,500-27,500"),
            ("Luxury villa (4+ bed)", "250-400 sq.ft", "\u0e3f22,500-44,000+"),
            ("Boutique resort / office", "100-200 sq.ft", "\u0e3f9,000-22,000"),
        ],
        "reviews_title": "What Koh Samui Customers Say",
        "reviews_sub": "Real feedback from property owners across Koh Samui.",
        "reviews": [
            {"text": "Our pool villa in Bophut has massive glass walls facing the Gulf. The heat was insane and our electricity bill was over \u0e3f15,000/month. After Ceramic Nano installation, the bill dropped to about \u0e3f11,000 and the villa is actually comfortable. Brilliant work.", "author": "Mark & Lisa T.", "meta": "Villa owners \u00b7 Bophut, Koh Samui \u00b7 Ceramic Nano"},
            {"text": "We manage a wellness resort in Taling Ngam. JaiDeeClear tinted all guest suites and the yoga pavilion. The improvement in guest comfort has been immediate and our energy costs are down about 25%. Very professional team.", "author": "Khun Pim S.", "meta": "Resort manager \u00b7 Taling Ngam, Koh Samui \u00b7 Sputtering Series"},
            {"text": "Beachfront condo in Lamai \u2014 afternoon sun was making the place unlivable. Ceramic UV400 solved the problem completely. Quick install, clean work, and my furniture has stopped fading. Should have done this years ago.", "author": "Steve C.", "meta": "Condo owner \u00b7 Lamai, Koh Samui \u00b7 Ceramic UV400"}
        ],
        "areas": ["Chaweng", "Lamai", "Bophut", "Fisherman's Village", "Maenam", "Nathon", "Lipa Noi", "Taling Ngam", "Bangrak", "Choeng Mon", "Hua Thanon", "Plai Laem", "Bang Makham", "Namuang", "Ang Thong"],
        "nearby_cities": [("Phuket", "phuket"), ("Krabi", "krabi"), ("Pattaya", "pattaya")],
        "cta_title": "Ready to Tint Your Samui Property?",
        "cta_sub": "Get a free on-site measurement and no-obligation quote. We serve all areas across Koh Samui.",
        "contact_district_placeholder": "e.g. Chaweng, Bophut, Lamai...",
        "related_locations": [("Phuket", "phuket"), ("Krabi", "krabi"), ("Pattaya", "pattaya"), ("Bangkok", "bangkok")],
    }


def _city_krabi():
    return {
        "name": "Krabi",
        "slug": "krabi",
        "province": "Krabi",
        "lat": "8.0863",
        "lng": "98.9063",
        "meta_desc": "Professional window tinting in Krabi. 99% UV protection, up to 30% energy savings. On-site installation for villas, resorts & homes. Free quote — WhatsApp us today.",
        "hero_sub": "Krabi's intense Andaman coast sun, growing resort development, and year-round tropical UV exposure make quality window film essential. JaiDeeClear delivers professional on-site installation across the province — from Ao Nang beachfront villas to Ko Lanta resort properties and Krabi Town homes.",
        "stat_uv": "UV 12+",
        "stat_uv_label": "Krabi's Peak UV Index",
        "film_carbon_desc": "Our entry-level option — solid basic UV protection at a budget-friendly price. Ideal for guesthouses in Ao Nang or rental bungalows on Ko Lanta where cost is the primary consideration.",
        "film_nano_desc": "The top choice for Krabi villas and resort properties. Nano-ceramic technology delivers excellent heat and glare reduction without a metallic appearance — preserving your stunning limestone karst and sea views.",
        "film_nano_local_note_bold": "Krabi favourite:",
        "film_nano_local_note": "The go-to choice for Krabi beachfront villas — blocks intense Andaman UV while preserving the spectacular natural scenery that makes Krabi properties special.",
        "film_uv400_desc": "Enhanced UV400 blocking for maximum skin and furniture protection. Ideal for villas in Klong Muang and Tubkaek with large west-facing windows catching the intense Andaman sunset.",
        "film_sputtering_desc": "Premium magnetron-sputtered film for maximum solar control. The preferred choice for luxury resort developments, beachfront estates, and commercial properties in Krabi requiring the highest TSER performance.",
        "quick_guide_premium_label": "Premium / resort / beachfront estate",
        "process_title": "Professional Installation Across Krabi",
        "process_sub": "We come to you anywhere in Krabi province — no need to remove windows or visit a workshop.",
        "process_step1_text": "WhatsApp us or use our online form with your property type and location — whether you're in Ao Nang, Klong Muang, or Ko Lanta.",
        "process_step2_text": "Our technician visits your property — from a Railay beachfront villa to a Krabi Town townhouse — to measure all windows at no charge.",
        "property_types_subtitle": "From beachfront resorts to island villas — we tailor every installation to the property.",
        "property_types": [
            {
                "emoji": "\U0001f3e8",
                "title": "Resorts & Hotels",
                "subtitle": "Beach resorts \u00b7 Island hotels \u00b7 Eco lodges",
                "desc": "Krabi's resort market thrives on the stunning natural environment — but the same sun that draws tourists also creates intense heat in guest rooms. We handle multi-room installations with zero disruption, using commercial-grade film designed for tropical coastal conditions.",
                "testimonial": "\"Our 30-room resort in Klong Muang was spending a fortune on cooling. Window film reduced our electricity costs by about 22% and guest comfort reviews have improved noticeably. Professional team, clean install.\"",
                "testimonial_author": "\u2014 Resort GM, Klong Muang"
            },
            {
                "emoji": "\U0001f3e1",
                "title": "Villas & Pool Homes",
                "subtitle": "Pool villas \u00b7 Beachfront homes \u00b7 Holiday rentals",
                "desc": "Krabi's villas feature expansive glass to capture the dramatic limestone scenery and ocean views. Our films reject heat without compromising those views — essential for both owner comfort and guest satisfaction in the rental market.",
                "testimonial": "\"Beautiful pool villa in Tubkaek but the west-facing glass was a disaster every afternoon. Ceramic Nano solved it completely \u2014 cool rooms, preserved views, and our Airbnb guests love the comfort.\"",
                "testimonial_author": "\u2014 Villa owner, Tubkaek"
            },
            {
                "emoji": "\U0001f3e0",
                "title": "Houses & Condos",
                "subtitle": "Family homes \u00b7 Town condos \u00b7 Shophouses",
                "desc": "Krabi Town and surrounding areas are growing rapidly with modern homes and condominiums. Afternoon heat gain through glass is a universal problem. A single installation noticeably drops temperatures and reduces electricity costs — practical benefits for everyday living.",
                "testimonial": "\"Our family home in Krabi Town had terrible afternoon heat in the upstairs bedrooms. After tinting, the kids' rooms are comfortable and we've cut our AC runtime significantly. Great value.\"",
                "testimonial_author": "\u2014 Homeowner, Krabi Town"
            }
        ],
        "faq_title": "Common Questions About Window Tinting in Krabi",
        "faqs": [
            {"q": "How much does window tinting cost in Krabi?", "a": "Window tinting in Krabi ranges from \u0e3f50-70/sq.ft for carbon film to \u0e3f155+/sq.ft for premium sputtering film. A typical 3-bedroom villa costs \u0e3f13,500-35,000 depending on glass area and film choice. We provide free on-site measurements and quotes."},
            {"q": "Do you cover all areas of Krabi province?", "a": "Yes \u2014 we serve all Krabi areas including Ao Nang, Klong Muang, Tubkaek, Krabi Town, Ko Lanta, Railay, Nong Thale, Sai Thai, Pak Nam, and surrounding districts. Our technicians travel to your property for free measurement and installation."},
            {"q": "How long does window film installation take?", "a": "A typical condo or small house takes 3-5 hours. A villa takes one full day. Larger resort properties take 1-3 days. You can stay in the property during installation."},
            {"q": "Which window film do you recommend for Krabi?", "a": "For most Krabi homes and villas, our Ceramic Nano film offers the best balance of heat rejection, UV protection, and clarity \u2014 it preserves the stunning natural views while blocking intense Andaman UV. For west-facing windows, Ceramic UV400 provides extended UV blocking. For resorts, our Sputtering Series delivers maximum performance."},
            {"q": "How much will I save on electricity with window film?", "a": "Most Krabi customers see a 20-30% reduction in monthly electricity bills. Properties with large glass areas and heavy AC usage see the biggest savings \u2014 some resort and villa owners report saving \u0e3f2,000-4,000+ per month during hot season."},
            {"q": "Does window film block natural light?", "a": "Our Ceramic Nano and Ceramic UV400 films maintain high visible light transmission \u2014 rooms stay bright and natural-looking. You'll notice a dramatic reduction in heat and glare without losing light quality. This is critical for Krabi properties designed around natural scenery views."},
            {"q": "What's the warranty on your window film?", "a": "All films carry a manufacturer-backed warranty: 2 years for Carbon Series, 5 years for Ceramic Nano and Ceramic UV400, and 7 years for Sputtering Series. Covers peeling, bubbling, discoloration, and delamination."},
            {"q": "Do you service Ko Lanta?", "a": "Yes \u2014 we service Ko Lanta as well as all mainland Krabi areas. For Ko Lanta projects, we schedule installation trips to handle multiple properties efficiently. Contact us for Ko Lanta scheduling and availability."},
            {"q": "Can window film be removed or replaced?", "a": "Yes \u2014 window film is fully removable. If you want to upgrade or replace end-of-life film, we strip the old film and install new. Old film removal costs \u0e3f20-30/sq.ft additional."}
        ],
        "pricing_title": "The Real Cost of Window Tinting in Krabi",
        "pricing_rows": [
            ("Condo / apartment", "30-60 sq.ft", "\u0e3f2,700-6,600"),
            ("2-3 bed house", "80-150 sq.ft", "\u0e3f7,200-16,500"),
            ("3-bed pool villa", "150-250 sq.ft", "\u0e3f13,500-27,500"),
            ("Large villa / estate", "250-400 sq.ft", "\u0e3f22,500-44,000+"),
            ("Resort / commercial", "100-200 sq.ft", "\u0e3f9,000-22,000"),
        ],
        "reviews_title": "What Krabi Customers Say",
        "reviews_sub": "Real feedback from property owners across Krabi.",
        "reviews": [
            {"text": "Our beachfront resort in Klong Muang had massive cooling costs from all the glass. JaiDeeClear installed Sputtering film across all guest rooms and common areas over 4 days. Our electricity dropped about 20% and guest comfort scores improved immediately.", "author": "Khun Wichai P.", "meta": "Resort owner \u00b7 Klong Muang, Krabi \u00b7 Sputtering Series"},
            {"text": "Pool villa in Tubkaek with stunning views but brutal afternoon heat. Ceramic Nano preserved the views perfectly while making the house actually liveable after lunch. Installation was clean and professional \u2014 done in one day.", "author": "Emma & Paul D.", "meta": "Villa owners \u00b7 Tubkaek, Krabi \u00b7 Ceramic Nano"},
            {"text": "Small house in Krabi Town. Nothing fancy but the heat was a real problem. Carbon film brought the cost down and made a noticeable difference in comfort. Good value for the price \u2014 installer was friendly and efficient.", "author": "Khun Naree W.", "meta": "Homeowner \u00b7 Krabi Town \u00b7 Carbon Series"}
        ],
        "areas": ["Ao Nang", "Railay", "Klong Muang", "Tubkaek", "Krabi Town", "Ao Nam Mao", "Ko Lanta", "Nong Thale", "Sai Thai", "Pak Nam", "Khlong Thom", "Nuea Khlong", "Plai Phraya", "Khao Phanom", "Muang Krabi", "Ao Leuk", "Khao Thong", "Tab Kaek", "Klong Jilad"],
        "nearby_cities": [("Phuket", "phuket"), ("Samui", "samui")],
        "cta_title": "Ready to Tint Your Krabi Property?",
        "cta_sub": "Get a free on-site measurement and no-obligation quote. We serve all areas across Krabi province.",
        "contact_district_placeholder": "e.g. Ao Nang, Klong Muang, Krabi Town...",
        "related_locations": [("Phuket", "phuket"), ("Samui", "samui"), ("Bangkok", "bangkok")],
    }


def _city_hua_hin():
    return {
        "name": "Hua Hin",
        "slug": "hua-hin",
        "province": "Prachuap Khiri Khan",
        "lat": "12.5684",
        "lng": "99.9577",
        "meta_desc": "Professional window tinting in Hua Hin. 99% UV protection, up to 30% energy savings. On-site installation for condos, villas & retirement homes. Free quote — WhatsApp us today.",
        "hero_sub": "Hua Hin's year-round coastal sun, large retirement community, and growing golf villa developments demand quality window film. JaiDeeClear delivers professional on-site installation across the district — from beachfront condos to Black Mountain pool villas and Pranburi holiday homes.",
        "stat_uv": "UV 12",
        "stat_uv_label": "Hua Hin's Peak UV Index",
        "film_carbon_desc": "Our entry-level option — solid basic UV protection at a budget-friendly price. Ideal for rental condos near the beach or holiday apartments where cost is the primary consideration.",
        "film_nano_desc": "The top choice for Hua Hin condos and retirement homes. Nano-ceramic technology delivers excellent heat and glare reduction without a metallic appearance — keeping your sea and mountain views crystal clear.",
        "film_nano_local_note_bold": "Hua Hin favourite:",
        "film_nano_local_note": "The go-to choice for Hua Hin retirement condos and villas — blocks intense coastal heat while maintaining the bright, airy feel that makes these properties comfortable for daily living.",
        "film_uv400_desc": "Enhanced UV400 blocking for maximum skin and furniture protection. Ideal for golf community villas and beachfront condos with large west-facing windows catching Hua Hin's intense afternoon Gulf sun.",
        "film_sputtering_desc": "Premium magnetron-sputtered film for maximum solar control. The preferred choice for luxury beachfront estates, five-star hotel properties, and large commercial buildings in Hua Hin requiring the highest TSER performance.",
        "quick_guide_premium_label": "Premium / commercial / luxury estate",
        "process_title": "Professional Installation Across Hua Hin",
        "process_sub": "We come to you anywhere in Hua Hin and surrounding areas — no need to remove windows or visit a workshop.",
        "process_step1_text": "WhatsApp us or use our online form with your property type and location — whether you're in Hua Hin Town, Khao Takiab, or Pranburi.",
        "process_step2_text": "Our technician visits your property — from a Cha-am beachfront condo to a Black Mountain golf villa — to measure all windows at no charge.",
        "property_types_subtitle": "From retirement condos to golf villas — we tailor every installation to the property.",
        "property_types": [
            {
                "emoji": "\U0001f3e2",
                "title": "Condos & Retirement Homes",
                "subtitle": "Beachfront condos \u00b7 Retirement apartments \u00b7 Long-stay units",
                "desc": "Hua Hin's retirement condo market is built around comfort and lifestyle. Many units have large glass balcony doors facing the Gulf — beautiful but punishing in the afternoon heat. We install films that maintain the views while dramatically reducing heat and protecting furniture from UV fading.",
                "testimonial": "\"Retired to Hua Hin three years ago. My beachfront condo was gorgeous but the afternoon heat was terrible. After Ceramic Nano, my electricity dropped by about \u0e3f2,000/month and I can actually enjoy the sea view all day.\"",
                "testimonial_author": "\u2014 Condo owner, Khao Takiab"
            },
            {
                "emoji": "\U0001f3e1",
                "title": "Villas & Pool Homes",
                "subtitle": "Golf villas \u00b7 Pool homes \u00b7 Holiday houses",
                "desc": "Hua Hin's golf community villas around Black Mountain, Palm Hills, and Banyan feature large glass areas overlooking fairways and gardens. Our films cut heat gain significantly while preserving the bright, open feel these properties are designed for.",
                "testimonial": "\"Our golf villa near Black Mountain has huge windows on all sides. The AC was running 18 hours a day. After window film, we cut that to about 12 hours and the rooms are still cooler than before. Excellent investment.\"",
                "testimonial_author": "\u2014 Villa owner, Black Mountain"
            },
            {
                "emoji": "\U0001f3e8",
                "title": "Hotels & Resorts",
                "subtitle": "Beach hotels \u00b7 Boutique resorts \u00b7 Serviced residences",
                "desc": "Hua Hin's hotel market caters to Bangkok weekenders and long-stay tourists who expect premium comfort. We handle multi-room installations with zero disruption — working floor by floor with commercial-grade film designed for coastal tropical conditions.",
                "testimonial": "\"We manage a 35-room beachfront hotel. JaiDeeClear tinted every guest room and the lobby over 4 days. No guest complaints, measurable cooling improvement, and our monthly electricity is down about 18%.\"",
                "testimonial_author": "\u2014 Hotel manager, Hua Hin Beach"
            }
        ],
        "faq_title": "Common Questions About Window Tinting in Hua Hin",
        "faqs": [
            {"q": "How much does window tinting cost in Hua Hin?", "a": "Window tinting in Hua Hin ranges from \u0e3f50-70/sq.ft for carbon film to \u0e3f155+/sq.ft for premium sputtering film. A typical 2-bedroom condo costs \u0e3f5,400-11,000 depending on glass area and film choice. We provide free on-site measurements and quotes."},
            {"q": "Do you cover all areas of Hua Hin?", "a": "Yes \u2014 we serve all Hua Hin areas including Hua Hin Town, Khao Takiab, Pranburi, Cha-am, Nong Kae, Hin Lek Fai, Bo Fai, Sam Roi Yot, Black Mountain, Palm Hills, and surrounding areas. Our technicians travel to your property for free measurement and installation."},
            {"q": "How long does window film installation take?", "a": "A typical condo takes 3-5 hours. A villa takes one full day. Larger hotel or commercial properties take 1-3 days. You can stay in the property during installation."},
            {"q": "Which window film do you recommend for Hua Hin?", "a": "For most Hua Hin condos and homes, our Ceramic Nano film offers the best balance of heat rejection, UV protection, and clarity \u2014 it maintains sea views while blocking intense coastal heat. For golf villas with west-facing glass, Ceramic UV400 provides extended UV blocking. For hotels and luxury estates, our Sputtering Series delivers maximum performance."},
            {"q": "How much will I save on electricity with window film?", "a": "Most Hua Hin customers see a 20-30% reduction in monthly electricity bills. Beachfront condos and pool villas with heavy AC usage see the biggest savings \u2014 some owners in Khao Takiab and Pranburi report saving \u0e3f1,500-3,500+ per month during hot season."},
            {"q": "Does window film block natural light?", "a": "Our Ceramic Nano and Ceramic UV400 films maintain high visible light transmission \u2014 rooms stay bright and natural-looking. You'll notice a dramatic reduction in heat and glare without losing light quality. This is especially important for Hua Hin retirement condos where a bright, comfortable living space matters most."},
            {"q": "What's the warranty on your window film?", "a": "All films carry a manufacturer-backed warranty: 2 years for Carbon Series, 5 years for Ceramic Nano and Ceramic UV400, and 7 years for Sputtering Series. Covers peeling, bubbling, discoloration, and delamination."},
            {"q": "Is window film a good investment for retirement properties?", "a": "Absolutely. Many Hua Hin retirees tell us film is one of the best investments they've made. It reduces electricity costs, improves daily comfort without constant AC, blocks harmful UV for health-conscious residents, and protects furniture from fading. The energy savings alone often pay for the installation within 1-2 years."},
            {"q": "Can window film be removed or replaced?", "a": "Yes \u2014 window film is fully removable. If you want to upgrade or replace end-of-life film, we strip the old film and install new. Old film removal costs \u0e3f20-30/sq.ft additional."}
        ],
        "pricing_title": "The Real Cost of Window Tinting in Hua Hin",
        "pricing_rows": [
            ("Studio / 1-bed condo", "30-60 sq.ft", "\u0e3f2,700-6,600"),
            ("2-bed condo", "60-100 sq.ft", "\u0e3f5,400-11,000"),
            ("3-bed pool villa", "150-250 sq.ft", "\u0e3f13,500-27,500"),
            ("Large villa (4+ bed)", "250-400 sq.ft", "\u0e3f22,500-44,000+"),
            ("Hotel / commercial", "100-200 sq.ft", "\u0e3f9,000-22,000"),
        ],
        "reviews_title": "What Hua Hin Customers Say",
        "reviews_sub": "Real feedback from property owners across Hua Hin.",
        "reviews": [
            {"text": "Retirement condo near Khao Takiab with big sea-view windows. The afternoon heat was a daily battle. Ceramic Nano changed everything \u2014 cooler rooms, lower electricity, and I can sit by the window with my coffee without overheating. Best money I've spent in Hua Hin.", "author": "John & Margaret P.", "meta": "Condo owners \u00b7 Khao Takiab, Hua Hin \u00b7 Ceramic Nano"},
            {"text": "Our golf villa near Palm Hills has massive sliding glass doors. The heat gain was insane and our electricity was sky-high. After Ceramic UV400, the house is noticeably cooler and we've cut our monthly bill by about \u0e3f3,000. Very professional installation.", "author": "Khun Preecha L.", "meta": "Villa owner \u00b7 Palm Hills, Hua Hin \u00b7 Ceramic UV400"},
            {"text": "Small boutique hotel on the beach road. Had all 20 rooms done with Sputtering film over a long weekend. Zero guest disruption, cleaner rooms from less dust near windows, and measurable savings on cooling. Highly recommend.", "author": "Andrew W.", "meta": "Hotel owner \u00b7 Hua Hin Beach \u00b7 Sputtering Series"}
        ],
        "areas": ["Hua Hin Town", "Khao Takiab", "Pranburi", "Pak Nam Pran", "Nong Kae", "Hin Lek Fai", "Bo Fai", "Cha-am", "Sam Roi Yot", "Khao Tao", "Black Mountain", "Palm Hills", "The Bluffs", "Banyan", "Nong Plub", "Thap Tai", "Soi 88", "Soi 94", "Soi 70", "Kao Tao"],
        "nearby_cities": [("Bangkok", "bangkok"), ("Pattaya", "pattaya")],
        "cta_title": "Ready to Tint Your Hua Hin Property?",
        "cta_sub": "Get a free on-site measurement and no-obligation quote. We serve all areas across Hua Hin and surrounds.",
        "contact_district_placeholder": "e.g. Hua Hin Town, Khao Takiab, Pranburi...",
        "related_locations": [("Bangkok", "bangkok"), ("Pattaya", "pattaya"), ("Phuket", "phuket")],
    }


# ══════════════════════════════════════════════
# CSS STYLES (from Phuket gold standard)
# ══════════════════════════════════════════════
def get_css():
    return """
        /* NAV BAR */
        header { position: sticky; top: 0; background: rgba(255, 255, 255, 0.97); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-bottom: 1px solid #e5e5e7; z-index: 1000; }
        .header-content { display: flex; justify-content: space-between; align-items: center; max-width: 1100px; margin: 0 auto; padding: 0 32px; height: 72px; }
        .logo-container { display: flex; align-items: center; }
        .logo-container a { display: flex; align-items: center; }
        .header-nav { display: flex; align-items: center; gap: 36px; }
        .nav-link { font-size: 15px; font-weight: 500; color: #1d1d1f; text-decoration: none; letter-spacing: -0.01em; transition: color 0.2s ease; white-space: nowrap; }
        .nav-link:hover { color: #f9a500; }
        .nav-link.active { color: #f9a500; font-weight: 600; }
        .whatsapp-btn { display: inline-flex; align-items: center; gap: 8px; background: #25D366; color: white; padding: 10px 22px; border-radius: 980px; text-decoration: none; font-size: 14px; font-weight: 600; white-space: nowrap; transition: all 0.2s ease; box-shadow: 0 2px 8px rgba(37,211,102,0.25); }
        .whatsapp-btn:hover { background: #20BA5A; transform: translateY(-1px); box-shadow: 0 4px 14px rgba(37,211,102,0.35); }
        .whatsapp-icon { width: 18px; height: 18px; flex-shrink: 0; }
        .hamburger { display: none; flex-direction: column; justify-content: center; align-items: center; gap: 5px; width: 40px; height: 40px; background: none; border: none; cursor: pointer; padding: 4px; border-radius: 8px; transition: background 0.2s; z-index: 1100; }
        .hamburger:hover { background: #f5f5f7; }
        .hamburger span { display: block; width: 22px; height: 2px; background: #1d1d1f; border-radius: 2px; transition: all 0.3s ease; transform-origin: center; }
        .hamburger.open span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
        .hamburger.open span:nth-child(2) { opacity: 0; transform: scaleX(0); }
        .hamburger.open span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }
        .mobile-menu { display: none; position: fixed; top: 72px; left: 0; right: 0; background: rgba(255,255,255,0.98); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-bottom: 1px solid #e5e5e7; padding: 20px 24px 28px; flex-direction: column; gap: 4px; z-index: 999; box-shadow: 0 8px 32px rgba(0,0,0,0.08); }
        .mobile-menu.open { display: flex; }
        .mobile-menu .nav-link { font-size: 17px; font-weight: 500; padding: 14px 0; border-bottom: 1px solid #f0f0f2; color: #1d1d1f; }
        .mobile-menu .nav-link:last-of-type { border-bottom: none; }
        .mobile-menu .whatsapp-btn { margin-top: 12px; justify-content: center; padding: 14px 22px; font-size: 15px; }
        @media (max-width: 768px) {
            .header-content { padding: 0 20px; height: 64px; }
            .header-nav { display: none; }
            .hamburger { display: flex; }
            .mobile-menu { top: 64px; }
        }

        /* BASE */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #ffffff; color: #1d1d1f; line-height: 1.6; -webkit-font-smoothing: antialiased; }
        .container { max-width: 980px; margin: 0 auto; padding: 0 22px; }

        /* BREADCRUMB */
        .breadcrumb { padding: 14px 0; background: #f5f5f7; border-bottom: 1px solid #e5e5e7; }
        .breadcrumb-list { list-style: none; display: flex; align-items: center; gap: 8px; font-size: 13px; color: #86868b; }
        .breadcrumb-list a { color: #6e6e73; text-decoration: none; transition: color 0.2s; }
        .breadcrumb-list a:hover { color: #f9a500; }
        .breadcrumb-list .separator { color: #c7c7cc; }
        .breadcrumb-list .current { color: #1d1d1f; font-weight: 500; }

        /* HERO */
        .hero { background: linear-gradient(135deg, #1d1d1f 0%, #2d2d2f 100%); color: white; padding: 80px 0 72px; text-align: center; }
        .hero-eyebrow { font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: #f9a500; margin-bottom: 16px; }
        .hero h1 { font-size: 52px; font-weight: 700; letter-spacing: -0.03em; line-height: 1.1; margin-bottom: 20px; }
        .hero h1 em { font-style: normal; color: #f9a500; }
        .hero-sub { font-size: 19px; color: #a8a8a8; max-width: 620px; margin: 0 auto 28px; line-height: 1.5; }
        .hero-cta-group { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }
        .hero-review-stars { margin-top: 24px; font-size: 15px; color: #a8a8a8; }
        .hero-review-stars .stars { color: #f9a500; letter-spacing: 2px; }

        /* BUTTONS */
        .btn { padding: 14px 28px; border-radius: 980px; font-size: 15px; font-weight: 600; border: none; cursor: pointer; transition: all 0.2s ease; text-decoration: none; display: inline-flex; align-items: center; justify-content: center; gap: 8px; }
        .btn-primary { background: #f9a500; color: white; }
        .btn-primary:hover { background: #e09400; transform: translateY(-1px); }
        .btn-outline { background: transparent; color: white; border: 1.5px solid rgba(255,255,255,0.4); }
        .btn-outline:hover { background: rgba(255,255,255,0.08); }
        .btn-outline-dark { background: transparent; color: #1d1d1f; border: 1.5px solid #d2d2d7; }
        .btn-outline-dark:hover { border-color: #f9a500; color: #f9a500; }
        .btn-whatsapp { background: #25D366; color: white; }
        .btn-whatsapp:hover { background: #20BA5A; transform: translateY(-1px); }
        .btn-line { background: #06C755; color: white; }
        .btn-line:hover { background: #05B04C; transform: translateY(-1px); }

        /* STATS BAR */
        .stats-bar { background: #f5f5f7; border-bottom: 1px solid #e5e5e7; padding: 28px 0; }
        .stats-grid { display: grid; grid-template-columns: repeat(4,1fr); text-align: center; }
        .stat-item { padding: 0 16px; border-right: 1px solid #e5e5e7; }
        .stat-item:last-child { border-right: none; }
        .stat-number { font-size: 32px; font-weight: 700; color: #1d1d1f; letter-spacing: -0.02em; }
        .stat-label { font-size: 13px; color: #6e6e73; margin-top: 4px; }

        /* SECTIONS */
        .section { padding: 72px 0; }
        .section-alt { background: #f5f5f7; }
        .section-header { text-align: center; margin-bottom: 48px; }
        .section-eyebrow { font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: #f9a500; margin-bottom: 12px; }
        .section-header h2 { font-size: 40px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 16px; }
        .section-header p { font-size: 17px; color: #6e6e73; max-width: 600px; margin: 0 auto; }

        /* QUICK GUIDE TABLE */
        .quick-guide { max-width: 680px; margin: 0 auto 48px; border-radius: 16px; overflow: hidden; border: 1px solid #e5e5e7; background: white; }
        .quick-guide-title { font-size: 16px; font-weight: 600; padding: 18px 24px; background: #1d1d1f; color: white; }
        .quick-guide table { width: 100%; border-collapse: collapse; }
        .quick-guide th { text-align: left; padding: 12px 24px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em; color: #86868b; background: #fafafa; border-bottom: 1px solid #e5e5e7; }
        .quick-guide td { padding: 14px 24px; font-size: 15px; border-bottom: 1px solid #f0f0f2; color: #1d1d1f; }
        .quick-guide tr:last-child td { border-bottom: none; }
        .quick-guide .recommended { color: #f9a500; font-weight: 600; }

        /* FILM GRID */
        .film-grid { display: grid; grid-template-columns: repeat(2,1fr); gap: 20px; }
        .film-card { background: white; border-radius: 18px; padding: 28px; border: 1px solid #e5e5e7; transition: all 0.2s ease; position: relative; }
        .film-card:hover { box-shadow: 0 8px 24px rgba(0,0,0,0.08); transform: translateY(-2px); }
        .film-card.popular { border: 2px solid #1d1d1f; }
        .popular-badge { position: absolute; top: -1px; left: 28px; background: #f9a500; color: white; padding: 5px 14px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; border-radius: 0 0 8px 8px; }
        .film-card h3 { font-size: 22px; font-weight: 600; margin-bottom: 6px; letter-spacing: -0.01em; }
        .film-lifespan { font-size: 13px; color: #86868b; margin-bottom: 12px; }
        .film-price { font-size: 28px; font-weight: 700; color: #1d1d1f; margin-bottom: 4px; }
        .film-price-unit { font-size: 13px; color: #86868b; margin-bottom: 16px; }
        .film-desc { font-size: 14px; color: #6e6e73; line-height: 1.6; margin-bottom: 20px; }
        .film-note { font-size: 13px; color: #1d1d1f; background: #fef9ee; border: 1px solid #f9a500; border-radius: 10px; padding: 12px 16px; margin-bottom: 20px; line-height: 1.5; }
        .specs-row { display: flex; gap: 16px; padding: 12px 0; border-top: 1px solid #e5e5e7; font-size: 12px; color: #6e6e73; font-weight: 500; flex-wrap: wrap; }

        /* PROCESS STEPS */
        .process-steps { display: grid; grid-template-columns: repeat(4,1fr); gap: 20px; }
        .process-step { text-align: center; padding: 28px 20px; }
        .step-number { width: 48px; height: 48px; background: #1d1d1f; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 700; margin: 0 auto 16px; }
        .process-step h3 { font-size: 16px; font-weight: 600; margin-bottom: 8px; }
        .process-step p { font-size: 13px; color: #6e6e73; line-height: 1.5; }
        .timeline-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 16px; max-width: 680px; margin: 40px auto 0; }
        .timeline-item { text-align: center; padding: 20px 16px; background: white; border-radius: 14px; border: 1px solid #e5e5e7; }
        .timeline-item .timeline-type { font-size: 14px; font-weight: 600; color: #1d1d1f; margin-bottom: 4px; }
        .timeline-item .timeline-duration { font-size: 13px; color: #6e6e73; }

        /* PROPERTY TYPES BENTO GRID */
        .bento-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
        .bento-card { background: white; border-radius: 20px; border: 1px solid #e5e5e7; overflow: hidden; transition: all 0.2s ease; display: flex; flex-direction: column; }
        .bento-card:hover { box-shadow: 0 8px 24px rgba(0,0,0,0.08); transform: translateY(-2px); }
        .bento-visual { height: 160px; display: flex; align-items: center; justify-content: center; font-size: 56px; background: linear-gradient(135deg, #f5f5f7 0%, #ebebed 100%); }
        .bento-card:nth-child(1) .bento-visual { background: linear-gradient(135deg, #fef9ee 0%, #fdefd0 100%); }
        .bento-card:nth-child(2) .bento-visual { background: linear-gradient(135deg, #eef6fe 0%, #d0e8fd 100%); }
        .bento-card:nth-child(3) .bento-visual { background: linear-gradient(135deg, #eefef4 0%, #d0fde0 100%); }
        .bento-body { padding: 24px 24px 28px; flex: 1; display: flex; flex-direction: column; }
        .bento-body h3 { font-size: 20px; font-weight: 700; margin-bottom: 6px; letter-spacing: -0.01em; }
        .bento-body .bento-subtitle { font-size: 13px; color: #86868b; margin-bottom: 14px; }
        .bento-body .bento-desc { font-size: 14px; color: #6e6e73; line-height: 1.6; margin-bottom: 20px; }
        .bento-testimonial { margin-top: auto; padding: 16px; background: #f5f5f7; border-radius: 12px; font-size: 13px; color: #1d1d1f; line-height: 1.5; font-style: italic; }
        .bento-testimonial-author { font-size: 12px; color: #86868b; margin-top: 8px; font-style: normal; font-weight: 600; }
        @media (max-width: 768px) { .bento-grid { grid-template-columns: 1fr; } }

        /* FAQ */
        .faq-list { max-width: 720px; margin: 0 auto; }
        .faq-item { border-bottom: 1px solid #e5e5e7; padding: 24px 0; cursor: pointer; }
        .faq-item:first-child { border-top: 1px solid #e5e5e7; }
        .faq-question { font-size: 17px; font-weight: 600; color: #1d1d1f; display: flex; justify-content: space-between; align-items: center; gap: 16px; }
        .faq-question .faq-toggle { flex-shrink: 0; width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; font-size: 18px; color: #86868b; transition: transform 0.3s; }
        .faq-item.open .faq-toggle { transform: rotate(45deg); }
        .faq-answer { font-size: 15px; color: #6e6e73; line-height: 1.6; max-height: 0; overflow: hidden; transition: max-height 0.3s ease, padding 0.3s ease; padding-top: 0; }
        .faq-item.open .faq-answer { max-height: 300px; padding-top: 12px; }

        /* CLIMATE / TRUST CARDS */
        .climate-intro { max-width: 720px; margin: 0 auto 48px; font-size: 16px; color: #6e6e73; line-height: 1.7; text-align: center; }
        .challenge-cards { display: grid; grid-template-columns: repeat(3,1fr); gap: 20px; }
        .challenge-card { background: white; border-radius: 18px; padding: 32px 28px; border: 1px solid #e5e5e7; transition: all 0.2s ease; }
        .challenge-card:hover { box-shadow: 0 8px 24px rgba(0,0,0,0.08); transform: translateY(-2px); }
        .challenge-icon { font-size: 40px; margin-bottom: 16px; }
        .challenge-card h3 { font-size: 19px; font-weight: 600; margin-bottom: 10px; letter-spacing: -0.01em; }
        .challenge-card p { font-size: 14px; color: #6e6e73; line-height: 1.6; }

        /* PRICING */
        .pricing-tables { display: grid; grid-template-columns: 1fr; gap: 24px; max-width: 680px; margin: 0 auto; }
        .pricing-table-wrap { border-radius: 16px; overflow: hidden; border: 1px solid #e5e5e7; background: white; }
        .pricing-table-wrap h3 { font-size: 16px; font-weight: 600; padding: 18px 24px; background: #1d1d1f; color: white; }
        .pricing-table-wrap table { width: 100%; border-collapse: collapse; }
        .pricing-table-wrap th { text-align: left; padding: 10px 20px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em; color: #86868b; background: #fafafa; border-bottom: 1px solid #e5e5e7; }
        .pricing-table-wrap td { padding: 12px 20px; font-size: 14px; border-bottom: 1px solid #f0f0f2; color: #1d1d1f; }
        .pricing-table-wrap tr:last-child td { border-bottom: none; }
        .pricing-note { font-size: 13px; color: #86868b; text-align: center; margin-top: 20px; font-style: italic; }

        /* REVIEWS */
        .reviews-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 20px; }
        .review-card { background: white; border-radius: 18px; padding: 28px; border: 1px solid #e5e5e7; transition: all 0.2s ease; }
        .review-card:hover { box-shadow: 0 8px 24px rgba(0,0,0,0.08); transform: translateY(-2px); }
        .review-stars { color: #f9a500; font-size: 16px; letter-spacing: 2px; margin-bottom: 14px; }
        .review-text { font-size: 15px; color: #1d1d1f; line-height: 1.6; margin-bottom: 16px; font-style: italic; }
        .review-author { font-size: 14px; font-weight: 600; color: #1d1d1f; }
        .review-meta { font-size: 12px; color: #86868b; margin-top: 4px; }

        /* AREAS WE SERVE */
        .areas-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 10px; max-width: 800px; margin: 0 auto 40px; }
        .area-tag { text-align: center; padding: 10px 12px; background: white; border: 1px solid #e5e5e7; border-radius: 10px; font-size: 14px; color: #1d1d1f; transition: all 0.2s; }
        .area-tag:hover { border-color: #f9a500; color: #f9a500; }
        .nearby-cities { text-align: center; margin-top: 32px; padding-top: 32px; border-top: 1px solid #e5e5e7; }
        .nearby-cities h3 { font-size: 18px; font-weight: 600; margin-bottom: 16px; }
        .nearby-links { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }
        .nearby-links a { font-size: 14px; color: #f9a500; text-decoration: none; padding: 8px 18px; border: 1px solid #f9a500; border-radius: 980px; transition: all 0.2s; }
        .nearby-links a:hover { background: #f9a500; color: white; }

        /* WHY JAIDEECLEAR / TRUST */
        .trust-badges { display: grid; grid-template-columns: repeat(5,1fr); gap: 16px; max-width: 800px; margin: 40px auto 0; }
        .trust-badge { text-align: center; padding: 20px 12px; background: white; border-radius: 14px; border: 1px solid #e5e5e7; }
        .trust-badge .badge-icon { font-size: 28px; margin-bottom: 8px; }
        .trust-badge .badge-text { font-size: 13px; color: #1d1d1f; font-weight: 500; line-height: 1.4; }

        /* RELATED RESOURCES */
        .resources-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 24px; }
        .resource-group h3 { font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em; color: #86868b; margin-bottom: 16px; }
        .resource-group a { display: block; font-size: 15px; color: #1d1d1f; text-decoration: none; padding: 10px 0; border-bottom: 1px solid #f0f0f2; transition: color 0.2s; }
        .resource-group a:hover { color: #f9a500; }
        .resource-group a:last-child { border-bottom: none; }

        /* CONTACT FORM */
        .final-cta-section { background: linear-gradient(135deg, #1d1d1f 0%, #2d2d2f 100%); color: white; }
        .final-cta-inner { max-width: 680px; margin: 0 auto; text-align: center; }
        .final-cta-inner h2 { font-size: 40px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 16px; }
        .final-cta-inner > p { font-size: 17px; color: #a8a8a8; margin-bottom: 40px; }
        .contact-form { background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); border-radius: 20px; padding: 36px; text-align: left; }
        .form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px; }
        .form-group { display: flex; flex-direction: column; gap: 6px; }
        .form-group.full-width { grid-column: 1 / -1; }
        .form-group label { font-size: 13px; font-weight: 500; color: #a8a8a8; }
        .form-group input, .form-group select, .form-group textarea { padding: 12px 16px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.15); background: rgba(255,255,255,0.06); color: white; font-size: 15px; font-family: inherit; outline: none; transition: border-color 0.2s; }
        .form-group input::placeholder, .form-group textarea::placeholder { color: #6e6e73; }
        .form-group input:focus, .form-group select:focus, .form-group textarea:focus { border-color: #f9a500; }
        .form-group select option { background: #1d1d1f; color: white; }
        .form-group textarea { resize: vertical; min-height: 80px; }
        .form-submit-row { display: flex; gap: 12px; justify-content: center; margin-top: 24px; flex-wrap: wrap; }
        .contact-channels { display: flex; gap: 12px; justify-content: center; margin-top: 24px; flex-wrap: wrap; }
        .response-time { text-align: center; margin-top: 24px; font-size: 14px; color: #86868b; }
        .response-time strong { color: #a8a8a8; }

        /* SECTION CTA */
        .section-cta { text-align: center; margin-top: 40px; }
        .section-cta .btn { margin: 0 6px; }

        /* CTA BANNER */
        .cta-banner { background: linear-gradient(135deg, #1d1d1f 0%, #2d2d2f 100%); border-radius: 24px; padding: 48px; text-align: center; color: white; margin: 0 22px; }
        .cta-banner h3 { font-size: 28px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 12px; }
        .cta-banner p { font-size: 16px; color: #a8a8a8; margin-bottom: 24px; max-width: 480px; margin-left: auto; margin-right: auto; }

        /* STICKY MOBILE CTA */
        .sticky-mobile-cta { display: none; position: fixed; bottom: 0; left: 0; right: 0; background: rgba(255,255,255,0.97); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-top: 1px solid #e5e5e7; padding: 12px 16px; z-index: 999; box-shadow: 0 -4px 20px rgba(0,0,0,0.08); }
        .sticky-mobile-cta .sticky-inner { display: flex; gap: 10px; max-width: 480px; margin: 0 auto; }
        .sticky-mobile-cta .btn { flex: 1; padding: 12px 16px; font-size: 14px; text-align: center; }

        /* FOOTER */
        footer { border-top: 1px solid #e5e5e7; padding: 40px 0; margin-top: 0; }
        .footer-content { text-align: center; }
        .footer-locations { margin-bottom: 24px; }
        .footer-locations h4 { font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: #86868b; margin-bottom: 12px; }
        .footer-location-links { display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; }
        .footer-location-link { font-size: 13px; color: #6e6e73; text-decoration: none; padding: 5px 12px; border: 1px solid #e5e5e7; border-radius: 980px; transition: all 0.2s ease; }
        .footer-location-link:hover { border-color: #f9a500; color: #f9a500; }
        .footer-location-link--active { background: #f9a500; color: white; border-color: #f9a500; }
        .social-links { display: flex; justify-content: center; gap: 16px; margin-top: 24px; }
        .social-links a { color: #f9a500; font-size: 24px; text-decoration: none; }
        .social-links a:hover { color: #FFA500; }
        .copyright { font-size: 12px; color: #86868b; margin-top: 16px; }
        .copyright a { color: #86868b; }

        /* RESPONSIVE */
        @media (max-width: 768px) {
            .hero h1 { font-size: 36px; }
            .hero { padding: 60px 0 56px; }
            .stats-grid { grid-template-columns: repeat(2,1fr); gap: 16px; }
            .stat-item { border-right: none; border-bottom: 1px solid #e5e5e7; padding-bottom: 16px; }
            .stat-item:nth-last-child(-n+2) { border-bottom: none; }
            .film-grid { grid-template-columns: 1fr; }
            .process-steps { grid-template-columns: repeat(2,1fr); }
            .timeline-grid { grid-template-columns: 1fr; }
            .section-header h2 { font-size: 30px; }
            .section { padding: 56px 0; }
            .challenge-cards { grid-template-columns: 1fr; }
            .pricing-tables { grid-template-columns: 1fr; }
            .reviews-grid { grid-template-columns: 1fr; }
            .ba-grid { grid-template-columns: 1fr; }
            .areas-grid { grid-template-columns: repeat(2,1fr); }
            .trust-badges { grid-template-columns: repeat(2,1fr); }
            .resources-grid { grid-template-columns: 1fr; }
            .cta-banner { padding: 36px 24px; margin: 0; border-radius: 0; }
            .cta-banner h3 { font-size: 24px; }
            .final-cta-inner h2 { font-size: 30px; }
            .form-grid { grid-template-columns: 1fr; }
            .contact-form { padding: 24px; }
            .quick-guide { margin: 0 0 40px; }
            .sticky-mobile-cta { display: block; }
            body { padding-bottom: 72px; }
        }
        @media (max-width: 480px) {
            .hero h1 { font-size: 30px; }
            .areas-grid { grid-template-columns: repeat(2,1fr); }
            .trust-badges { grid-template-columns: 1fr; }
        }
    """


# ══════════════════════════════════════════════
# JS SCRIPTS (from Phuket gold standard)
# ══════════════════════════════════════════════
def get_js():
    return """
    // Mobile menu toggle
    (function() {
        var btn = document.getElementById('hamburger');
        var menu = document.getElementById('mobileMenu');
        if (!btn || !menu) return;
        btn.addEventListener('click', function() {
            var isOpen = menu.classList.toggle('open');
            btn.classList.toggle('open', isOpen);
            btn.setAttribute('aria-expanded', isOpen);
            document.body.style.overflow = isOpen ? 'hidden' : '';
        });
        menu.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                menu.classList.remove('open');
                btn.classList.remove('open');
                btn.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            });
        });
        document.addEventListener('click', function(e) {
            if (!btn.contains(e.target) && !menu.contains(e.target)) {
                menu.classList.remove('open');
                btn.classList.remove('open');
                btn.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            }
        });
    })();

    // FAQ accordion
    (function() {
        document.querySelectorAll('.faq-item').forEach(function(item) {
            var question = item.querySelector('.faq-question');
            question.addEventListener('click', function() {
                document.querySelectorAll('.faq-item.open').forEach(function(openItem) {
                    if (openItem !== item) openItem.classList.remove('open');
                });
                item.classList.toggle('open');
            });
        });
    })();

    // Sticky mobile CTA — show after scrolling past hero
    (function() {
        var sticky = document.getElementById('stickyCta');
        if (!sticky) return;
        var hero = document.querySelector('.hero');
        if (!hero) return;
        function checkScroll() {
            var heroBottom = hero.getBoundingClientRect().bottom;
            if (heroBottom < 0) {
                sticky.style.display = 'block';
            } else {
                sticky.style.display = 'none';
            }
        }
        function init() {
            if (window.innerWidth <= 768) {
                window.addEventListener('scroll', checkScroll, { passive: true });
                checkScroll();
            } else {
                sticky.style.display = 'none';
                window.removeEventListener('scroll', checkScroll);
            }
        }
        init();
        window.addEventListener('resize', init);
    })();
    """


# ══════════════════════════════════════════════
# HELPER FUNCTIONS — build dynamic HTML sections
# ══════════════════════════════════════════════

def _wa_link(city_name, text="Hi, I'd like a quote for window tinting in {city}"):
    msg = text.replace("{city}", city_name)
    return f"https://wa.me/{WHATSAPP}?text={quote(msg)}"


def build_schema_localbusiness(c):
    schema = {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "name": f"JaiDeeClear Window Film — {c['name']}",
        "description": f"Professional window tinting and UV protection film installation in {c['name']}. On-site service for homes, condos, and offices. 99% UV blocking, up to 30% energy savings.",
        "url": f"https://jaideeclear.com/window-tinting-{c['slug']}/",
        "telephone": f"+{WHATSAPP.lstrip('+')}",
        "email": "jaideeclear@gmail.com",
        "image": f"https://jaideeclear.com/images/{c['slug']}-hero.jpg",
        "logo": f"https://jaideeclear.com/{LOGO}",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": c["name"],
            "addressRegion": c["province"],
            "addressCountry": "TH"
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": c["lat"],
            "longitude": c["lng"]
        },
        "areaServed": {
            "@type": "City",
            "name": c["name"]
        },
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
            "opens": "08:00",
            "closes": "18:00"
        }],
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "[PLACEHOLDER - Rating, e.g. 4.9]",
            "reviewCount": "[PLACEHOLDER - Count, e.g. 47]"
        },
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Window Film Services",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Residential Window Tinting", "description": f"Professional window film for homes, condos, and villas in {c['name']}"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Commercial Window Tinting", "description": f"Window film for offices, hotels, resorts, and commercial buildings in {c['name']}"}}
            ]
        },
        "sameAs": [FACEBOOK, INSTAGRAM]
    }
    return json.dumps(schema, indent=6, ensure_ascii=False)


def build_schema_faq(c):
    entities = []
    for faq in c["faqs"]:
        entities.append({
            "@type": "Question",
            "name": faq["q"],
            "acceptedAnswer": {"@type": "Answer", "text": faq["a"]}
        })
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities
    }
    return json.dumps(schema, indent=6, ensure_ascii=False)


def build_schema_breadcrumb(c):
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://jaideeclear.com/"},
            {"@type": "ListItem", "position": 2, "name": "Locations", "item": "https://jaideeclear.com/locations/"},
            {"@type": "ListItem", "position": 3, "name": f"Window Tinting in {c['name']}", "item": f"https://jaideeclear.com/window-tinting-{c['slug']}/"}
        ]
    }
    return json.dumps(schema, indent=6, ensure_ascii=False)


def build_film_cards(c):
    return f"""
                <!-- Carbon Series -->
                <div class="film-card">
                    <h3>Carbon Series</h3>
                    <p class="film-lifespan">Lifespan: 2–3 years</p>
                    <div class="film-price">฿50–70</div>
                    <div class="film-price-unit">per sq.ft</div>
                    <p class="film-desc">{c['film_carbon_desc']}</p>
                    <div class="specs-row">
                        <span>UVR: 99%</span>
                        <span>Basic heat rejection</span>
                        <span>Best for: Budget installs</span>
                    </div>
                </div>

                <!-- Ceramic Nano (Popular) -->
                <div class="film-card popular">
                    <div class="popular-badge">Most Popular</div>
                    <h3>Ceramic Nano</h3>
                    <p class="film-lifespan">Lifespan: 5–7 years</p>
                    <div class="film-price">฿90–110</div>
                    <div class="film-price-unit">per sq.ft</div>
                    <p class="film-desc">{c['film_nano_desc']}</p>
                    <div class="film-note">
                        <strong>{c['film_nano_local_note_bold']}</strong> {c['film_nano_local_note']}
                    </div>
                    <div class="specs-row">
                        <span>UVR: 99%</span>
                        <span>High IRR</span>
                        <span>Clear appearance</span>
                    </div>
                </div>

                <!-- Ceramic UV400 -->
                <div class="film-card">
                    <h3>Ceramic UV400</h3>
                    <p class="film-lifespan">Lifespan: 5–7 years</p>
                    <div class="film-price">฿110–130</div>
                    <div class="film-price-unit">per sq.ft</div>
                    <p class="film-desc">{c['film_uv400_desc']}</p>
                    <div class="specs-row">
                        <span>UVR: 99%+</span>
                        <span>UV400 spectrum</span>
                        <span>Best for: Skin protection</span>
                    </div>
                </div>

                <!-- Sputtering Series -->
                <div class="film-card">
                    <h3>Sputtering Series</h3>
                    <p class="film-lifespan">Lifespan: 7+ years</p>
                    <div class="film-price">฿155+</div>
                    <div class="film-price-unit">per sq.ft</div>
                    <p class="film-desc">{c['film_sputtering_desc']}</p>
                    <div class="specs-row">
                        <span>UVR: 99%</span>
                        <span>Max TSER</span>
                        <span>Best for: Commercial &amp; luxury</span>
                    </div>
                </div>"""


def build_property_cards(c):
    html = ""
    for pt in c["property_types"]:
        html += f"""
                <div class="bento-card">
                    <div class="bento-visual">{pt['emoji']}</div>
                    <div class="bento-body">
                        <h3>{pt['title']}</h3>
                        <p class="bento-subtitle">{pt['subtitle']}</p>
                        <p class="bento-desc">{pt['desc']}</p>
                        <div class="bento-testimonial">
                            {pt['testimonial']}
                            <div class="bento-testimonial-author">{pt['testimonial_author']}</div>
                        </div>
                    </div>
                </div>"""
    return html


def build_faq_items(c):
    html = ""
    for faq in c["faqs"]:
        html += f"""
                <div class="faq-item">
                    <p class="faq-question">
                        <span>{faq['q']}</span>
                        <span class="faq-toggle">+</span>
                    </p>
                    <div class="faq-answer">{faq['a']}</div>
                </div>"""
    return html


def build_pricing_rows(c):
    html = ""
    for row in c["pricing_rows"]:
        html += f"""
                            <tr>
                                <td>{row[0]}</td>
                                <td>{row[1]}</td>
                                <td>{row[2]}</td>
                            </tr>"""
    return html


def build_review_cards(c):
    html = ""
    for r in c["reviews"]:
        html += f"""
                <div class="review-card">
                    <div class="review-stars">★★★★★</div>
                    <p class="review-text">"{r['text']}"</p>
                    <p class="review-author">{r['author']}</p>
                    <p class="review-meta">{r['meta']}</p>
                </div>"""
    return html


def build_area_tags(c):
    html = ""
    for area in c["areas"]:
        html += f"""
                <div class="area-tag">{area}</div>"""
    return html


def build_nearby_links(c):
    html = ""
    for name, slug in c["nearby_cities"]:
        html += f"""
                    <a href="window-tinting-{slug}.html">Window Tinting in {name} →</a>"""
    return html


def build_footer_links(c, all_cities):
    html = ""
    for city in all_cities:
        active = " footer-location-link--active" if city["slug"] == c["slug"] else ""
        html += f"""
                        <a href="window-tinting-{city['slug']}.html" class="footer-location-link{active}">{city['name']}</a>"""
    return html


def build_related_locations(c):
    html = ""
    for name, slug in c["related_locations"]:
        html += f"""
                    <a href="window-tinting-{slug}.html">Window Tinting in {name} →</a>"""
    return html


# ══════════════════════════════════════════════
# MAIN PAGE GENERATOR
# ══════════════════════════════════════════════

def generate_page(c, all_cities):
    """Generate complete HTML page for a city."""
    css = get_css()
    js = get_js()
    wa_quote = _wa_link(c["name"])
    wa_film = _wa_link(c["name"], "Hi, I'd like a film recommendation for my {city} property")
    wa_faq = _wa_link(c["name"], "Hi, I have a question about window tinting in {city}")
    wa_cta = _wa_link(c["name"], "Hi, I'd like a free quote for window tinting in {city}")

    # Build all dynamic sections
    schema_lb = build_schema_localbusiness(c)
    schema_faq = build_schema_faq(c)
    schema_bc = build_schema_breadcrumb(c)
    film_cards = build_film_cards(c)
    property_cards = build_property_cards(c)
    faq_items = build_faq_items(c)
    pricing_rows = build_pricing_rows(c)
    review_cards = build_review_cards(c)
    area_tags = build_area_tags(c)
    nearby_links = build_nearby_links(c)
    footer_links = build_footer_links(c, all_cities)
    related_locs = build_related_locations(c)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="icon" type="image/x-icon" href="favicon.ico">
    <link rel="icon" type="image/png" href="favicon.png">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- SEO Meta Tags -->
    <title>Window Tinting in {c['name']} | Professional UV Film Installation — JaiDeeClear</title>
    <meta name="description" content="{c['meta_desc']}">
    <link rel="canonical" href="https://jaideeclear.com/window-tinting-{c['slug']}/">

    <!-- Open Graph -->
    <meta property="og:title" content="Window Tinting in {c['name']} — JaiDeeClear">
    <meta property="og:description" content="Professional window film installation. 99% UV protection, up to 30% energy savings. Free quote.">
    <meta property="og:image" content="https://jaideeclear.com/images/{c['slug']}-og.jpg">
    <meta property="og:url" content="https://jaideeclear.com/window-tinting-{c['slug']}/">
    <meta property="og:type" content="website">

    <!-- Schema 1: LocalBusiness -->
    <script type="application/ld+json">
    {schema_lb}
    </script>

    <!-- Schema 2: FAQPage -->
    <script type="application/ld+json">
    {schema_faq}
    </script>

    <!-- Schema 3: BreadcrumbList -->
    <script type="application/ld+json">
    {schema_bc}
    </script>

    <!-- Seline Analytics -->
    <script async src="https://cdn.seline.com/seline.js" data-token="{SELINE_TOKEN}"></script>

    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

    <style>{css}
    </style>
</head>
<body>

    <!-- HEADER -->
    <header>
        <div class="header-content">
            <div class="logo-container">
                <a href="index.html">
                    <img src="{LOGO}" alt="JaiDeeClear Logo" style="height: 64px; width: auto; object-fit: contain;">
                </a>
            </div>
            <nav class="header-nav">
                <a href="about.html" class="nav-link">About</a>
                <a href="schedule.html" class="nav-link">Schedule</a>
                <a href="https://wa.me/{WHATSAPP}" target="_blank" class="whatsapp-btn">
                    {WA_SVG}
                    Chat with Us
                </a>
            </nav>
            <button class="hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false">
                <span></span><span></span><span></span>
            </button>
        </div>
    </header>

    <!-- Mobile menu drawer -->
    <div class="mobile-menu" id="mobileMenu" role="navigation" aria-label="Mobile navigation">
        <a href="about.html" class="nav-link">About</a>
        <a href="schedule.html" class="nav-link">Schedule</a>
        <a href="https://wa.me/{WHATSAPP}" target="_blank" class="whatsapp-btn">
            {WA_SVG}
            Chat with Us
        </a>
    </div>

    <!-- BREADCRUMB -->
    <nav class="breadcrumb" aria-label="Breadcrumb">
        <div class="container">
            <ol class="breadcrumb-list">
                <li><a href="index.html">Home</a></li>
                <li class="separator">›</li>
                <li><a href="index.html#locations">Locations</a></li>
                <li class="separator">›</li>
                <li class="current">Window Tinting in {c['name']}</li>
            </ol>
        </div>
    </nav>

    <!-- HERO -->
    <section class="hero">
        <div class="container">
            <p class="hero-eyebrow">Window Tinting · {c['name']}</p>
            <h1>Professional Window Tinting<br>in <em>{c['name']}</em></h1>
            <p class="hero-sub">
                {c['hero_sub']}
            </p>
            <div class="hero-cta-group">
                <a href="schedule.html" class="btn btn-primary">Get a Free Quote</a>
                <a href="https://wa.me/{WHATSAPP}" target="_blank" class="btn btn-outline">
                    <i class="fab fa-whatsapp"></i> WhatsApp Us
                </a>
            </div>
            <p class="hero-review-stars">
                <span class="stars">★★★★★</span> <strong>[PLACEHOLDER - Rating, e.g. 4.9]</strong> from <strong>[PLACEHOLDER - Count, e.g. 47]</strong> Google Reviews
            </p>
        </div>
    </section>

    <!-- Stats bar -->
    <div class="stats-bar">
        <div class="container">
            <div class="stats-grid">
                <div class="stat-item">
                    <div class="stat-number">99%</div>
                    <div class="stat-label">UV Rays Blocked</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">{c['stat_uv']}</div>
                    <div class="stat-label">{c['stat_uv_label']}</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">30%</div>
                    <div class="stat-label">Avg. Electricity Savings</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">7 yrs</div>
                    <div class="stat-label">Max Film Lifespan</div>
                </div>
            </div>
        </div>
    </div>

    <!-- FILMS SECTION -->
    <section class="section section-alt" id="films">
        <div class="container">
            <div class="section-header">
                <p class="section-eyebrow">Our Films</p>
                <h2>Choose the Right Film for Your {c['name']} Property</h2>
                <p>Every film is professionally installed on-site. Free measurement included with every quote.</p>
            </div>

            <!-- Quick Guide -->
            <div class="quick-guide">
                <div class="quick-guide-title">How to Choose — Quick Guide</div>
                <table>
                    <thead>
                        <tr>
                            <th>Your Priority</th>
                            <th>Recommended Film</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Best value / short-term rental</td>
                            <td>Carbon Series</td>
                        </tr>
                        <tr>
                            <td>Best all-round for homes &amp; condos</td>
                            <td class="recommended">Ceramic Nano ⭐</td>
                        </tr>
                        <tr>
                            <td>Max skin &amp; furniture protection</td>
                            <td>Ceramic UV400</td>
                        </tr>
                        <tr>
                            <td>{c['quick_guide_premium_label']}</td>
                            <td>Sputtering Series</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Film Cards -->
            <div class="film-grid">{film_cards}
            </div>

            <!-- Section CTA -->
            <div class="section-cta">
                <a href="schedule.html" class="btn btn-primary">Get a Quote →</a>
                <a href="{wa_film}" target="_blank" class="btn btn-outline-dark">Not sure which film? Get a free recommendation →</a>
            </div>
        </div>
    </section>

    <!-- HOW IT WORKS -->
    <section class="section" id="how-it-works">
        <div class="container">
            <div class="section-header">
                <p class="section-eyebrow">How It Works</p>
                <h2>{c['process_title']}</h2>
                <p>{c['process_sub']}</p>
            </div>
            <div class="process-steps">
                <div class="process-step">
                    <div class="step-number">1</div>
                    <h3>Get a Quote</h3>
                    <p>{c['process_step1_text']}</p>
                </div>
                <div class="process-step">
                    <div class="step-number">2</div>
                    <h3>Free Measurement</h3>
                    <p>{c['process_step2_text']}</p>
                </div>
                <div class="process-step">
                    <div class="step-number">3</div>
                    <h3>Professional Install</h3>
                    <p>We install your chosen film cleanly and efficiently. You can stay in the property during the entire process — minimal disruption guaranteed.</p>
                </div>
                <div class="process-step">
                    <div class="step-number">4</div>
                    <h3>Enjoy &amp; Save</h3>
                    <p>Feel the difference immediately — cooler rooms, lower electricity bills, and protected interiors across your {c['name']} property.</p>
                </div>
            </div>

            <!-- Timelines -->
            <div class="timeline-grid">
                <div class="timeline-item">
                    <div class="timeline-type">Condo / Apartment</div>
                    <div class="timeline-duration">3–5 hours</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-type">Villa (3–4 bed)</div>
                    <div class="timeline-duration">1 full day</div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-type">Large Villa / Commercial</div>
                    <div class="timeline-duration">1–3 days</div>
                </div>
            </div>

            <div class="section-cta">
                <a href="schedule.html" class="btn btn-primary">Get Started — Request Your Free Measurement →</a>
            </div>
        </div>
    </section>

    <!-- PROPERTY TYPES -->
    <section class="section" id="property-types">
        <div class="container">
            <div class="section-header">
                <p class="section-eyebrow">Who We Work With</p>
                <h2>Properties That Often Work With Us in {c['name']}</h2>
                <p>{c['property_types_subtitle']}</p>
            </div>
            <div class="bento-grid">{property_cards}
            </div>
        </div>
    </section>

    <!-- FAQ -->
    <section class="section section-alt" id="faq">
        <div class="container">
            <div class="section-header">
                <p class="section-eyebrow">FAQ</p>
                <h2>{c['faq_title']}</h2>
            </div>
            <div class="faq-list">{faq_items}
            </div>
            <div class="section-cta">
                <a href="{wa_faq}" target="_blank" class="btn btn-outline-dark"><i class="fab fa-whatsapp"></i> Have a question? Ask us on WhatsApp</a>
            </div>
        </div>
    </section>

    <!-- PRICING -->
    <section class="section section-alt" id="pricing">
        <div class="container">
            <div class="section-header">
                <p class="section-eyebrow">Pricing</p>
                <h2>{c['pricing_title']}</h2>
                <p>Transparent pricing by property type. Free on-site measurement included with every quote.</p>
            </div>
            <div class="pricing-tables">
                <div class="pricing-table-wrap">
                    <h3>Estimated Costs by Property Type</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Property Type</th>
                                <th>Typical Glass Area</th>
                                <th>Cost Range</th>
                            </tr>
                        </thead>
                        <tbody>{pricing_rows}
                        </tbody>
                    </table>
                </div>
            </div>
            <p class="pricing-note">Ranges cover Carbon (lowest) to Sputtering (highest). Final price based on actual measured glass area.</p>
            <div class="section-cta">
                <a href="schedule.html" class="btn btn-primary">Get Your Exact Price — Free Quote →</a>
            </div>
        </div>
    </section>

    <!-- REVIEWS -->
    <section class="section" id="reviews">
        <div class="container">
            <div class="section-header">
                <p class="section-eyebrow">Reviews</p>
                <h2>{c['reviews_title']}</h2>
                <p>{c['reviews_sub']}</p>
            </div>
            <div class="reviews-grid">{review_cards}
            </div>
        </div>
    </section>

    <!-- AREAS WE SERVE -->
    <section class="section" id="areas">
        <div class="container">
            <div class="section-header">
                <p class="section-eyebrow">Service Areas</p>
                <h2>Areas We Serve Across {c['name']}</h2>
                <p>Free on-site measurement and installation across the entire area.</p>
            </div>
            <div class="areas-grid">{area_tags}
            </div>
            <div class="nearby-cities">
                <h3>Nearby Cities We Also Serve</h3>
                <div class="nearby-links">{nearby_links}
                </div>
            </div>
        </div>
    </section>

    <!-- WHY JAIDEECLEAR -->
    <section class="section section-alt" id="why-us">
        <div class="container">
            <div class="section-header">
                <p class="section-eyebrow">Why Us</p>
                <h2>Why Choose JaiDeeClear in {c['name']}</h2>
                <p>30+ premium projects completed across Thailand's most prestigious developments.</p>
            </div>
            <div class="challenge-cards">
                <div class="challenge-card">
                    <div class="challenge-icon">🏆</div>
                    <h3>Proven Track Record</h3>
                    <p>Over 30 premium projects completed — from luxury villas to commercial buildings across Thailand. Every installation is backed by real results and repeat clients.</p>
                </div>
                <div class="challenge-card">
                    <div class="challenge-icon">⚙️</div>
                    <h3>Premium Technology</h3>
                    <p>We use advanced ceramic nano and UV protection films that deliver 99%+ UV blockage, superior heat rejection, and exceptional durability. No cheap metallic films that degrade in months.</p>
                </div>
                <div class="challenge-card">
                    <div class="challenge-icon">👷</div>
                    <h3>Professional Installation</h3>
                    <p>Our team brings over 10 years of hands-on experience. Every install is precise, clean, and backed by a manufacturer warranty — no shortcuts, no callbacks.</p>
                </div>
                <div class="challenge-card">
                    <div class="challenge-icon">📉</div>
                    <h3>Measurable Results</h3>
                    <p>Clients report immediate comfort improvements and energy savings up to 30%. Reduced glare, enhanced privacy, and significantly lower electricity bills — starting from day one.</p>
                </div>
                <div class="challenge-card">
                    <div class="challenge-icon">🗺️</div>
                    <h3>Regional Expertise</h3>
                    <p>With established presence across Bangkok, Phuket, Pattaya, and more, we understand Thailand's unique climate challenges. Our specifications are tailored to local conditions — not generic imports.</p>
                </div>
                <div class="challenge-card">
                    <div class="challenge-icon">🤝</div>
                    <h3>Comprehensive Service</h3>
                    <p>From initial consultation through specification, installation, and after-sales support — we manage every step. Free on-site measurement, 0% installment options, and a 5-year warranty included.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- RELATED RESOURCES -->
    <section class="section" id="resources">
        <div class="container">
            <div class="section-header">
                <p class="section-eyebrow">Learn More</p>
                <h2>Related Resources</h2>
            </div>
            <div class="resources-grid">
                <div class="resource-group">
                    <h3>Guides</h3>
                    <a href="/blog/how-to-choose-window-film/">How to Choose the Right Window Film →</a>
                    <a href="/blog/ceramic-vs-carbon/">Ceramic vs Carbon Film: What's the Difference? →</a>
                    <a href="/blog/window-film-electricity-savings/">How Window Film Cuts Your Electricity Bill →</a>
                </div>
                <div class="resource-group">
                    <h3>Other Locations</h3>{related_locs}
                </div>
                <div class="resource-group">
                    <h3>Services</h3>
                    <a href="/services/residential/">Residential Window Tinting →</a>
                    <a href="/services/commercial/">Commercial Window Tinting →</a>
                    <a href="/films/">View All Films →</a>
                </div>
            </div>
        </div>
    </section>

    <!-- FINAL CTA + CONTACT FORM -->
    <section class="section final-cta-section" id="contact">
        <div class="container">
            <div class="final-cta-inner">
                <h2>{c['cta_title']}</h2>
                <p>{c['cta_sub']}</p>

                <form class="contact-form" action="{FORMSPREE}" method="POST">
                    <div class="form-grid">
                        <div class="form-group">
                            <label for="contact-name">Name</label>
                            <input type="text" id="contact-name" name="name" placeholder="Your name" required>
                        </div>
                        <div class="form-group">
                            <label for="contact-phone">Phone / WhatsApp</label>
                            <input type="tel" id="contact-phone" name="phone" placeholder="+66..." required>
                        </div>
                        <div class="form-group">
                            <label for="contact-property">Property Type</label>
                            <select id="contact-property" name="property">
                                <option value="" disabled selected>Select property type</option>
                                <option value="condo">Condo</option>
                                <option value="house">House</option>
                                <option value="villa">Villa</option>
                                <option value="office">Office</option>
                                <option value="hotel">Hotel / Resort</option>
                                <option value="other">Other</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="contact-district">District / Area in {c['name']}</label>
                            <input type="text" id="contact-district" name="district" placeholder="{c['contact_district_placeholder']}">
                        </div>
                        <div class="form-group full-width">
                            <label for="contact-message">Message (optional)</label>
                            <textarea id="contact-message" name="message" placeholder="Tell us about your property or any questions..."></textarea>
                        </div>
                    </div>
                    <input type="hidden" name="_subject" value="New lead from {c['name']} city page">
                    <div class="form-submit-row">
                        <button type="submit" class="btn btn-primary">Get My Free Quote</button>
                    </div>
                </form>

                <div class="contact-channels">
                    <a href="{wa_cta}" target="_blank" class="btn btn-whatsapp">
                        <i class="fab fa-whatsapp"></i> WhatsApp Us
                    </a>
                    <a href="{LINE_URL}" target="_blank" class="btn btn-line">
                        <i class="fab fa-line"></i> Add Us on LINE
                    </a>
                </div>

                <div class="response-time">
                    <strong>Business hours:</strong> Mon–Sat, 8am–6pm<br>
                    We respond within 2 hours during business hours
                </div>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-locations">
                    <h4>Service Locations</h4>
                    <div class="footer-location-links">{footer_links}
                    </div>
                </div>
                <div class="social-links">
                    <a href="{FACEBOOK}" target="_blank" aria-label="Facebook">
                        <i class="fab fa-facebook-f"></i>
                    </a>
                    <a href="{INSTAGRAM}" target="_blank" aria-label="Instagram">
                        <i class="fab fa-instagram"></i>
                    </a>
                </div>
                <p class="copyright">© 2025 JaiDeeClear. On-site service throughout Thailand · <a href="index.html">Home</a></p>
            </div>
        </div>
    </footer>

    <!-- STICKY MOBILE CTA BAR -->
    <div class="sticky-mobile-cta" id="stickyCta">
        <div class="sticky-inner">
            <a href="schedule.html" class="btn btn-primary">Get a Quote</a>
            <a href="https://wa.me/{WHATSAPP}" target="_blank" class="btn btn-whatsapp">
                <i class="fab fa-whatsapp"></i> WhatsApp
            </a>
        </div>
    </div>

    <!-- SCRIPTS -->
    <script>{js}
    </script>

</body>
</html>"""

    return html


# ══════════════════════════════════════════════
# MAIN ENTRY POINT
# ══════════════════════════════════════════════

def main():
    all_cities = build_cities()
    output_dir = os.path.dirname(os.path.abspath(__file__))

    for city in all_cities:
        filename = f"window-tinting-{city['slug']}.html"
        filepath = os.path.join(output_dir, filename)
        html = generate_page(city, all_cities)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  Generated: {filename}")

    print(f"\nDone — {len(all_cities)} city pages generated.")


if __name__ == "__main__":
    main()

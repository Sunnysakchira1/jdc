#!/usr/bin/env python3
"""
Programmatic generator for JaiDeeClear SEO location pages.
Produces 10 city-specific HTML files with unique localized content.
"""

import os

CITIES = [
    {
        "name": "Bangkok",
        "slug": "bangkok",
        "meta_desc": "Best window tinting in Bangkok — JaiDeeClear installs premium UV & heat-rejection film for condos, houses, villas, and offices across Bangkok. Free on-site measurement. Call today.",
        "hero_sub": "Bangkok's extreme heat and UV index demand serious solar protection. JaiDeeClear brings professional window film installation directly to your door — condos, houses, villas, and offices across the entire city.",
        "stat_uv": "UV 13",
        "stat_uv_label": "Bangkok's Peak UV Index",
        "section_eyebrow_why": "Why Bangkok",
        "section_title_why": "Bangkok's Climate Makes Window Tinting Essential",
        "section_sub_why": "From Sukhumvit high-rises to Thonburi townhouses, the capital's punishing sun affects every property type.",
        "reasons": [
            {"icon": "☀️", "title": "Extreme UV Exposure", "text": "Bangkok regularly records a UV index of 11–13 — classified as \"Extreme\" by the WHO. Unprotected glass lets in UV radiation that fades furniture, damages flooring, and harms skin even indoors. A quality ceramic film blocks up to 99% of UV rays year-round."},
            {"icon": "🌡️", "title": "Year-Round Heat", "text": "Bangkok averages 35°C in the hot season, and glass-heavy condos along Sukhumvit, Silom, and Ratchada corridors trap solar heat aggressively. Window film with high infrared rejection (IRR) can reduce indoor temperatures by up to 10°C, cutting air-conditioning costs significantly."},
            {"icon": "🏙️", "title": "High-Density Living", "text": "Bangkok's dense urban fabric — from the glass towers of Asok and Chidlom to low-rise communities in Ladprao and Bang Na — means privacy is a constant concern. Daytime privacy film lets natural light in while blocking the view from outside, without darkening your interior."},
            {"icon": "💡", "title": "Soaring Electricity Bills", "text": "Air conditioning accounts for up to 50% of electricity use in Bangkok homes and offices. By rejecting solar heat at the glass, window film reduces the load on your AC system — most customers report a 20–30% drop in their monthly electricity bill."},
            {"icon": "🛡️", "title": "Safety & Security", "text": "Bangkok's urban environment calls for added security. Our safety films (0.4 mm and 0.8 mm) hold shattered glass in place in the event of a break-in, accident, or storm — protecting occupants in condos from Chatuchak to Bangkapi."},
            {"icon": "🏢", "title": "Commercial Compliance", "text": "Office buildings along Sathorn, Wireless Road, and the CBD increasingly specify solar-control glazing for LEED and energy-efficiency targets. JaiDeeClear's commercial-grade films help buildings meet these standards without costly glass replacement."},
        ],
        "film_section_title": "Choose the Right Film for Your Bangkok Property",
        "film_section_sub": "Every film is professionally installed on-site. Free measurement included with every quote.",
        "film_popular_desc": "The top choice for Bangkok condos and houses. Nano-ceramic technology delivers excellent heat and glare reduction without a metallic appearance — preserving your view of the city skyline.",
        "film_uv400_desc": "Enhanced UV400 blocking for maximum skin and furniture protection. Recommended for Bangkok properties with large south-facing windows or significant afternoon sun exposure.",
        "film_sputtering_desc": "Premium magnetron-sputtered film for maximum solar control. The preferred choice for Bangkok commercial buildings, luxury condos, and high-rise offices requiring the highest TSER performance.",
        "process_sub": "We come to you anywhere in Bangkok — no need to remove windows or visit a workshop.",
        "process_step2_text": "Our technician visits your property — from Sukhumvit to Bangna — to measure all windows at no charge.",
        "process_step1_text": "Use our online quote tool or WhatsApp us with your property type and location in Bangkok.",
        "faq_title": "Common Questions About Window Tinting in Bangkok",
        "faqs": [
            {"q": "Is window tinting legal for residential properties in Bangkok?", "a": "Yes. There are no legal restrictions on window film for residential properties in Thailand. For vehicles, Thai law specifies minimum visible light transmission levels, but for homes, condos, and offices in Bangkok, you are free to choose any film darkness or reflectivity level."},
            {"q": "How long does installation take for a Bangkok condo?", "a": "A standard Bangkok condo (1–2 bedrooms) typically takes 3–5 hours. Larger units or townhouses may require a full day. Our team works cleanly and efficiently, and you can remain in the property during installation."},
            {"q": "Will window film affect my view of the Bangkok skyline?", "a": "Our Ceramic Nano and Ceramic UV400 films are specifically designed to maintain high visible light transmission — you keep your view of landmarks like Asiatique, the Chao Phraya River, or the city skyline while blocking heat and UV. We also offer near-clear options with minimal tint."},
            {"q": "Do you serve all areas of Bangkok?", "a": "Yes — we cover the entire Bangkok metropolitan area, including Sukhumvit, Silom, Sathorn, Ladprao, Bangna, Thonburi, Nonthaburi, and surrounding districts. Travel fees may apply for properties beyond the inner city."},
            {"q": "How much can I save on electricity in Bangkok?", "a": "Most Bangkok customers report a 20–30% reduction in air-conditioning costs after installation. Given Bangkok's average electricity rate of approximately ฿4–5 per kWh and the city's near year-round cooling demand, quality window film typically pays for itself within 1–2 years."},
        ],
        "cta_title": "Ready to Tint Your Bangkok Property?",
        "cta_sub": "Get a free on-site measurement and no-obligation quote. We serve all Bangkok districts.",
    },
    {
        "name": "Chiang Mai",
        "slug": "chiang-mai",
        "meta_desc": "Best window tinting in Chiang Mai — JaiDeeClear installs premium UV & heat-rejection film for houses, villas, condos, and offices across Chiang Mai. Free on-site measurement.",
        "hero_sub": "Chiang Mai's scorching hot season and growing expat community make professional window film a smart investment. JaiDeeClear delivers on-site installation to homes, villas, and offices throughout the city and surrounding areas.",
        "stat_uv": "UV 12",
        "stat_uv_label": "Chiang Mai Peak UV Index",
        "section_eyebrow_why": "Why Chiang Mai",
        "section_title_why": "Chiang Mai's Climate Makes Window Tinting a Smart Choice",
        "section_sub_why": "From Nimmanhaemin condos to Hang Dong villas, the northern capital's intense sun and seasonal haze affect every property.",
        "reasons": [
            {"icon": "☀️", "title": "Fierce Hot-Season Sun", "text": "Chiang Mai's hot season (March–May) routinely pushes temperatures above 40°C, with UV index readings of 11–12. Unprotected windows turn homes into greenhouses — quality window film blocks up to 99% of UV rays and dramatically reduces indoor heat."},
            {"icon": "🌡️", "title": "Wide Temperature Swings", "text": "Chiang Mai swings from cool-season mornings near 15°C to hot-season afternoons above 40°C. Window film provides year-round insulation — keeping heat out in summer and reducing heat loss in the cooler months, stabilising your indoor climate."},
            {"icon": "🏡", "title": "Expat Villas & Modern Condos", "text": "The Nimmanhaemin, Santitham, and Hang Dong areas are home to a thriving expat community living in modern villas and condos with large glass facades. These properties benefit enormously from heat-rejection film that preserves mountain views while cutting solar gain."},
            {"icon": "💡", "title": "Lower Electricity Bills", "text": "Air conditioning is essential during Chiang Mai's hot season, and electricity costs add up quickly. Window film reduces AC load by rejecting solar heat at the glass — most customers see a 20–30% drop in their monthly electricity bill."},
            {"icon": "🌫️", "title": "Haze Season Protection", "text": "Chiang Mai's annual burning season (February–April) brings hazardous air quality. While window film doesn't filter air, it allows you to keep windows sealed while maintaining natural light — reducing the temptation to open windows during high-PM2.5 days."},
            {"icon": "🛡️", "title": "Furniture & Interior Protection", "text": "The intense northern sun fades wood furniture, silk textiles, and artwork rapidly. UV-blocking film protects your interiors from sun damage — especially important for Chiang Mai's many beautifully furnished Lanna-style homes and boutique properties."},
        ],
        "film_section_title": "Choose the Right Film for Your Chiang Mai Property",
        "film_section_sub": "Every film is professionally installed on-site. Free measurement included with every quote.",
        "film_popular_desc": "The top choice for Chiang Mai homes and condos. Nano-ceramic technology delivers excellent heat and glare reduction without a metallic appearance — preserving your view of Doi Suthep.",
        "film_uv400_desc": "Enhanced UV400 blocking for maximum skin and furniture protection. Ideal for Chiang Mai villas with large west-facing windows catching the intense afternoon sun.",
        "film_sputtering_desc": "Premium magnetron-sputtered film for maximum solar control. The preferred choice for Chiang Mai commercial buildings, co-working spaces, and luxury residences.",
        "process_sub": "We come to you anywhere in Chiang Mai — no need to remove windows or visit a workshop.",
        "process_step2_text": "Our technician visits your property — from Nimmanhaemin to Hang Dong — to measure all windows at no charge.",
        "process_step1_text": "Use our online quote tool or WhatsApp us with your property type and location in Chiang Mai.",
        "faq_title": "Common Questions About Window Tinting in Chiang Mai",
        "faqs": [
            {"q": "Do you serve areas outside Chiang Mai city centre?", "a": "Yes — we cover the entire Chiang Mai metropolitan area including Nimmanhaemin, Santitham, Hang Dong, San Kamphaeng, Mae Rim, and surrounding districts. We also serve properties in nearby Lamphun and Chiang Mai's outer ring areas."},
            {"q": "Will window film help during Chiang Mai's haze season?", "a": "While window film doesn't filter air, it allows you to keep windows sealed and still enjoy natural light. This reduces the need to open windows during high-PM2.5 days, helping you maintain better indoor air quality during the burning season."},
            {"q": "How long does installation take for a Chiang Mai villa?", "a": "A typical Chiang Mai villa (3–4 bedrooms) takes one full day. Smaller condos around Nimmanhaemin usually take 3–5 hours. Our team works cleanly and you can remain in the property during installation."},
            {"q": "Is window film effective in Chiang Mai's cool season?", "a": "Absolutely. Film provides insulation year-round — it keeps heat out during the hot season and helps retain warmth during cool-season mornings when temperatures can drop to 15°C. It also blocks UV rays consistently, regardless of temperature."},
            {"q": "What film do you recommend for properties with a Doi Suthep view?", "a": "Our Ceramic Nano and Ceramic UV400 films maintain high visible light transmission, so you keep your mountain views while blocking heat and UV. We also offer near-clear options for properties where preserving the view is the top priority."},
        ],
        "cta_title": "Ready to Tint Your Chiang Mai Property?",
        "cta_sub": "Get a free on-site measurement and no-obligation quote. We serve all Chiang Mai districts.",
    },
    {
        "name": "Phuket",
        "slug": "phuket",
        "meta_desc": "Best window tinting in Phuket — JaiDeeClear installs premium UV & heat-rejection film for villas, condos, hotels, and offices across Phuket. Free on-site measurement.",
        "hero_sub": "Phuket's tropical sun, salt air, and luxury property market demand the highest-quality window film. JaiDeeClear delivers professional on-site installation to villas, condos, and commercial properties across the island.",
        "stat_uv": "UV 12+",
        "stat_uv_label": "Phuket's Peak UV Index",
        "section_eyebrow_why": "Why Phuket",
        "section_title_why": "Phuket's Tropical Climate Demands Window Protection",
        "section_sub_why": "From Patong beachfront condos to Laguna villas, the island's relentless sun and salt air affect every property.",
        "reasons": [
            {"icon": "☀️", "title": "Relentless Tropical Sun", "text": "Phuket sits just 8° north of the equator, receiving intense solar radiation year-round. The UV index regularly exceeds 12, and the island's clear skies mean properties face direct sun exposure for most of the day. Quality window film blocks up to 99% of harmful UV rays."},
            {"icon": "🌡️", "title": "Year-Round Heat & Humidity", "text": "Phuket averages 31–34°C throughout the year with high humidity. Glass-heavy villas in Kamala, Bang Tao, and Rawai trap enormous amounts of solar heat. High-IRR window film can reduce indoor temperatures by up to 10°C, dramatically cutting cooling costs."},
            {"icon": "🏝️", "title": "Luxury Villa Protection", "text": "Phuket's luxury property market — from Layan pool villas to Surin hillside estates — features expansive floor-to-ceiling glass. These properties need premium film that rejects heat without compromising ocean views or architectural aesthetics."},
            {"icon": "💡", "title": "Slash Resort-Level AC Costs", "text": "Cooling costs for Phuket properties can be staggering, especially for villas with large glass areas. Window film reduces the AC load significantly — most property owners report 20–30% savings on electricity, which adds up quickly in Phuket's year-round heat."},
            {"icon": "🛡️", "title": "Storm & Safety Protection", "text": "Phuket's monsoon season brings heavy storms that can shatter unprotected glass. Our safety films (0.4 mm and 0.8 mm) hold broken glass in place, protecting occupants and interiors from flying debris — essential for beachfront and hillside properties."},
            {"icon": "🏨", "title": "Hotel & Hospitality Solutions", "text": "Phuket's hotels, resorts, and serviced apartments benefit from commercial-grade window film that reduces guest-room cooling costs, protects furnishings from UV fade, and enhances privacy — all without altering the property's exterior appearance."},
        ],
        "film_section_title": "Choose the Right Film for Your Phuket Property",
        "film_section_sub": "Every film is professionally installed on-site. Free measurement included with every quote.",
        "film_popular_desc": "The top choice for Phuket condos and villas. Nano-ceramic technology delivers excellent heat and glare reduction without a metallic appearance — preserving your Andaman Sea views.",
        "film_uv400_desc": "Enhanced UV400 blocking for maximum skin and furniture protection. Ideal for Phuket villas with large west-facing windows catching the intense sunset exposure.",
        "film_sputtering_desc": "Premium magnetron-sputtered film for maximum solar control. The preferred choice for Phuket luxury villas, resorts, and commercial properties requiring the highest TSER performance.",
        "process_sub": "We come to you anywhere on Phuket island — no need to remove windows or visit a workshop.",
        "process_step2_text": "Our technician visits your property — from Patong to Rawai — to measure all windows at no charge.",
        "process_step1_text": "Use our online quote tool or WhatsApp us with your property type and location in Phuket.",
        "faq_title": "Common Questions About Window Tinting in Phuket",
        "faqs": [
            {"q": "Do you cover all areas of Phuket island?", "a": "Yes — we serve the entire island including Patong, Kata, Karon, Kamala, Bang Tao, Laguna, Cherng Talay, Rawai, Chalong, and Phuket Town. We also serve properties on nearby islands accessible by road."},
            {"q": "Is window film suitable for beachfront properties with salt air?", "a": "Absolutely. Our ceramic and sputtering films are non-metallic and corrosion-resistant, making them ideal for Phuket's salt-air environment. Unlike metallic films, they won't oxidise or degrade from coastal exposure."},
            {"q": "How long does installation take for a Phuket villa?", "a": "A typical Phuket villa (3–5 bedrooms with large glass areas) takes 1–2 days depending on the number and size of windows. Condos usually take 3–5 hours. Our team works cleanly and you can remain in the property."},
            {"q": "Will film protect my furniture from fading?", "a": "Yes — Phuket's intense tropical sun causes rapid UV fading of furniture, curtains, and flooring. Our films block up to 99% of UV rays, dramatically slowing the fading process and protecting your investment in interior furnishings."},
            {"q": "Can you install film on hotel or resort properties?", "a": "Yes — we have extensive experience with Phuket hospitality properties. We offer commercial-grade films, flexible scheduling to minimise guest disruption, and volume pricing for large-scale installations."},
        ],
        "cta_title": "Ready to Tint Your Phuket Property?",
        "cta_sub": "Get a free on-site measurement and no-obligation quote. We serve all areas across Phuket island.",
    },
    {
        "name": "Pattaya",
        "slug": "pattaya",
        "meta_desc": "Best window tinting in Pattaya — JaiDeeClear installs premium UV & heat-rejection film for condos, houses, villas, and offices across Pattaya. Free on-site measurement.",
        "hero_sub": "Pattaya's beachfront condos, retirement homes, and commercial properties face intense solar glare and humidity year-round. JaiDeeClear delivers professional window film installation directly to your door across the entire Pattaya area.",
        "stat_uv": "UV 12",
        "stat_uv_label": "Pattaya's Peak UV Index",
        "section_eyebrow_why": "Why Pattaya",
        "section_title_why": "Pattaya's Coastal Climate Calls for Window Protection",
        "section_sub_why": "From Jomtien beachfront towers to Pratumnak hillside villas, the coastal city's sun and humidity affect every property.",
        "reasons": [
            {"icon": "☀️", "title": "Intense Coastal Sun", "text": "Pattaya's east-facing coastline means morning sun hits beachfront condos directly, while afternoon sun bakes west-facing units. The UV index regularly reaches 12, and the sea reflection amplifies glare. Quality window film blocks up to 99% of UV rays and cuts glare significantly."},
            {"icon": "🌡️", "title": "Year-Round Heat & Humidity", "text": "Pattaya averages 32–35°C with high humidity throughout the year. The large glass facades of condos along Beach Road, Jomtien, and Wongamat trap enormous solar heat. High-IRR film can reduce indoor temperatures by up to 10°C."},
            {"icon": "🏢", "title": "High-Rise Condo Living", "text": "Pattaya's skyline is dominated by high-rise condos — from the towers of Wongamat to the beachfront complexes of Jomtien. Floor-to-ceiling glass is standard, making heat-rejection film essential for comfortable living and manageable electricity bills."},
            {"icon": "💡", "title": "Cut Cooling Costs", "text": "Many Pattaya residents — especially retirees on fixed incomes — are sensitive to electricity costs. Window film reduces AC load by 20–30%, translating to significant monthly savings in a city where air conditioning runs nearly year-round."},
            {"icon": "🛡️", "title": "Privacy for Ground-Floor Units", "text": "Pattaya's dense development means many ground-floor condos and townhouses face directly onto streets or neighbouring buildings. Daytime privacy film lets light in while blocking the view from outside — a popular choice in areas like Pratumnak and South Pattaya."},
            {"icon": "🏠", "title": "Retirement Home Protection", "text": "Pattaya's large expat and retiree community lives in houses and villas across East Pattaya, Huay Yai, and Mabprachan. Window film protects furnishings from UV fade, reduces heat, and adds a layer of security — all important for long-term residents."},
        ],
        "film_section_title": "Choose the Right Film for Your Pattaya Property",
        "film_section_sub": "Every film is professionally installed on-site. Free measurement included with every quote.",
        "film_popular_desc": "The top choice for Pattaya condos and houses. Nano-ceramic technology delivers excellent heat and glare reduction without a metallic appearance — preserving your sea views.",
        "film_uv400_desc": "Enhanced UV400 blocking for maximum skin and furniture protection. Ideal for Pattaya beachfront units with direct east or west sun exposure.",
        "film_sputtering_desc": "Premium magnetron-sputtered film for maximum solar control. The preferred choice for Pattaya high-rise condos, commercial buildings, and luxury villas.",
        "process_sub": "We come to you anywhere in Pattaya — no need to remove windows or visit a workshop.",
        "process_step2_text": "Our technician visits your property — from Wongamat to Jomtien — to measure all windows at no charge.",
        "process_step1_text": "Use our online quote tool or WhatsApp us with your property type and location in Pattaya.",
        "faq_title": "Common Questions About Window Tinting in Pattaya",
        "faqs": [
            {"q": "Do you serve all areas of Pattaya?", "a": "Yes — we cover North Pattaya, Central Pattaya, South Pattaya, Jomtien, Pratumnak, Wongamat, Na Jomtien, Bang Saray, East Pattaya, Huay Yai, and Mabprachan. We also serve nearby Sriracha and Laem Chabang."},
            {"q": "Can you install film on high-rise condo windows?", "a": "Absolutely. We have extensive experience with Pattaya high-rises. Our team works from inside the unit — no scaffolding or external access needed. We've installed film in buildings across Wongamat, Jomtien, and Pratumnak."},
            {"q": "How long does installation take for a Pattaya condo?", "a": "A standard Pattaya condo (1–2 bedrooms) typically takes 3–5 hours. Larger units or houses may require a full day. Our team works cleanly and you can remain in the property during installation."},
            {"q": "Will film reduce glare from the sea?", "a": "Yes — this is one of the most popular reasons for window tinting in Pattaya. Our films significantly reduce solar glare while maintaining clear views of the coastline. Many beachfront residents report a dramatic improvement in screen visibility and eye comfort."},
            {"q": "Is window film a good investment for rental condos?", "a": "Definitely. Tinted condos in Pattaya command higher rental rates and attract longer-term tenants who value comfort. The electricity savings alone often cover the film cost within 1–2 years, making it an excellent investment for landlords."},
        ],
        "cta_title": "Ready to Tint Your Pattaya Property?",
        "cta_sub": "Get a free on-site measurement and no-obligation quote. We serve all Pattaya areas.",
    },
    {
        "name": "Nonthaburi",
        "slug": "nonthaburi",
        "meta_desc": "Best window tinting in Nonthaburi — JaiDeeClear installs premium UV & heat-rejection film for houses, condos, townhouses, and offices across Nonthaburi. Free on-site measurement.",
        "hero_sub": "As Bangkok's largest and fastest-growing suburb, Nonthaburi's new housing estates and riverside condos face the same extreme heat and UV as the capital. JaiDeeClear delivers professional window film installation across the entire province.",
        "stat_uv": "UV 13",
        "stat_uv_label": "Nonthaburi Peak UV Index",
        "section_eyebrow_why": "Why Nonthaburi",
        "section_title_why": "Nonthaburi's Rapid Growth Makes Window Tinting Essential",
        "section_sub_why": "From riverside condos along the Chao Phraya to sprawling housing estates in Bang Yai, Nonthaburi's properties need solar protection.",
        "reasons": [
            {"icon": "☀️", "title": "Same Extreme UV as Bangkok", "text": "Nonthaburi shares Bangkok's extreme UV index of 11–13 — classified as \"Extreme\" by the WHO. The province's newer developments often feature large glass areas that let in massive amounts of solar radiation without proper film protection."},
            {"icon": "🏘️", "title": "Booming Housing Estates", "text": "Nonthaburi's housing estates in Bang Yai, Bang Bua Thong, and Pak Kret are among Thailand's fastest-growing residential areas. New townhouses and detached homes with modern glass facades benefit enormously from heat-rejection film installed at move-in."},
            {"icon": "🏢", "title": "Riverside Condos & Mixed-Use", "text": "The Chao Phraya riverside in Nonthaburi is lined with modern condos and mixed-use developments. These glass-heavy buildings face intense afternoon sun from the west, making window film essential for comfortable living and lower electricity costs."},
            {"icon": "💡", "title": "Cut Electricity Costs", "text": "Nonthaburi residents face the same high electricity costs as Bangkok. Window film reduces AC load by 20–30%, and the savings are especially significant for larger townhouses and detached homes with multiple sun-exposed windows."},
            {"icon": "🛡️", "title": "Privacy in Dense Estates", "text": "Nonthaburi's housing estates are built at high density, with homes often close together. Daytime privacy film is a popular choice — it lets natural light in while preventing neighbours from seeing inside, maintaining comfort without curtains."},
            {"icon": "🚇", "title": "MRT Corridor Development", "text": "The Purple MRT line has driven rapid condo development along Nonthaburi's main corridors. These new buildings feature floor-to-ceiling glass that demands heat-rejection film for liveable indoor temperatures and reasonable electricity bills."},
        ],
        "film_section_title": "Choose the Right Film for Your Nonthaburi Property",
        "film_section_sub": "Every film is professionally installed on-site. Free measurement included with every quote.",
        "film_popular_desc": "The top choice for Nonthaburi townhouses and condos. Nano-ceramic technology delivers excellent heat and glare reduction without a metallic appearance — ideal for modern housing estates.",
        "film_uv400_desc": "Enhanced UV400 blocking for maximum skin and furniture protection. Recommended for Nonthaburi homes with large west-facing windows catching the intense afternoon sun.",
        "film_sputtering_desc": "Premium magnetron-sputtered film for maximum solar control. The preferred choice for Nonthaburi commercial buildings, riverside condos, and large detached homes.",
        "process_sub": "We come to you anywhere in Nonthaburi — no need to remove windows or visit a workshop.",
        "process_step2_text": "Our technician visits your property — from Pak Kret to Bang Yai — to measure all windows at no charge.",
        "process_step1_text": "Use our online quote tool or WhatsApp us with your property type and location in Nonthaburi.",
        "faq_title": "Common Questions About Window Tinting in Nonthaburi",
        "faqs": [
            {"q": "Do you serve all areas of Nonthaburi?", "a": "Yes — we cover the entire Nonthaburi province including Pak Kret, Bang Yai, Bang Bua Thong, Mueang Nonthaburi, Sai Noi, and all major housing estates. We also serve the adjacent areas of Pathum Thani."},
            {"q": "Can you install film on new-build homes?", "a": "Absolutely — and we recommend it. Installing window film at move-in protects your new furniture and flooring from day one, and you start saving on electricity immediately. Many Nonthaburi homeowners include window tinting in their move-in budget."},
            {"q": "How long does installation take for a Nonthaburi townhouse?", "a": "A standard 3-storey townhouse typically takes 4–6 hours. Larger detached homes may require a full day. Our team works cleanly and efficiently, and you can remain in the property during installation."},
            {"q": "Is there a difference in pricing between Nonthaburi and Bangkok?", "a": "Our pricing is the same across the Bangkok metropolitan area, which includes all of Nonthaburi. There are no additional travel fees for properties within the greater Bangkok region."},
            {"q": "Will window film help with noise reduction?", "a": "While window film is not primarily designed for noise reduction, the thicker safety films (0.4 mm and 0.8 mm) do provide a modest reduction in external noise — a nice bonus for properties near busy Nonthaburi roads or construction areas."},
        ],
        "cta_title": "Ready to Tint Your Nonthaburi Property?",
        "cta_sub": "Get a free on-site measurement and no-obligation quote. We serve all Nonthaburi districts.",
    },
    {
        "name": "Khon Kaen",
        "slug": "khon-kaen",
        "meta_desc": "Best window tinting in Khon Kaen — JaiDeeClear installs premium UV & heat-rejection film for houses, condos, offices, and commercial buildings across Khon Kaen. Free on-site measurement.",
        "hero_sub": "Khon Kaen's scorching Isan summers push temperatures above 40°C, making window film essential for comfortable living. JaiDeeClear delivers professional on-site installation to homes, offices, and commercial properties across the city.",
        "stat_uv": "UV 12",
        "stat_uv_label": "Khon Kaen Peak UV Index",
        "section_eyebrow_why": "Why Khon Kaen",
        "section_title_why": "Khon Kaen's Isan Heat Makes Window Tinting Essential",
        "section_sub_why": "From university-area condos to new housing estates on the bypass, Khon Kaen's fierce sun demands serious solar protection.",
        "reasons": [
            {"icon": "☀️", "title": "Extreme Dry-Season Heat", "text": "Khon Kaen's dry season (March–May) regularly exceeds 40°C — among the hottest temperatures in Thailand. The UV index reaches 12, and the flat Isan terrain offers no natural shade. Window film blocks up to 99% of UV rays and dramatically reduces indoor heat."},
            {"icon": "🌡️", "title": "Dramatic Seasonal Swings", "text": "Khon Kaen swings from cool-season mornings near 12°C to dry-season afternoons above 40°C. Window film provides year-round thermal regulation — keeping heat out in summer and helping retain warmth during the surprisingly cold Isan winter mornings."},
            {"icon": "🏙️", "title": "Booming Property Market", "text": "As Isan's commercial capital, Khon Kaen is experiencing rapid development — new condos near Khon Kaen University, housing estates along the bypass roads, and commercial buildings in the CBD. Modern glass facades need film from day one."},
            {"icon": "💡", "title": "Slash Cooling Costs", "text": "Electricity costs in Khon Kaen's hot season can be brutal, especially for homes and offices running AC at full capacity. Window film reduces the cooling load by 20–30%, delivering significant monthly savings during the hottest months."},
            {"icon": "🛡️", "title": "Protect Interiors from UV Damage", "text": "Khon Kaen's intense sun causes rapid fading of furniture, wood flooring, and fabrics. UV-blocking film preserves your interiors — especially important for the city's growing number of modern, well-furnished homes and offices."},
            {"icon": "🏢", "title": "Commercial & University District", "text": "Khon Kaen's commercial district and the area around Khon Kaen University feature modern office buildings and co-working spaces with extensive glazing. Commercial-grade film helps these buildings meet energy-efficiency goals while maintaining a professional appearance."},
        ],
        "film_section_title": "Choose the Right Film for Your Khon Kaen Property",
        "film_section_sub": "Every film is professionally installed on-site. Free measurement included with every quote.",
        "film_popular_desc": "The top choice for Khon Kaen homes and condos. Nano-ceramic technology delivers excellent heat and glare reduction — essential for surviving the Isan hot season in comfort.",
        "film_uv400_desc": "Enhanced UV400 blocking for maximum skin and furniture protection. Ideal for Khon Kaen properties with large windows facing the fierce afternoon sun.",
        "film_sputtering_desc": "Premium magnetron-sputtered film for maximum solar control. The preferred choice for Khon Kaen commercial buildings, offices, and large residential properties.",
        "process_sub": "We come to you anywhere in Khon Kaen — no need to remove windows or visit a workshop.",
        "process_step2_text": "Our technician visits your property — from the city centre to the bypass estates — to measure all windows at no charge.",
        "process_step1_text": "Use our online quote tool or WhatsApp us with your property type and location in Khon Kaen.",
        "faq_title": "Common Questions About Window Tinting in Khon Kaen",
        "faqs": [
            {"q": "Do you serve areas outside Khon Kaen city?", "a": "Yes — we cover the entire Khon Kaen province including the city centre, university area, bypass road estates, and surrounding districts. We can also serve properties in nearby Udon Thani and Maha Sarakham during scheduled visits."},
            {"q": "How effective is window film in Khon Kaen's extreme heat?", "a": "Very effective. Our high-IRR films can reduce indoor temperatures by up to 10°C even during Khon Kaen's hottest days. Combined with AC, this makes a dramatic difference in comfort and electricity costs during the March–May hot season."},
            {"q": "How long does installation take?", "a": "A standard Khon Kaen home (3 bedrooms) typically takes 4–6 hours. Condos take 3–4 hours. Larger properties or commercial buildings may require a full day or more. Our team works cleanly and you can remain in the property."},
            {"q": "Is window film worth it if I only run AC during hot season?", "a": "Absolutely. Even outside the hot season, window film blocks 99% of UV rays year-round, protecting your furniture and skin. During the hot season, the electricity savings alone can cover the cost of installation within 1–2 seasons."},
            {"q": "Do you offer commercial pricing for offices in Khon Kaen?", "a": "Yes — we offer volume pricing for commercial installations. Contact us via WhatsApp or our quote tool for a customised quote based on your total window area and film requirements."},
        ],
        "cta_title": "Ready to Tint Your Khon Kaen Property?",
        "cta_sub": "Get a free on-site measurement and no-obligation quote. We serve all Khon Kaen districts.",
    },
    {
        "name": "Hat Yai",
        "slug": "hat-yai",
        "meta_desc": "Best window tinting in Hat Yai (Songkhla) — JaiDeeClear installs premium UV & heat-rejection film for homes, shophouses, offices, and commercial buildings across Hat Yai. Free on-site measurement.",
        "hero_sub": "Hat Yai's tropical humidity, intense sun, and bustling commercial district make window film a smart investment. JaiDeeClear delivers professional on-site installation to homes, shophouses, and offices across southern Thailand's largest city.",
        "stat_uv": "UV 12+",
        "stat_uv_label": "Hat Yai Peak UV Index",
        "section_eyebrow_why": "Why Hat Yai",
        "section_title_why": "Hat Yai's Tropical Climate Demands Window Protection",
        "section_sub_why": "From Niphat Uthit shophouses to modern developments along Kanjanavanich Road, Hat Yai's sun and humidity affect every property.",
        "reasons": [
            {"icon": "☀️", "title": "Intense Tropical Sun", "text": "Hat Yai sits in Thailand's deep south, receiving intense equatorial sun year-round. The UV index regularly exceeds 12, and the city's mix of clear and humid days means UV exposure is consistently high. Quality window film blocks up to 99% of harmful UV rays."},
            {"icon": "🌡️", "title": "Heat & Humidity Year-Round", "text": "Hat Yai averages 32–35°C with high humidity throughout the year — there is no real cool season. Air conditioning runs constantly, and window film with high infrared rejection can reduce indoor temperatures by up to 10°C, cutting cooling costs significantly."},
            {"icon": "🏪", "title": "Shophouse & Commercial District", "text": "Hat Yai's famous commercial district — centred on Niphat Uthit Road and the market areas — features traditional shophouses with large glass frontages. Window film provides heat rejection, UV protection, and daytime privacy for these busy commercial properties."},
            {"icon": "💡", "title": "Lower Electricity Bills", "text": "With AC running nearly year-round in Hat Yai, electricity costs are a major expense. Window film reduces the cooling load by 20–30%, delivering consistent monthly savings — especially valuable for shophouse businesses and large commercial spaces."},
            {"icon": "🛡️", "title": "Storm Protection", "text": "Southern Thailand's monsoon season brings heavy rains and strong winds to Hat Yai. Safety films hold shattered glass in place during storms, protecting occupants and interiors — particularly important for ground-floor shophouses and exposed properties."},
            {"icon": "🏢", "title": "Modern Development Growth", "text": "Hat Yai is experiencing rapid modernisation with new condos, office buildings, and retail centres along Kanjanavanich Road and the PSU university area. These modern glass buildings need professional window film for energy efficiency and occupant comfort."},
        ],
        "film_section_title": "Choose the Right Film for Your Hat Yai Property",
        "film_section_sub": "Every film is professionally installed on-site. Free measurement included with every quote.",
        "film_popular_desc": "The top choice for Hat Yai homes and shophouses. Nano-ceramic technology delivers excellent heat and glare reduction — ideal for the city's year-round tropical heat.",
        "film_uv400_desc": "Enhanced UV400 blocking for maximum skin and furniture protection. Recommended for Hat Yai properties with large sun-exposed windows and merchandise displays.",
        "film_sputtering_desc": "Premium magnetron-sputtered film for maximum solar control. The preferred choice for Hat Yai commercial buildings, modern offices, and large retail spaces.",
        "process_sub": "We come to you anywhere in Hat Yai — no need to remove windows or visit a workshop.",
        "process_step2_text": "Our technician visits your property — from the city centre to Kanjanavanich Road — to measure all windows at no charge.",
        "process_step1_text": "Use our online quote tool or WhatsApp us with your property type and location in Hat Yai.",
        "faq_title": "Common Questions About Window Tinting in Hat Yai",
        "faqs": [
            {"q": "Do you serve areas outside Hat Yai city?", "a": "Yes — we cover the entire Hat Yai area including the city centre, Kanjanavanich corridor, PSU area, and surrounding Songkhla province districts. We also serve properties in nearby Songkhla town and Sadao."},
            {"q": "Is window film suitable for shophouse frontages?", "a": "Absolutely. Window film is one of the most popular upgrades for Hat Yai shophouses. It reduces heat entering through the glass frontage, protects merchandise from UV fading, and provides daytime privacy — all while maintaining visibility from inside."},
            {"q": "How long does installation take?", "a": "A standard Hat Yai home or shophouse typically takes 3–5 hours. Larger commercial properties may require a full day. Our team works cleanly and efficiently, and your business can remain open during installation."},
            {"q": "Will film help with Hat Yai's humidity issues?", "a": "While window film doesn't directly reduce humidity, by lowering indoor temperatures it reduces condensation on glass and helps your AC dehumidify more efficiently. This can make a noticeable difference in Hat Yai's consistently humid climate."},
            {"q": "Do you offer film for Hat Yai's new condo developments?", "a": "Yes — we work with both individual unit owners and property developers. For new developments, we offer bulk installation pricing and can coordinate with construction schedules for pre-occupancy installation."},
        ],
        "cta_title": "Ready to Tint Your Hat Yai Property?",
        "cta_sub": "Get a free on-site measurement and no-obligation quote. We serve all Hat Yai and Songkhla areas.",
    },
    {
        "name": "Udon Thani",
        "slug": "udon-thani",
        "meta_desc": "Best window tinting in Udon Thani — JaiDeeClear installs premium UV & heat-rejection film for houses, condos, offices, and commercial buildings across Udon Thani. Free on-site measurement.",
        "hero_sub": "Udon Thani's extreme Isan heat and thriving expat community make professional window film a smart investment. JaiDeeClear delivers on-site installation to homes, offices, and commercial properties across the city and surrounding areas.",
        "stat_uv": "UV 12",
        "stat_uv_label": "Udon Thani Peak UV Index",
        "section_eyebrow_why": "Why Udon Thani",
        "section_title_why": "Udon Thani's Isan Climate Makes Window Tinting Essential",
        "section_sub_why": "From expat homes near Nong Prajak Park to commercial buildings on Pho Si Road, Udon Thani's fierce sun demands protection.",
        "reasons": [
            {"icon": "☀️", "title": "Scorching Isan Summers", "text": "Udon Thani's hot season (March–May) pushes temperatures above 40°C with a UV index reaching 12. The flat Isan plateau offers no natural shade, and properties face unrelenting sun exposure. Quality window film blocks up to 99% of harmful UV rays."},
            {"icon": "🌡️", "title": "Extreme Temperature Range", "text": "Udon Thani experiences one of Thailand's widest temperature ranges — from cool-season mornings near 10°C to hot-season peaks above 42°C. Window film provides year-round thermal regulation, keeping interiors comfortable across all seasons."},
            {"icon": "🏡", "title": "Growing Expat Community", "text": "Udon Thani is one of Isan's most popular expat destinations, with a large community of retirees and families living in houses and villas around Nong Prajak Park, Ban Nong Saeng, and the outskirts. These homes benefit enormously from heat-rejection and UV-blocking film."},
            {"icon": "💡", "title": "Reduce Electricity Costs", "text": "Electricity bills in Udon Thani spike dramatically during the hot season when AC runs at full capacity. Window film reduces the cooling load by 20–30%, delivering meaningful savings — especially important for retirees on fixed incomes."},
            {"icon": "🛡️", "title": "Furniture & Interior Protection", "text": "Udon Thani's intense sun causes rapid fading of furniture, wood flooring, and fabrics. UV-blocking film preserves your interiors and extends the life of furnishings — a practical investment for long-term residents."},
            {"icon": "🏢", "title": "Commercial District Growth", "text": "Udon Thani's commercial centre along Pho Si Road and the areas around CentralPlaza are growing rapidly. Modern office buildings and retail spaces with extensive glazing need professional window film for energy efficiency and occupant comfort."},
        ],
        "film_section_title": "Choose the Right Film for Your Udon Thani Property",
        "film_section_sub": "Every film is professionally installed on-site. Free measurement included with every quote.",
        "film_popular_desc": "The top choice for Udon Thani homes and condos. Nano-ceramic technology delivers excellent heat and glare reduction — essential for surviving the Isan hot season comfortably.",
        "film_uv400_desc": "Enhanced UV400 blocking for maximum skin and furniture protection. Ideal for Udon Thani properties with large windows facing the fierce afternoon sun.",
        "film_sputtering_desc": "Premium magnetron-sputtered film for maximum solar control. The preferred choice for Udon Thani commercial buildings, offices, and large residential properties.",
        "process_sub": "We come to you anywhere in Udon Thani — no need to remove windows or visit a workshop.",
        "process_step2_text": "Our technician visits your property — from Nong Prajak to the outer ring road — to measure all windows at no charge.",
        "process_step1_text": "Use our online quote tool or WhatsApp us with your property type and location in Udon Thani.",
        "faq_title": "Common Questions About Window Tinting in Udon Thani",
        "faqs": [
            {"q": "Do you serve areas outside Udon Thani city?", "a": "Yes — we cover the entire Udon Thani province including the city centre, Nong Prajak area, Ban Nong Saeng, and surrounding districts. We can also serve properties in nearby Nong Khai during scheduled visits."},
            {"q": "Is window film effective in Udon Thani's extreme heat?", "a": "Very effective. Our high-IRR films can reduce indoor temperatures by up to 10°C even during Udon Thani's hottest days above 40°C. Combined with AC, this makes a dramatic difference in comfort and electricity costs."},
            {"q": "How long does installation take?", "a": "A standard Udon Thani home (3 bedrooms) typically takes 4–6 hours. Smaller condos take 3–4 hours. Our team works cleanly and you can remain in the property during installation."},
            {"q": "Do many expats in Udon Thani use window film?", "a": "Yes — window tinting is very popular among Udon Thani's expat community. Many long-term residents consider it one of the best home investments for comfort and energy savings in the Isan climate."},
            {"q": "Is window film also useful during Udon Thani's cool season?", "a": "Yes. While the cool season brings welcome relief from heat, UV rays remain strong year-round. Film continues to protect your furniture and skin, and the insulation properties help retain warmth during the surprisingly cold Isan mornings."},
        ],
        "cta_title": "Ready to Tint Your Udon Thani Property?",
        "cta_sub": "Get a free on-site measurement and no-obligation quote. We serve all Udon Thani districts.",
    },
    {
        "name": "Nakhon Ratchasima",
        "slug": "nakhon-ratchasima",
        "meta_desc": "Best window tinting in Nakhon Ratchasima (Korat) — JaiDeeClear installs premium UV & heat-rejection film for houses, condos, offices, and commercial buildings. Free on-site measurement.",
        "hero_sub": "Nakhon Ratchasima — known as Korat — is the gateway to Isan and Thailand's largest province. Its fierce dry-season sun and rapid urban growth make professional window film essential. JaiDeeClear delivers on-site installation across the city.",
        "stat_uv": "UV 12",
        "stat_uv_label": "Korat's Peak UV Index",
        "section_eyebrow_why": "Why Korat",
        "section_title_why": "Nakhon Ratchasima's Climate Makes Window Tinting Essential",
        "section_sub_why": "From the Thao Suranaree district to new estates along Mittraphap Road, Korat's intense sun affects every property type.",
        "reasons": [
            {"icon": "☀️", "title": "Fierce Dry-Season Sun", "text": "Nakhon Ratchasima's dry season (March–May) brings temperatures above 40°C with a UV index reaching 12. As Thailand's largest province by area, the flat terrain means properties face unrelenting sun exposure with no natural shade. Window film blocks up to 99% of UV rays."},
            {"icon": "🌡️", "title": "Wide Temperature Range", "text": "Korat swings from cool-season mornings near 12°C to dry-season peaks above 40°C. Window film provides year-round thermal regulation — keeping heat out during the brutal Isan summer and helping retain warmth during cool-season mornings."},
            {"icon": "🏙️", "title": "Rapid Urban Expansion", "text": "Korat is one of Thailand's fastest-growing cities, with new housing estates, condos, and commercial developments along Mittraphap Road and the bypass. Modern glass-heavy construction needs window film from day one for comfort and energy efficiency."},
            {"icon": "💡", "title": "Cut Electricity Costs", "text": "Air conditioning is essential during Korat's hot season, driving up electricity bills. Window film reduces the cooling load by 20–30%, delivering significant monthly savings — especially for larger homes and commercial spaces."},
            {"icon": "🛡️", "title": "Protect Interiors from UV", "text": "Korat's intense sun causes rapid fading of furniture, wood flooring, and textiles. UV-blocking film preserves your interiors — important for the city's growing number of well-furnished modern homes and the historic properties near Thao Suranaree monument."},
            {"icon": "🏢", "title": "Commercial & Industrial Hub", "text": "As Isan's gateway city, Korat hosts major commercial and industrial zones. Office buildings, factories, and retail centres with extensive glazing benefit from commercial-grade window film that improves energy efficiency and working conditions."},
        ],
        "film_section_title": "Choose the Right Film for Your Korat Property",
        "film_section_sub": "Every film is professionally installed on-site. Free measurement included with every quote.",
        "film_popular_desc": "The top choice for Korat homes and condos. Nano-ceramic technology delivers excellent heat and glare reduction — essential for comfortable living through the Isan hot season.",
        "film_uv400_desc": "Enhanced UV400 blocking for maximum skin and furniture protection. Ideal for Korat properties with large windows facing the fierce afternoon sun.",
        "film_sputtering_desc": "Premium magnetron-sputtered film for maximum solar control. The preferred choice for Korat commercial buildings, industrial facilities, and large residential properties.",
        "process_sub": "We come to you anywhere in Nakhon Ratchasima — no need to remove windows or visit a workshop.",
        "process_step2_text": "Our technician visits your property — from the city centre to the Mittraphap Road estates — to measure all windows at no charge.",
        "process_step1_text": "Use our online quote tool or WhatsApp us with your property type and location in Nakhon Ratchasima.",
        "faq_title": "Common Questions About Window Tinting in Nakhon Ratchasima",
        "faqs": [
            {"q": "Do you serve all areas of Nakhon Ratchasima?", "a": "Yes — we cover the entire Korat metropolitan area including the city centre, Mittraphap Road corridor, Suranaree area, and surrounding districts. We also serve properties near Khao Yai and Pak Chong during scheduled visits."},
            {"q": "How effective is window film in Korat's extreme heat?", "a": "Very effective. Our high-IRR films can reduce indoor temperatures by up to 10°C even during Korat's hottest days above 40°C. Combined with AC, this makes a dramatic difference in comfort and electricity costs."},
            {"q": "How long does installation take?", "a": "A standard Korat home (3 bedrooms) typically takes 4–6 hours. Condos take 3–4 hours. Larger commercial properties may require a full day or more. Our team works cleanly and you can remain in the property."},
            {"q": "Is window film a good investment for new-build homes in Korat?", "a": "Absolutely. Installing film at move-in protects your new furniture from day one and starts saving on electricity immediately. Many developers in the Korat area now recommend window tinting as part of the new-home setup."},
            {"q": "Do you serve the Khao Yai / Pak Chong area?", "a": "Yes — we regularly serve properties in the Khao Yai and Pak Chong area, which is popular for holiday homes and resorts. Contact us to schedule a visit during our Nakhon Ratchasima service trips."},
        ],
        "cta_title": "Ready to Tint Your Korat Property?",
        "cta_sub": "Get a free on-site measurement and no-obligation quote. We serve all Nakhon Ratchasima districts.",
    },
    {
        "name": "Chiang Rai",
        "slug": "chiang-rai",
        "meta_desc": "Best window tinting in Chiang Rai — JaiDeeClear installs premium UV & heat-rejection film for houses, villas, condos, and offices across Chiang Rai. Free on-site measurement.",
        "hero_sub": "Chiang Rai's hot-season temperatures rival Bangkok, and the city's growing community of retirees and digital nomads demands comfortable, energy-efficient homes. JaiDeeClear delivers professional window film installation across the city and surrounding areas.",
        "stat_uv": "UV 11+",
        "stat_uv_label": "Chiang Rai Peak UV Index",
        "section_eyebrow_why": "Why Chiang Rai",
        "section_title_why": "Chiang Rai's Climate Makes Window Tinting a Smart Investment",
        "section_sub_why": "From the White Temple district to Mae Fah Luang villas, Chiang Rai's seasonal extremes affect every property.",
        "reasons": [
            {"icon": "☀️", "title": "Hot-Season Intensity", "text": "Chiang Rai's hot season (March–May) pushes temperatures above 38°C with a UV index exceeding 11. Despite its northern location, the city receives intense solar radiation during these months. Quality window film blocks up to 99% of harmful UV rays year-round."},
            {"icon": "🌡️", "title": "Extreme Seasonal Swings", "text": "Chiang Rai experiences Thailand's widest temperature range — from cool-season mornings near 8°C to hot-season peaks above 38°C. Window film provides year-round insulation, keeping heat out in summer and helping retain warmth during the cold northern winter."},
            {"icon": "🏡", "title": "Retiree & Digital Nomad Community", "text": "Chiang Rai attracts a growing community of retirees and remote workers living in houses and villas around the city, Mae Chan, and Mae Sai. These residents value comfort and energy efficiency — window film delivers both while protecting furnishings from UV damage."},
            {"icon": "💡", "title": "Reduce Electricity Costs", "text": "While Chiang Rai's cool season offers relief, the hot season drives significant AC usage. Window film reduces cooling costs by 20–30% during the hottest months, and the UV protection works year-round regardless of temperature."},
            {"icon": "🛡️", "title": "Protect Art & Interiors", "text": "Chiang Rai is Thailand's art capital — home to the White Temple, Blue Temple, and a thriving creative community. Many homes and galleries feature valuable artwork and handcrafted furnishings that need UV protection from the intense northern sun."},
            {"icon": "🏔️", "title": "Mountain View Preservation", "text": "Chiang Rai properties often feature stunning views of the surrounding mountains and countryside. Our ceramic films reject heat and UV while maintaining high visible light transmission — so you keep your views without the solar punishment."},
        ],
        "film_section_title": "Choose the Right Film for Your Chiang Rai Property",
        "film_section_sub": "Every film is professionally installed on-site. Free measurement included with every quote.",
        "film_popular_desc": "The top choice for Chiang Rai homes and villas. Nano-ceramic technology delivers excellent heat and glare reduction without a metallic appearance — preserving your mountain views.",
        "film_uv400_desc": "Enhanced UV400 blocking for maximum skin and furniture protection. Ideal for Chiang Rai properties with large windows and valuable artwork or furnishings.",
        "film_sputtering_desc": "Premium magnetron-sputtered film for maximum solar control. The preferred choice for Chiang Rai commercial buildings, boutique hotels, and luxury residences.",
        "process_sub": "We come to you anywhere in Chiang Rai — no need to remove windows or visit a workshop.",
        "process_step2_text": "Our technician visits your property — from the city centre to Mae Fah Luang — to measure all windows at no charge.",
        "process_step1_text": "Use our online quote tool or WhatsApp us with your property type and location in Chiang Rai.",
        "faq_title": "Common Questions About Window Tinting in Chiang Rai",
        "faqs": [
            {"q": "Do you serve areas outside Chiang Rai city?", "a": "Yes — we cover the entire Chiang Rai province including the city centre, Mae Chan, Mae Sai, Chiang Saen, and Mae Fah Luang. We also serve properties in the Golden Triangle area during scheduled visits."},
            {"q": "Is window film useful during Chiang Rai's cool season?", "a": "Absolutely. While the cool season brings welcome relief from heat, UV rays remain strong year-round. Film continues to protect your furniture, artwork, and skin. The insulation properties also help retain warmth during Chiang Rai's cold mornings."},
            {"q": "How long does installation take?", "a": "A standard Chiang Rai home (3 bedrooms) typically takes 4–6 hours. Villas with large glass areas may require a full day. Our team works cleanly and you can remain in the property during installation."},
            {"q": "Will film protect artwork and antiques?", "a": "Yes — this is one of the most important benefits for Chiang Rai properties. Our films block up to 99% of UV rays, dramatically slowing the fading and degradation of artwork, textiles, and antique furnishings caused by sun exposure."},
            {"q": "Can you install film on boutique hotels and guesthouses?", "a": "Yes — we work with many hospitality properties in Chiang Rai. We offer flexible scheduling to minimise guest disruption and volume pricing for larger installations. Contact us for a customised commercial quote."},
        ],
        "cta_title": "Ready to Tint Your Chiang Rai Property?",
        "cta_sub": "Get a free on-site measurement and no-obligation quote. We serve all Chiang Rai districts.",
    },
]

# All city info for the footer and location links section
ALL_CITIES = [(c["name"], c["slug"]) for c in CITIES]

WHATSAPP_SVG = '''<svg class="whatsapp-icon" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/>
                    </svg>'''


def generate_footer_links(current_slug):
    """Generate footer location links with the current city marked active."""
    links = []
    for name, slug in ALL_CITIES:
        cls = ' footer-location-link--active' if slug == current_slug else ''
        links.append(f'                        <a href="window-tinting-{slug}.html" class="footer-location-link{cls}">{name}</a>')
    return "\n".join(links)


def generate_reasons_html(reasons):
    """Generate the 6 reason cards."""
    cards = []
    for r in reasons:
        cards.append(f'''                <div class="reason-card">
                    <div class="reason-icon">{r["icon"]}</div>
                    <h3>{r["title"]}</h3>
                    <p>{r["text"]}</p>
                </div>''')
    return "\n".join(cards)


def generate_faqs_html(faqs):
    """Generate FAQ items."""
    items = []
    for f in faqs:
        items.append(f'''                <div class="faq-item">
                    <p class="faq-question">{f["q"]}</p>
                    <p class="faq-answer">{f["a"]}</p>
                </div>''')
    return "\n".join(items)


def generate_faq_schema(city_name, faqs):
    """Generate FAQPage schema JSON-LD."""
    entries = []
    for f in faqs:
        entries.append(f'''        {{
          "@type": "Question",
          "name": "{f["q"]}",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "{f["a"]}"
          }}
        }}''')
    return ",\n".join(entries)


def generate_page(city):
    slug = city["slug"]
    name = city["name"]

    footer_links = generate_footer_links(slug)
    reasons_html = generate_reasons_html(city["reasons"])
    faqs_html = generate_faqs_html(city["faqs"])
    faq_schema_entries = generate_faq_schema(name, city["faqs"])

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{city["meta_desc"]}">
    <title>Best Window Tinting in {name} | JaiDeeClear</title>

    <!-- Canonical URL -->
    <link rel="canonical" href="https://jaideeclear.com/window-tinting-{slug}">

    <!-- Open Graph -->
    <meta property="og:title" content="Best Window Tinting in {name} | JaiDeeClear">
    <meta property="og:description" content="{city["meta_desc"]}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://jaideeclear.com/window-tinting-{slug}">

    <!-- LocalBusiness Schema Markup -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "JaiDeeClear Window Tinting — {name}",
      "description": "Premium window tinting services in {name}, Thailand. UV protection, heat rejection, and privacy film for residential and commercial properties.",
      "url": "https://jaideeclear.com/window-tinting-{slug}",
      "telephone": "+66655079694",
      "email": "jaideeclear@gmail.com",
      "areaServed": {{
        "@type": "City",
        "name": "{name}",
        "addressCountry": "TH"
      }},
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "{name}",
        "addressCountry": "TH"
      }},
      "openingHours": "Mo-Su 08:00-18:00",
      "priceRange": "฿฿",
      "sameAs": [
        "https://www.facebook.com/Jaideeclear",
        "https://www.instagram.com/jaideeclear"
      ],
      "hasOfferCatalog": {{
        "@type": "OfferCatalog",
        "name": "Window Tinting Films",
        "itemListElement": [
          {{
            "@type": "Offer",
            "itemOffered": {{
              "@type": "Service",
              "name": "Ceramic Nano Window Film",
              "description": "Nano-ceramic heat and UV rejection film, 5–7 year lifespan"
            }},
            "priceSpecification": {{
              "@type": "UnitPriceSpecification",
              "price": "90",
              "priceCurrency": "THB",
              "unitText": "per sq.ft"
            }}
          }},
          {{
            "@type": "Offer",
            "itemOffered": {{
              "@type": "Service",
              "name": "Sputtering Series Window Film",
              "description": "Premium magnetron-sputtered film for maximum solar control"
            }},
            "priceSpecification": {{
              "@type": "UnitPriceSpecification",
              "price": "155",
              "priceCurrency": "THB",
              "unitText": "per sq.ft"
            }}
          }}
        ]
      }}
    }}
    </script>

    <!-- FAQPage Schema -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
{faq_schema_entries}
      ]
    }}
    </script>

    <!-- Seline Analytics -->
    <script async src="https://cdn.seline.com/seline.js" data-token="900711a10bdeff9"></script>

    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background: #ffffff;
            color: #1d1d1f;
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
        }}

        .container {{ max-width: 980px; margin: 0 auto; padding: 0 22px; }}

        /* ── Header ── */
        header {{
            position: sticky; top: 0;
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid #e5e5e7;
            z-index: 100; padding: 20px 0;
        }}
        .header-content {{
            display: flex; justify-content: space-between; align-items: center;
            max-width: 980px; margin: 0 auto; padding: 0 22px;
        }}
        .logo-container {{ display: flex; align-items: center; gap: 12px; }}
        .logo-container a {{ display: flex; align-items: center; }}
        .header-nav {{ display: flex; align-items: center; gap: 24px; }}
        .nav-link {{
            font-size: 14px; color: #1d1d1f; text-decoration: none;
            font-weight: 500; transition: opacity 0.2s ease;
        }}
        .nav-link:hover {{ opacity: 0.7; }}
        .whatsapp-btn {{
            display: flex; align-items: center; gap: 8px;
            background: #25D366; color: white; padding: 10px 20px;
            border-radius: 24px; text-decoration: none; font-size: 14px;
            font-weight: 600; transition: all 0.2s ease;
            box-shadow: 0 2px 8px rgba(37,211,102,0.3);
        }}
        .whatsapp-btn:hover {{
            background: #20BA5A; transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(37,211,102,0.4);
        }}
        .whatsapp-icon {{ width: 20px; height: 20px; }}

        /* ── Hero ── */
        .hero {{
            background: linear-gradient(135deg, #1d1d1f 0%, #2d2d2f 100%);
            color: white; padding: 80px 0 72px; text-align: center;
        }}
        .hero-eyebrow {{
            font-size: 13px; font-weight: 600; text-transform: uppercase;
            letter-spacing: 0.1em; color: #f9a500; margin-bottom: 16px;
        }}
        .hero h1 {{
            font-size: 52px; font-weight: 700; letter-spacing: -0.03em;
            line-height: 1.1; margin-bottom: 20px;
        }}
        .hero h1 em {{ font-style: normal; color: #f9a500; }}
        .hero-sub {{
            font-size: 19px; color: #a8a8a8; max-width: 600px;
            margin: 0 auto 36px; line-height: 1.5;
        }}
        .hero-cta-group {{ display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }}

        .btn {{
            padding: 14px 28px; border-radius: 980px; font-size: 15px;
            font-weight: 600; border: none; cursor: pointer;
            transition: all 0.2s ease; text-decoration: none;
            display: inline-flex; align-items: center; justify-content: center; gap: 8px;
        }}
        .btn-primary {{ background: #f9a500; color: white; }}
        .btn-primary:hover {{ background: #e09400; transform: translateY(-1px); }}
        .btn-outline {{ background: transparent; color: white; border: 1.5px solid rgba(255,255,255,0.4); }}
        .btn-outline:hover {{ background: rgba(255,255,255,0.08); }}

        /* ── Stats bar ── */
        .stats-bar {{ background: #f5f5f7; border-bottom: 1px solid #e5e5e7; padding: 28px 0; }}
        .stats-grid {{ display: grid; grid-template-columns: repeat(4,1fr); text-align: center; }}
        .stat-item {{ padding: 0 16px; border-right: 1px solid #e5e5e7; }}
        .stat-item:last-child {{ border-right: none; }}
        .stat-number {{ font-size: 32px; font-weight: 700; color: #1d1d1f; letter-spacing: -0.02em; }}
        .stat-label {{ font-size: 13px; color: #6e6e73; margin-top: 4px; }}

        /* ── Sections ── */
        .section {{ padding: 72px 0; }}
        .section-alt {{ background: #f5f5f7; }}
        .section-header {{ text-align: center; margin-bottom: 52px; }}
        .section-eyebrow {{
            font-size: 13px; font-weight: 600; text-transform: uppercase;
            letter-spacing: 0.1em; color: #f9a500; margin-bottom: 12px;
        }}
        .section-header h2 {{ font-size: 40px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 16px; }}
        .section-header p {{ font-size: 17px; color: #6e6e73; max-width: 560px; margin: 0 auto; }}

        /* ── Reasons grid ── */
        .reasons-grid {{ display: grid; grid-template-columns: repeat(3,1fr); gap: 20px; }}
        .reason-card {{
            background: white; border-radius: 18px; padding: 32px 28px;
            border: 1px solid #e5e5e7; transition: all 0.2s ease;
        }}
        .reason-card:hover {{ box-shadow: 0 8px 24px rgba(0,0,0,0.08); transform: translateY(-2px); }}
        .reason-icon {{ font-size: 40px; margin-bottom: 16px; }}
        .reason-card h3 {{ font-size: 19px; font-weight: 600; margin-bottom: 10px; letter-spacing: -0.01em; }}
        .reason-card p {{ font-size: 14px; color: #6e6e73; line-height: 1.6; }}

        /* ── Film grid ── */
        .film-grid {{ display: grid; grid-template-columns: repeat(2,1fr); gap: 20px; }}
        .film-card {{
            background: white; border-radius: 18px; padding: 28px;
            border: 1px solid #e5e5e7; transition: all 0.2s ease; position: relative;
        }}
        .film-card:hover {{ box-shadow: 0 8px 24px rgba(0,0,0,0.08); transform: translateY(-2px); }}
        .film-card.popular {{ border: 2px solid #1d1d1f; }}
        .popular-badge {{
            position: absolute; top: -1px; left: 28px;
            background: #f9a500; color: white; padding: 5px 14px;
            font-size: 11px; font-weight: 700; text-transform: uppercase;
            letter-spacing: 0.06em; border-radius: 0 0 8px 8px;
        }}
        .film-card h3 {{ font-size: 22px; font-weight: 600; margin-bottom: 6px; letter-spacing: -0.01em; }}
        .film-lifespan {{ font-size: 13px; color: #86868b; margin-bottom: 12px; }}
        .film-price {{ font-size: 28px; font-weight: 700; color: #1d1d1f; margin-bottom: 4px; }}
        .film-price-unit {{ font-size: 13px; color: #86868b; margin-bottom: 16px; }}
        .film-desc {{ font-size: 14px; color: #6e6e73; line-height: 1.6; margin-bottom: 20px; }}
        .specs-row {{
            display: flex; gap: 16px; padding: 12px 0; border-top: 1px solid #e5e5e7;
            font-size: 12px; color: #6e6e73; font-weight: 500; flex-wrap: wrap;
        }}

        /* ── Process steps ── */
        .process-steps {{ display: grid; grid-template-columns: repeat(4,1fr); gap: 20px; }}
        .process-step {{ text-align: center; padding: 28px 20px; }}
        .step-number {{
            width: 48px; height: 48px; background: #1d1d1f; color: white;
            border-radius: 50%; display: flex; align-items: center;
            justify-content: center; font-size: 18px; font-weight: 700;
            margin: 0 auto 16px;
        }}
        .process-step h3 {{ font-size: 16px; font-weight: 600; margin-bottom: 8px; }}
        .process-step p {{ font-size: 13px; color: #6e6e73; line-height: 1.5; }}

        /* ── FAQ ── */
        .faq-list {{ max-width: 720px; margin: 0 auto; }}
        .faq-item {{ border-bottom: 1px solid #e5e5e7; padding: 24px 0; }}
        .faq-item:first-child {{ border-top: 1px solid #e5e5e7; }}
        .faq-question {{ font-size: 17px; font-weight: 600; margin-bottom: 10px; color: #1d1d1f; }}
        .faq-answer {{ font-size: 15px; color: #6e6e73; line-height: 1.6; }}

        /* ── CTA Banner ── */
        .cta-banner {{
            background: linear-gradient(135deg, #1d1d1f 0%, #2d2d2f 100%);
            border-radius: 24px; padding: 64px 48px; text-align: center;
            color: white; margin: 0 22px;
        }}
        .cta-banner h2 {{ font-size: 36px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 16px; }}
        .cta-banner p {{
            font-size: 17px; color: #a8a8a8; margin-bottom: 32px;
            max-width: 480px; margin-left: auto; margin-right: auto;
        }}

        /* ── Footer ── */
        footer {{ border-top: 1px solid #e5e5e7; padding: 40px 0; margin-top: 60px; }}
        .footer-content {{ text-align: center; }}
        .footer-locations {{ margin-bottom: 24px; }}
        .footer-locations h4 {{
            font-size: 13px; font-weight: 600; text-transform: uppercase;
            letter-spacing: 0.08em; color: #86868b; margin-bottom: 12px;
        }}
        .footer-location-links {{ display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; }}
        .footer-location-link {{
            font-size: 13px; color: #6e6e73; text-decoration: none;
            padding: 5px 12px; border: 1px solid #e5e5e7;
            border-radius: 980px; transition: all 0.2s ease;
        }}
        .footer-location-link:hover {{ border-color: #f9a500; color: #f9a500; }}
        .footer-location-link--active {{ background: #f9a500; color: white; border-color: #f9a500; }}
        .social-links {{ display: flex; justify-content: center; gap: 16px; margin-top: 24px; }}
        .social-links a {{ color: #f9a500; font-size: 24px; text-decoration: none; }}
        .social-links a:hover {{ color: #FFA500; }}
        .copyright {{ font-size: 12px; color: #86868b; margin-top: 16px; }}
        .copyright a {{ color: #86868b; }}

        /* ── Responsive ── */
        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 36px; }}
            .stats-grid {{ grid-template-columns: repeat(2,1fr); gap: 16px; }}
            .stat-item {{ border-right: none; border-bottom: 1px solid #e5e5e7; padding-bottom: 16px; }}
            .stat-item:nth-last-child(-n+2) {{ border-bottom: none; }}
            .reasons-grid {{ grid-template-columns: 1fr; }}
            .film-grid {{ grid-template-columns: 1fr; }}
            .process-steps {{ grid-template-columns: repeat(2,1fr); }}
            .section-header h2 {{ font-size: 30px; }}
            .cta-banner {{ padding: 40px 24px; margin: 0; border-radius: 0; }}
            .cta-banner h2 {{ font-size: 26px; }}
            .header-nav .nav-link {{ display: none; }}
        }}
    </style>
</head>
<body>

    <!-- ── Header ── -->
    <header>
        <div class="header-content">
            <div class="logo-container">
                <a href="index.html">
                    <img src="jdclogo.jpg" alt="JaiDee Clear Logo" style="height: 100px; width: auto; object-fit: contain;">
                </a>
            </div>
            <div class="header-nav">
                <a href="schedule.html" class="nav-link">Schedule</a>
                <a href="https://wa.me/+66655079694" target="_blank" class="whatsapp-btn">
                    {WHATSAPP_SVG}
                    Chat with Us
                </a>
            </div>
        </div>
    </header>

    <!-- ── Hero ── -->
    <section class="hero">
        <div class="container">
            <p class="hero-eyebrow">Window Tinting · {name}</p>
            <h1>Best Window Tinting<br>in <em>{name}</em></h1>
            <p class="hero-sub">
                {city["hero_sub"]}
            </p>
            <div class="hero-cta-group">
                <a href="schedule.html" class="btn btn-primary">Get a Free Quote</a>
                <a href="https://wa.me/+66655079694" target="_blank" class="btn btn-outline">
                    WhatsApp Us
                </a>
            </div>
        </div>
    </section>

    <!-- ── Stats bar ── -->
    <div class="stats-bar">
        <div class="container">
            <div class="stats-grid">
                <div class="stat-item">
                    <div class="stat-number">99%</div>
                    <div class="stat-label">UV Rays Blocked</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">{city["stat_uv"]}</div>
                    <div class="stat-label">{city["stat_uv_label"]}</div>
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

    <!-- ── Why {name} needs tinting ── -->
    <section class="section">
        <div class="container">
            <div class="section-header">
                <p class="section-eyebrow">{city["section_eyebrow_why"]}</p>
                <h2>{city["section_title_why"]}</h2>
                <p>{city["section_sub_why"]}</p>
            </div>
            <div class="reasons-grid">
{reasons_html}
            </div>
        </div>
    </section>

    <!-- ── Film options ── -->
    <section class="section section-alt">
        <div class="container">
            <div class="section-header">
                <p class="section-eyebrow">Our Films</p>
                <h2>{city["film_section_title"]}</h2>
                <p>{city["film_section_sub"]}</p>
            </div>
            <div class="film-grid">
                <!-- Carbon Series -->
                <div class="film-card">
                    <h3>Carbon Series</h3>
                    <p class="film-lifespan">Lifespan: 2–3 years</p>
                    <div class="film-price">฿50–70</div>
                    <div class="film-price-unit">per sq.ft</div>
                    <p class="film-desc">Our entry-level option — solid basic UV protection at a budget-friendly price point. Ideal for short-term rentals or properties where cost is the primary consideration.</p>
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
                    <p class="film-desc">{city["film_popular_desc"]}</p>
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
                    <p class="film-desc">{city["film_uv400_desc"]}</p>
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
                    <p class="film-desc">{city["film_sputtering_desc"]}</p>
                    <div class="specs-row">
                        <span>UVR: 99%</span>
                        <span>Max TSER</span>
                        <span>Best for: Commercial</span>
                    </div>
                </div>
            </div>

            <div style="text-align: center; margin-top: 36px;">
                <a href="schedule.html" class="btn btn-primary">See All Films &amp; Get a Quote</a>
            </div>
        </div>
    </section>

    <!-- ── How it works ── -->
    <section class="section">
        <div class="container">
            <div class="section-header">
                <p class="section-eyebrow">How It Works</p>
                <h2>Professional Installation, Delivered to Your Door</h2>
                <p>{city["process_sub"]}</p>
            </div>
            <div class="process-steps">
                <div class="process-step">
                    <div class="step-number">1</div>
                    <h3>Get a Quote</h3>
                    <p>{city["process_step1_text"]}</p>
                </div>
                <div class="process-step">
                    <div class="step-number">2</div>
                    <h3>Free Measurement</h3>
                    <p>{city["process_step2_text"]}</p>
                </div>
                <div class="process-step">
                    <div class="step-number">3</div>
                    <h3>Professional Install</h3>
                    <p>We install your chosen film cleanly and efficiently, typically completing a full property in a single day.</p>
                </div>
                <div class="process-step">
                    <div class="step-number">4</div>
                    <h3>Enjoy &amp; Save</h3>
                    <p>Start feeling the difference immediately — cooler rooms, lower electricity bills, and protected interiors.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- ── FAQ ── -->
    <section class="section section-alt">
        <div class="container">
            <div class="section-header">
                <p class="section-eyebrow">FAQ</p>
                <h2>{city["faq_title"]}</h2>
            </div>
            <div class="faq-list">
{faqs_html}
            </div>
        </div>
    </section>

    <!-- ── CTA Banner ── -->
    <section class="section" style="padding-bottom: 0;">
        <div class="cta-banner">
            <h2>{city["cta_title"]}</h2>
            <p>{city["cta_sub"]}</p>
            <div class="hero-cta-group">
                <a href="schedule.html" class="btn btn-primary">Get a Free Quote</a>
                <a href="https://wa.me/+66655079694" target="_blank" class="btn btn-outline">
                    WhatsApp Us
                </a>
            </div>
        </div>
    </section>

    <!-- ── Footer ── -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-locations">
                    <h4>Service Locations</h4>
                    <div class="footer-location-links">
{footer_links}
                    </div>
                </div>
                <div class="social-links">
                    <a href="https://www.facebook.com/Jaideeclear" target="_blank" aria-label="Facebook">
                        <i class="fab fa-facebook-f"></i>
                    </a>
                    <a href="https://www.instagram.com/jaideeclear" target="_blank" aria-label="Instagram">
                        <i class="fab fa-instagram"></i>
                    </a>
                </div>
                <p class="copyright">© 2025 JaiDeeClear. On-site service throughout Thailand · <a href="index.html">Home</a></p>
            </div>
        </div>
    </footer>

</body>
</html>'''

    return html


# ── Generate all 10 city pages ──
output_dir = os.path.dirname(os.path.abspath(__file__))
for city in CITIES:
    filename = f"window-tinting-{city['slug']}.html"
    filepath = os.path.join(output_dir, filename)
    html = generate_page(city)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✓ Generated {filename}")

print(f"\nDone — {len(CITIES)} city pages generated.")

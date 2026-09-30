from urllib.parse import quote

def enquire(text):return 'https://wa.me/919899631375?text='+quote(text)
weather='<div class="weather-pill" aria-label="Local weather"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 1v3m0 16v3M1 12h3m16 0h3M4 4l2 2m12 12 2 2M4 20l2-2M18 6l2-2"/></svg><span>Faldakot Malla <strong data-temperature>Checking weather…</strong><small data-weather-time>Current local estimate</small></span></div>'
longstay='''<section class="long-stay wrap" id="long-stay"><div><p class="eyebrow">7–28 DAYS · BY ARRANGEMENT</p><h2>Stay longer.<br><em>Settle deeper.</em></h2><p>Let the first few days be for arriving. Then make time for the book, the morning practice, the music or simply the peace you came looking for.</p><p>A quiet village home for an unhurried stay. Discuss your dates, meals, room needs and a personalised long-stay quote with the hosts.</p><div class="duration-options">'''+''.join(f'<a href="{enquire(f"Hello, I would like a peaceful {n}-night stay at Himalayan Hemp Eco Stay. Please share availability, pricing and inclusions.")}">{n} nights ↗</a>' for n in (7,14,28))+'''</div><p class="small-print">Subject to availability. Confirm connectivity and workspace needs before planning a working stay.</p></div><figure><img loading="lazy" src="/assets/quiet-exterior.webp" alt="Quiet moments beside the traditional stone house"><figcaption>A slower rhythm, rooted in village life.</figcaption></figure></section>'''
rituals='''<section class="daily-rhythm wrap"><div class="section-heading"><div><p class="eyebrow">A DAY AT YOUR OWN PACE</p><h2>Less to do.<br>More to feel.</h2></div><p>Bring your own practice.<br>Let quiet be part of the plan.</p></div><div class="rhythm-grid"><article><img loading="lazy" src="/assets/quiet-yoga.png" alt="Family sharing a gentle seated yoga practice in a traditional room"><p class="eyebrow">MORNINGS · BREATHE</p><h3>Begin softly.</h3><p>Make space for gentle movement, meditation or a few moments of stillness. Ask about a suitable practice space for your dates.</p></article><article><img loading="lazy" src="/assets/quiet-music.png" alt="A guest playing acoustic guitar in a traditional room"><p class="eyebrow">AFTERNOONS · CREATE</p><h3>Follow your own rhythm.</h3><p>Read, write, or discuss a little unamplified music with the hosts. Keep the volume gentle and respect the village’s quiet.</p></article></div><p class="small-print">Room arrangements and equipment vary. Please confirm any yoga, music or workspace requirements before booking.</p></section>'''
season='''<section class="season-section wrap"><p class="eyebrow">PLAN A THOUGHTFUL STAY</p><h2>Come prepared.<br>Leave the hurry behind.</h2><div class="season-grid"><article><span>01</span><h3>Choose your pace</h3><p>A short pause or several weeks: tell us what you need from your time here.</p></article><article><span>02</span><h3>Pack for the hills</h3><p>Bring layers, walking shoes, a torch and rain protection. Check the forecast and trail conditions before setting out.</p></article><article><span>03</span><h3>Know your welcome</h3><p>Agree meals, dietary needs, arrival support and room arrangements with the hosts before you travel.</p></article></div></section>'''
map_url='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3453.8721342440617!2d78.372778!3d30.040526!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xb46bcb2dedc59a05!2zMzDCsDAyJzI1LjkiTiA3OMKwMjInMjIuMCJF!5e0!3m2!1sen!2sin!4v1668445226158!5m2!1sen!2sin'
map_section='''<section class="location-section wrap"><div><p class="eyebrow">FIND YOUR WAY HERE</p><h2>A village in the hills.<br>A home worth finding.</h2><p>Faldakot Malla, Yamkeshwar<br>Pauri Garhwal, Uttarakhand 246121</p><p>The final approach is on foot. Confirm the roadhead and meeting point with the hosts; map directions do not replace the arrival instructions.</p><a class="button" href="https://www.google.com/maps/search/?api=1&amp;query=30.040526%2C78.372778" target="_blank" rel="noopener">Open location in Maps ↗</a><a class="text-link" href="/visit/">Plan your arrival →</a></div><iframe title="Himalayan Hemp Eco Stay location from the original website" src="'''+map_url+'''" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></section>'''

# Place-specific imagery and a quieter front-page sequence.
home=pages[''][1]
home=home.replace('/assets/house.jpg','/assets/cover-calm.webp').replace('The real Himalayan Hemp Eco Stay house, built with stone and lime, in Faldakot Malla','Himalayan Hemp Eco Stay in warm evening light')
home=home.replace('<p class="eyebrow">AN INTIMATE HIMALAYAN ESCAPE</p>',weather+'<p class="eyebrow">AN UNHURRIED HIMALAYAN STAY</p>')
home=home.replace('Some places<br>bring you <em>back.</em>','Stay a while.<br>Come back to <em>calm.</em>')
home=home.replace('A little closer to nature. A little closer to yourself.','For slow mornings, quiet days and longer stays.')
home=home.replace('<a class="button" href="/stay/">Discover your stay</a>','<a class="button" href="/stay/#long-stay">Plan a peaceful stay</a>')
home=home.replace('/assets/malla.jpg','/assets/quiet-yoga.png').replace('Real Malla bedroom with warm natural walls and wooden windows','A traditional interior for quiet moments')
home=home.replace('/assets/talla.jpg','/original/img/tariff/talla2.jpg').replace('Original stone hearth and timber details inside the house','Talla bedroom with warm earth walls and timber windows').replace('A HOME WITH SOUL','DISCOVER TALLA').replace('Warmth in<br>every detail.','Talla.<br>Your quiet corner.').replace('Stone, timber and hemp-lime finishes. Discover the textures that make this house its own.','Warm earth colours, timber windows and the character of a village home. Explore Talla’s bedroom, sitting area and attached bathroom.').replace('<a class="text-link" href="/house/">Inside the house →</a>','<a class="text-link" href="/stay/">Explore Talla &amp; all rooms →</a>')
home=re.sub(r'<section class="experiences.*?</section>',rituals,home,flags=re.S)
home=home.replace('<section class="landscape-feature">',longstay+'<section class="landscape-feature">')
home+=season+map_section
pages['']=(pages[''][0],home)
pages['stay']=(pages['stay'][0],longstay+pages['stay'][1])
pages['visit']=(pages['visit'][0],weather+pages['visit'][1]+map_section)
pages['retreats']=(pages['retreats'][0],pages['retreats'][1]+rituals)
pages['house']=(pages['house'][0],pages['house'][1]+rituals)

# Curate a calm gallery; retain the original files on disk but remove group/event images from display.
collections=[('House & landscape','gallery',[('/assets/cover-calm.webp','Evening at the hemp house'),('/assets/quiet-exterior.webp','Quiet moments by the house'),('/assets/room.jpg','The surrounding hills')]),('Rooms & interiors','tariff',[('/original/img/tariff/'+f,l) for f,l in room_names.items()]),('Quiet pursuits','activities',[('/assets/quiet-yoga.png','Space for a gentle practice'),('/assets/quiet-music.png','Room to read, write and create')])]
# Restore the original collection; omit only busy group/event photographs.
original_labels={
'gallery':{'gal1.jpg':'Layers of Himalayan hills','gal10.jpg':'Sunlight over the ridges','gal11.jpg':'An evening sky','gal12.jpg':'Farming in the village','gal14.jpg':'Clouds above village rooftops','gal2.jpg':'Traditional farming','gal3.jpg':'Hemp growing in the hills','gal4.jpg':'Village roofs and mountain clouds','gal5.jpg':'A quiet village companion','gal6.jpg':'Small details of home','gal8.jpg':'A pause beside the tent'},
'activities':{'farming.jpg':'Working with the land','hempcrete.jpg':'Hempcrete in the making','sunset.jpg':'Sunset in the hills','temple-meditation.jpg':'A hillside temple','tent.jpg':'Quiet camping moments','yoga.jpg':'A gentle outdoor practice'},
'sightseen':{'bungee.jpeg':'Adventure in the wider region','camping.jpeg':'Camps in the wider region','jhilmil-cave.jpeg':'Jhilmil Cave','mahafgarh.png':'Mahafgarh Temple','neelkanth-mahadev.jpeg':'Neelkanth Mahadev','ramjhula.jpeg':'Ram Jhula','yumkeshwar.jpeg':'Yamkeshwar Temple'}}
for group,labels in original_labels.items():
    items=[('/original/img/'+group+'/'+f,label) for f,label in labels.items() if (root/'original'/'img'/group/f).is_file()]
    if group=='gallery':collections[0][2].extend(items)
    elif group=='activities':collections[2][2].extend(items)
    # Regional images remain in the nearby-attractions section, not the gallery.
# One copy of each scene, including duplicates stored under different filenames.
import hashlib
omit={'/assets/room.jpg','/original/img/gallery/gal12.jpg','/original/img/gallery/gal14.jpg','/original/img/activities/farming.jpg','/original/img/activities/sunset.jpg','/original/img/activities/tent.jpg'}
seen=set()
for _,_,items in collections:
    unique=[]
    for src,alt in items:
        if src in omit:continue
        if src=='/original/img/gallery/gal1.jpg':src='/assets/hills-restored.png'
        fingerprint=hashlib.sha256((root/src.lstrip('/')).read_bytes()).hexdigest()
        if fingerprint in seen:continue
        seen.add(fingerprint);unique.append((src,alt))
    items[:]=unique
filters='<div class="gallery-filters wrap" aria-label="Filter photographs"><button class="active" data-filter="all" aria-pressed="true">All photographs</button>'+''.join(f'<button data-filter="{key}" aria-pressed="false">{label}</button>' for label,key,_ in collections)+'</div><p class="gallery-count wrap" role="status"></p>'
gallery_body=section('QUIET SPACES. NATURAL TEXTURES.','A slower way<br>of seeing.','Explore the house, its rooms and the calm surroundings. Select a photograph to take a closer look.')+filters
for label,key,items in collections:
    gallery_body+=f'<section class="gallery-section wrap" data-category="{key}"><h2>{label}</h2><div class="photo-grid">'+''.join(f'<figure><img loading="lazy" src="{src}" alt="{alt}"><figcaption>{alt}</figcaption></figure>' for src,alt in items)+'</div></section>'
pages['gallery']=('Gallery',gallery_body)
for key,(title,body) in list(pages.items()):
    body=body.replace('/assets/hemp.jpg','/assets/quiet-exterior.webp').replace('Hempcrete natural building activity','Stone and natural building details of the house')
    body=body.replace('/assets/landscape.jpg','/assets/quiet-exterior.webp').replace('/assets/view.jpg','/assets/quiet-yoga.png')
    pages[key]=(title,body)
footer=footer.replace('<a href="/stay/">Stays & residencies</a>','<a href="/stay/#long-stay">Long stays for calm & peace</a>')
footer=footer.replace('<span>© 2026 Himalayan Hemp Eco Stay</span>','<span>© 2026 Himalayan Hemp Eco Stay<br>Weather: <a href="https://www.met.no/" target="_blank" rel="noopener">MET Norway</a> · <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC BY 4.0</a> · rounded local forecast estimate.</span>')

# Give the full guestbook a clear route from the homepage.
review_link='<p class="all-reviews"><a class="button" href="/reviews/#guestbook-archive">View all 11 guestbook notes ↗</a></p>'
pages['']=(pages[''][0],pages[''][1].replace('<section class="guestbook wrap">','<section class="guestbook wrap">'+review_link))
pages['reviews']=(pages['reviews'][0],pages['reviews'][1].replace('<section class="gallery-section wrap">','<section class="gallery-section wrap" id="guestbook-archive">').replace('<h2>The guestbook archive</h2>','<h2>All 11 guestbook notes</h2><p>Original handwritten memories, preserved together. Select a note to read it at full size.</p>'))

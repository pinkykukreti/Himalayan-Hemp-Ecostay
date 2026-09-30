import re

room_names={'malla1.jpg':'Malla · Twin beds & natural finishes','malla2.jpg':'Malla · Another perspective','talla1.jpg':'Talla · Stone & timber interior','talla2.jpg':'Talla · Bedroom details','talla3.jpg':'Talla · A closer look','attach-toilet-talla.jpg':'Talla · Attached bathroom'}
rooms='<section class="stay-rooms wrap"><div class="section-heading"><div><p class="eyebrow">INSIDE YOUR STAY</p><h2>Every room.<br>Every quiet detail.</h2></div><p>Explore all six room, interior and bathroom photographs.<br>Select a photograph for a closer look.</p></div><div class="room-collection">'
for filename,label in room_names.items():
    rooms+=f'<figure><img loading="lazy" src="/original/img/tariff/{filename}" alt="{label}"><figcaption>{label}</figcaption></figure>'
rooms+='</div></section>'
pages['stay']=(pages['stay'][0],re.sub(r'<section class="room-gallery.*?</section>','',pages['stay'][1],count=1)+rooms)

quotes=[('“We hope we will be back soon!”','A note from our guestbook','testimonial1.jpg'),('“I would’ve loved to stay for longer.”','A note from our guestbook','testimonial2.jpg'),('“Thank you so much for this wonderfully unique experience in your village.”','Jack & Miranda · Guestbook','testimonial3.jpg')]
reviews='<section class="guestbook wrap"><div class="section-heading"><div><p class="eyebrow">WORDS LEFT BEHIND</p><h2>Remembered<br>with warmth.</h2></div><p>Excerpts from the original guestbook.<br><a href="https://www.airbnb.co.in/rooms/30969567">Read current Airbnb reviews ↗</a></p></div><div class="review-cards">'
for quote,who,file in quotes:
    reviews+=f'<article><span class="quote-mark" aria-hidden="true">“</span><blockquote>{quote}</blockquote><p>{who}</p><details><summary>View the original note</summary><img loading="lazy" src="/original/img/testimonials/{file}" alt="Original handwritten guestbook note"></details></article>'
reviews+='</div></section>'
pages['']=(pages[''][0],re.sub(r'<section class="reviews.*?</section>',reviews,pages[''][1],flags=re.S))
pages['reviews']=('Guest stories',reviews+'<section class="gallery-section wrap"><h2>The guestbook archive</h2><div class="review-archive">'+''.join(f'<figure><img loading="lazy" src="/original/{v}" alt="Original guestbook page"><figcaption>From our guestbook</figcaption></figure>' for v in assets if '/testimonials/' in v and (root/'original'/v).is_file())+'</div></section>')

filters='<div class="gallery-filters wrap" aria-label="Filter photographs"><button class="active" data-filter="all" aria-pressed="true">All photographs</button>'
gallery_html=''
for heading,folder in groups:
    if folder=='testimonials': continue
    filters+=f'<button data-filter="{folder}" aria-pressed="false">{heading}</button>'
    gallery_html+=f'<section class="gallery-section wrap" data-category="{folder}"><h2>{heading}</h2><div class="photo-grid">'
    for v in assets:
        if '/'+folder+'/' not in v or not (root/'original'/v).is_file():continue
        label=room_names.get(Path(v).name,heading if folder=='gallery' else Path(v).stem.replace('-',' ').title())
        gallery_html+=f'<figure><img loading="lazy" src="/original/{v}" alt="{escape(label)}"><figcaption>{escape(label)}</figcaption></figure>'
    gallery_html+='</div></section>'
filters+='</div><p class="gallery-count wrap" role="status"></p>'
pages['gallery']=('Gallery',section('THE HOUSE. THE DETAILS. THE HILLS.','A place to linger.','Explore the real rooms, village life and landscapes that shape a stay here. Filter by interest and select a photograph to enlarge it.')+filters+gallery_html)

form='''<section class="retreat-planner wrap"><aside><p class="eyebrow">A GATHERING WITH PURPOSE</p><h2>Tell us what<br>you imagine.</h2><p>Share a few details and we can explore whether the house is right for your group.</p><ol><li>Your idea and preferred dates</li><li>A conversation about space and access</li><li>A tailored proposal before you book</li></ol><p class="form-honesty">This prepares an email for you to review and send. It does not reserve dates.</p><a class="text-link" href="https://wa.me/919899631375">Prefer WhatsApp? Talk to us ↗</a></aside><form id="enquiry"><p class="eyebrow">START A RETREAT CONVERSATION</p><fieldset><legend>01 · About you</legend><div class="fields"><label>Your name<input name="name" autocomplete="name" required maxlength="100" placeholder="Full name"></label><label>Email address<input name="email" type="email" autocomplete="email" required placeholder="you@example.com"></label></div></fieldset><fieldset><legend>02 · Your gathering</legend><div class="fields"><label>Type of retreat<select name="type" required><option value="">Choose a focus</option><option>Yoga & meditation</option><option>Art & writing</option><option>Architecture & natural building</option><option>Leadership & research</option><option>Other intimate gathering</option></select></label><label>Expected guests<input name="guests" type="number" min="1" max="100" required placeholder="Group size"></label><label>Preferred arrival<input name="arrival" type="date" required></label><label>Preferred departure<input name="departure" type="date" required></label></div><label class="check"><input name="flexible" type="checkbox" value="Yes"> My dates are flexible</label></fieldset><fieldset><legend>03 · What matters to your group?</legend><label>Your plans<textarea name="message" rows="4" required maxlength="3000" placeholder="Your intention, space needs, food preferences or access questions…"></textarea></label><label class="check"><input type="checkbox" required> I understand the house is reached on foot and drinking alcohol, loud music and disruptive noise are prohibited.</label></fieldset><button class="button" type="submit">Prepare my enquiry ↗</button><p id="form-status" role="status"></p></form></section>'''
pages['retreats']=(pages['retreats'][0],re.sub(r'<section class="form-section.*?</section>',form,pages['retreats'][1],flags=re.S))
note='<section class="village-note wrap"><p class="eyebrow">PLEASE HONOUR OUR VILLAGE</p><h2>Peace is part of the welcome.</h2><div class="house-rules"><span>Drinking alcohol is prohibited</span><span>No loud music or parties</span><span>No disruptive noise</span></div><p>Our home belongs to a living village. Please respect local traditions, neighbours and the quiet surroundings that make this place special.</p></section>'
icons={
'Instagram':'<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".7"/></svg>',
'Facebook':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 21v-8h3l.5-4H14V7c0-1 .5-2 2-2h2V2h-3c-4 0-5 2-5 5v2H7v4h3v8"/></svg>',
'WhatsApp':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 18 2 22l5-1a10 10 0 1 0-3-3Z"/><path d="M8 7c-1 4 3 8 7 9l2-2-3-2-1 1-2-2 1-1-2-3Z"/></svg>'}
for label,icon in icons.items():footer=footer.replace('>'+label+' ↗','>'+icon+label+' ↗')
footer=footer.replace('<a href="/gallery/">Photo gallery</a>','<a href="/gallery/">Photo gallery</a><a href="/reviews/">Guest stories</a>')

pages['gallery']=(pages['gallery'][0],pages['gallery'][1].replace(filters,'<section class="gallery-feature wrap"><img loading="lazy" src="/assets/house-ai.png" alt="Himalayan Hemp Eco Stay exterior"><p>The house in the Himalayas</p></section>'+filters))
rule_paths=['<path d="M7 3h10v4a5 5 0 0 1-10 0V3Zm5 9v9m-4 0h8"/>','<path d="M9 18V5l10-2v13M9 8l10-2"/><circle cx="6" cy="18" r="3"/><circle cx="16" cy="16" r="3"/>','<path d="M4 9h4l5-4v14l-5-4H4V9Zm12-2a7 7 0 0 1 0 10"/>']
for label,path in zip(['Drinking alcohol is prohibited','No loud music or parties','No disruptive noise'],rule_paths):
    note=note.replace('<span>'+label,'<span><svg viewBox="0 0 24 24" aria-hidden="true">'+path+'<path d="M3 3l18 18"/></svg>'+label)

# Run the website on your laptop

1. Extract Himalayan-Hemp-Website.zip to a folder.
2. Install Python 3 if it is not already installed.
3. Open a terminal in that folder and run:

   python run-local.py

4. Open http://127.0.0.1:8000 in your browser. Keep the terminal open; press Ctrl+C to stop.

On Windows, `py run-local.py` also works. On macOS, use `python3 run-local.py`.
Do not open index.html by double-clicking: the website needs a local HTTP server for its page links.

## Edit the website

- `build.py`: page text, navigation, logo and footer.
- `home.html`: homepage content.
- `dist/style.css`: visual design and mobile layouts.
- `dist/main.js`: navigation, clickable photo viewer and enquiry form.
- `dist/original/`: photos and logo copied from the original website.
- Run `python build.py` after editing page content, then refresh the browser.
- All images are local. Google Fonts needs internet; system fonts are used offline.

## Included updates

Original logo; expanded contact/navigation/social footer; gallery with a single-photo viewer; quiet-village note prohibiting alcohol consumption, loud music and disruptive noise.

54 available original image assets were copied. The original site's img/gallery/gal13.jpg returns HTTP 404 and could not be included. Social icon assets and the logo are retained; the gallery includes all available photos from the original homepage/gallery/review pages.

Direct email delivery was deferred at your request. The enquiry form continues to open an email draft for the visitor to review and send. No backend, password or mail-service subscription is required to preview this website.

For public hosting, upload the contents of `dist` to the domain root. The current private review site does not replace your existing public domain.

Latest revision: edge-to-edge cover, non-overlapping hero text, single-photo viewer, refreshed gallery and navigation, rule icons and back-to-top button. Browser checks passed at 320, 390, 768, 1024 and 1440 px.

For business readiness, next confirm current room capacity, prices/inclusions, cancellation terms and arrival support. Direct enquiry delivery still needs your email-service setup. These facts should be verified before advertising packages.

## Calm long-stay update
- Your supplied cover and exterior photographs, plus edited yoga/music interiors.
- Group/event photos removed from the visible gallery (original files retained in the source archive).
- 7/14/28-night WhatsApp enquiry links; prices and availability are confirmed by the hosts.
- Map uses the pin from your original website. Confirm the final walking route with the hosts.
- Temperature uses MET Norway, fetched in the browser and cached for at least one hour. It is a local forecast estimate, not a property sensor. No API key is required. Offline or on failure it says Weather unavailable. Attribution is in the footer.
- For high traffic, move weather requests behind a caching backend in accordance with the provider terms: https://api.met.no/doc/TermsOfService
- Main new content: calm.py; styling: dist/calm.css; weather: dist/weather.js.
- Images show suggested quiet activities; confirm room arrangements and equipment before promising availability.


## Latest content refinements (30 September 2026)
`refinements.py` adds Google review excerpts, nearby attractions, sunrise/sunset and room comparison. Gallery duplicates are excluded in `calm.py`. Original files are retained.
Google rating and excerpts are a dated, manually checked snapshot, not an automatically updated feed. Refresh the values after checking the listing. Attraction distances come from the original property website and require host confirmation.

## GitHub
No GitHub remote is configured in this checkout. Upload the project source, including `dist`, `build.py`, `premium.py`, `calm.py`, `refinements.py`, `home.html` and `images.json`, to your chosen repository. Do not upload credentials or temporary archives. Publish `dist` at a domain root. For GitHub Pages, prefer a custom domain or user site: a repository subpath requires adapting absolute asset and navigation paths.


## Hemp living positioning — 1 October 2026
`positioning.py` applies the latest headline, Experience Hemp page, three guest segments, builder trial stay and workshop enquiry options. Keep it with the other build modules. Farm access and the Experience Center are labelled planned. Update their status only when ready; no workshop dates or prices are invented.

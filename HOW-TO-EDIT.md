# Jose's Compadre Mexican Grill: website

A small site with the menu, catering, a call button, directions, Facebook, and Toast online ordering. It is plain HTML, so GitHub Pages can host it for free.

## Files
- `index.html`: the main page, with the logo embedded.
- `lunch.html`: the lunch page, with daily specials, lunch plates and lunch fajitas. GitHub Pages serves it at `/lunch`, so links leave off `.html`. Opening the files straight from your computer won't follow those links; test on the live site.
- `build.py`: all the menu, lunch and catering data lives here. `LUNCH` and `DAILY` hold the lunch page items.
- `template.html`: the page design.
- `logo.png`: the logo with its background removed.
- `photo-*.webp`: the food and restaurant photos. To add a photo, save it as `photo-<name>.webp` and list `<name>` in `GALLERY_FOOD` or `GALLERY_PLACE` in `build.py`.

Everything in the `upload-to-github` folder goes in the repo. `README.md` and the `readme-*.jpg` screenshots are the project write-up shown on the GitHub repo page.

## Updating the menu or prices
1. Edit the item in `build.py`. Each line is `("Name", "price", "description")`.
2. Run `python3 build.py`. This rebuilds `index.html` and `lunch.html`.
3. Commit and push. The live site updates in about a minute.

## Publishing on GitHub Pages
1. Create a new public repo, for example `joses-compadre`.
2. Click **Add file → Upload files**, select everything in `upload-to-github`, and commit.
3. In the repo, go to **Settings → Pages → Build and deployment**, choose **Deploy from a branch**, then pick **main** and **/ (root)**.
4. The site goes live at `https://<username>.github.io/joses-compadre/`.

## Custom domain (optional, about $10–15 a year)
Buy a domain such as josescompadre.com from Cloudflare, Porkbun or Namecheap. Then:
1. Enter the domain under **Settings → Pages → Custom domain**. This creates a `CNAME` file.
2. At your registrar, add these DNS records:
   - An `A` record for `@` pointing to each of GitHub's IPs: `185.199.108.153`, `185.199.109.153`, `185.199.110.153` and `185.199.111.153`.
   - A `CNAME` record for `www` pointing to `<username>.github.io`.
3. Check **Enforce HTTPS** once it becomes available.

## Before cancelling Squarespace
- Update the website link on the Facebook page.
- Update the website link on the Google Business Profile.
- Update the website link in Toast.

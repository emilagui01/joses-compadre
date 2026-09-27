# Builds index.html from the menu data below.
# To update the menu: edit MENU / CATERING, then run:  python3 build.py
import base64, html, json

PHONE_DISPLAY = "(501) 945-7979"
PHONE_TEL = "+15019457979"
ADDRESS_1 = "11100 Highway 165"
ADDRESS_2 = "North Little Rock, AR 72117"
TOAST = "https://order.toasttab.com/online/joses-compadre-mexican-grill-11100-hwy-165"
FACEBOOK = "https://www.facebook.com/people/Joses-Compadre-Mexican-Grill-Cantina-Restaurant/100063804210612/"
MAPS_Q = "Jose's Compadre Mexican Grill, 11100 Hwy 165, North Little Rock, AR 72117"

# Each item: (name, price, description) — price may be "" when options carry the prices.
MENU = [
 ("appetizers", "Appetizers", None, [
  ("Sampler Platter", "15.99", "Taquitos, flautas, wings, chicken quesadilla, beef nachos & a small queso dip, with guacamole, sour cream & pico de gallo."),
  ("De'ann Special", "12.99", "Steak, grilled chicken & shrimp with white cheese dip, pico de gallo & 3 tortillas."),
  ("Queso Fundido", "9.99", "Chorizo & cheese with sliced jalapeños & 3 tortillas."),
  ("Wings", "11.99", "8 pieces. Flavors: dry rub, caliente, spicy honey or BBQ."),
  ("Taquitos", "10.79", "8 small fried corn tortillas with small queso dip, sour cream, guacamole & pico de gallo."),
  ("Flautas", "11.29", "8 small fried flour tortillas stuffed with chicken or beef, with small queso dip, sour cream, guacamole & pico de gallo."),
  ("Bean Dip", "Sm $6.58 · Lg $8.58", "A rich cheese dip with beans."),
  ("White Queso", "Sm $5.29 · Lg $7.29", "A rich cheese dip. Add ground beef or chorizo 1.29"),
  ("Yellow Queso", "Sm $5.29 · Lg $7.29", "A rich cheese dip. Add ground beef or chorizo 1.29"),
 ]),
 ("specials", "House Specials", None, [
  ("A1 Compadre Special", "15.29", "Grilled steak & chicken with taquitos, with guacamole, pico de gallo, sour cream, frijoles charros, rice & 3 flour tortillas."),
  ("A2 Enchiladas Rancheras", "13.29", "3 enchiladas (chicken, beef or cheese) topped with Monterey Jack & pico de gallo, with rice & beans."),
  ("A3 Chicken Monterrey", "13.29", "Broiled chicken breast with refried beans & rice. Add grilled onions & bell peppers 1.00"),
  ("A4 Taquitos Dinner", "12.99", "Fried corn tortillas stuffed with beef, topped with lettuce, sour cream & guacamole, with rice & beans."),
  ("A5 Pancho Villa", "12.29", "One cheese enchilada, one beef enchilada & one taco, with rice & beans."),
  ("A6 Enchiladas Supremas", "13.29", "Two grilled chicken enchiladas with bell peppers & onions, topped with sour cream sauce, with rice & frijoles charros."),
  ("A7 Shrimp Ranchero", "16.29", "Shrimp with sautéed onions & bell peppers, topped with cheese, with 3 flour tortillas, rice & beans."),
  ("A8 Compadre Favorite Shrimp", "16.29", "Shrimp grilled with bacon & Monterey Jack, with rice & beans."),
  ("A9 Chimichanga Grande", "13.99", "Flour tortilla stuffed with steak or chicken breast, beans & cheese, fried golden brown and topped with your favorite sauce. With guacamole, olives, tomatoes, lettuce & sour cream."),
  ("A10 Chimichanga", "12.29", "Ground beef or shredded chicken with beans & cheese, fried golden brown, with lettuce, tomatoes, black olives, guacamole & sour cream. With grilled chicken or steak 13.29"),
  ("A11 Carne Asada", "15.29", "Tender beef grilled with a tasty salsa (spicy, just enough), with rice & beans. Add shrimp 17.29"),
  ("A12 Dos Amigos", "16.29", "Grilled chicken & shrimp with onions & mushrooms, topped with Monterey Jack, with frijoles charros, guacamole, sour cream & 3 flour tortillas."),
  ("A13 Chimichanga", "11.29", "Ground beef or shredded chicken & beans, fried golden brown, with rice & beans. With grilled chicken or steak 12.29"),
  ("A14 Camarones a la Diabla", "16.99", "Grilled shrimp in our secret fiery sauce with grilled onions & mushrooms, rice, beans & 3 tortillas."),
  ("A15 Shrimp al Mojo de Ajo", "16.99", "Shrimp in garlic mojo sauce with rice, beans, sautéed vegetables & 3 flour tortillas."),
  ("A16 Tilapia Fish Tacos", "12.29", "2 lightly breaded tilapia fillets on soft tacos with lettuce, cheese & pico de gallo, rice & beans. Try them with our house dressing."),
  ("A17 Pollo con Crema", "12.99", "Grilled chicken breast with our sour cream sauce, steamed vegetables & rice."),
  ("A18 Pollo con Queso", "11.99", "Grilled chicken on a bed of rice topped with creamy queso blanco. Beef 12.99 · Beef & chicken 12.99 · Trio with shrimp 13.99"),
  ("A19 Grilled Tilapia", "12.99", "2 seasoned fillets with steamed vegetables & rice."),
  ("A20 Fajita Potato", "12.29", "Loaded baked potato with onions & bell peppers, with rice & small queso."),
  ("A21 Pork Carnitas", "13.99", "Seasoned pork with 3 flour tortillas, a small salad with avocado & fresh onions, rice & beans."),
  ("A22 Chicken & Shrimp Ranchero", "16.29", "With bell peppers, onions & tomatoes on a bed of rice with queso blanco & 3 flour tortillas."),
  ("A23 Street Tacos al Pastor", "13.99", "3 tacos with marinated meat, sautéed pineapple, onions & cilantro on corn tortillas, with rice & charro beans."),
  ("A24 Pollo Loco", "13.99", "Chicken breast topped with spinach, pico de gallo, mushrooms & melted cheese."),
  ("A25 Choripollo", "13.99", "Grilled chicken, chorizo, pico de gallo & spinach on a bed of rice, topped with melted cheese."),
  ("A26 Bistec", "15.99", "With rice, beans, grilled onions, chile toreado & 3 tortillas of your choice."),
  ("A27 Pollo a la Parrilla", "13.99", "Grilled chicken breast with our special seasoning, with pico de gallo, rice, grilled mushrooms & onions."),
 ]),
 ("fajitas", "Fajitas", None, [
  ("Single Fajitas", "15.99+", "Your choice of meat grilled with bell peppers, onions & a little tomato. Served with guacamole, sour cream, shredded cheese, pico de gallo, lettuce, charro beans & flour tortillas. Chicken 15.99 · Beef 16.99 · Chicken & beef 16.99 · Beef & shrimp 16.99 · Chicken or beef & shrimp 17.99 · Trio 17.99 · Shrimp 18.99"),
  ("Fajita Fiesta for Two", "27.99+", "Fajitas for two, with all the same sides, double tortillas & 2 sopapillas for dessert. Chicken 27.99 · Beef 28.99 · Chicken & beef 29.99 · Trio 29.99 · Beef or chicken & shrimp 29.99 · Shrimp 30.99"),
  ("Tacos al Carbon", "12.29", "Two flour tortillas with steak or grilled chicken & bacon, with sour cream, guacamole, pico de gallo, rice & frijoles charros."),
 ]),
 ("combos", "Combos", "Served with rice, beans, lettuce & tomato.", [
  ("C1", "12.29", "Three enchiladas — cheese, shredded chicken or ground beef."),
  ("C2", "12.29", "Ground beef taco, cheese enchilada & tamale."),
  ("C3", "13.29", "Chile relleno, cheese enchilada & ground beef taco."),
  ("C4", "12.29", "One tamale & two enchiladas — cheese, shredded chicken or ground beef."),
  ("C5", "12.29", "Three crispy ground beef tacos. Make them soft tacos +1.00"),
  ("C6", "13.29", "Chile relleno, ground beef taco & tamale."),
  ("C7", "12.29", "Two tacos & one burrito."),
  ("C8", "13.29", "Beef tostada, tamale & cheese enchilada."),
  ("C9", "12.29", "Two beef enchiladas & one taco."),
  ("C10", "13.29", "Ground beef taco & ground beef chimichanga."),
  ("C11", "13.29", "Guacamole tostada, tamale & ground beef enchilada."),
  ("C12", "11.99", "Two ground beef tacos & one tamale."),
 ]),
 ("quesadillas", "Quesadillas", "Served with lettuce, pico de gallo, sour cream & guacamole on the side, except the Spinach Quesadilla.", [
  ("Quesadilla", "10.29+", "Flour tortilla & cheese. Cheese only 10.29 · Ground beef 11.29 · Shredded chicken 11.29 · Grilled chicken 11.99 · Steak 12.99 · Chicken & beef 12.99 · Trio 13.79 · Shrimp 13.99 · Add mushrooms 1.29"),
  ("California Quesadilla", "14.29+", "Chipotle tortilla with mushrooms & chipotle sauce. Chicken 14.29 · Beef 15.29 · Trio 16.29"),
  ("Vegetarian Quesadilla", "11.99", "Mushrooms, onions & bell peppers."),
  ("Casa Quesadilla", "13.29", "Grilled chicken or steak in a garlic herb tortilla."),
  ("Mucho Quesadilla", "14.99", "Chicken, beef, mushrooms, onions & bell pepper in our famous garlic herb tortilla."),
  ("Spinach Quesadilla", "12.99", "Shredded cheese, spinach, mushrooms & pico de gallo, with rice, lettuce & sour cream on the side."),
 ]),
 ("nachos", "Nachos", "Individual chips topped with melted shredded cheese, in half or full size. Fiesta Nachos is the one exception: a pile of chips topped with queso dip, in one size.", [
  ("Muchos Nachos", "Half $11.29 · Full $13.29", "Grilled chicken or steak with beans, cheese, olives, mushrooms & tomatoes, served with guacamole, sour cream & jalapeños."),
  ("Fajita Nachos", "Half $10.29 · Full $12.29", "Grilled chicken or steak with beans & cheese, served with guacamole, sour cream & jalapeños."),
  ("Shrimp Nachos", "Half $11.29 · Full $14.29", "Shrimp with beans & cheese, served with guacamole, sour cream & jalapeños."),
  ("Beef or Chicken Nachos", "Half $9.99 · Full $11.29", "Ground beef or shredded chicken with beans & cheese, served with sour cream & jalapeños."),
  ("Texas Nachos", "Half $10.29 · Full $11.99", "Ground beef, beans, cheese & black olives, served with guacamole, sour cream & jalapeños."),
  ("Cheese Nachos", "Half $8.99 · Full $10.99", "Corn tortilla chips with cheese, sour cream & jalapeños."),
  ("Fiesta Nachos", "11.29", "A pile of chips topped with queso dip, beans, meat, lettuce, tomatoes, sour cream & jalapeños. One size. With grilled chicken or steak 12.29"),
 ]),
 ("burritos", "Burritos", "Big burrito plates come with lettuce, tomato, guacamole, black olives & sour cream on the side.", [
  ("Burrito de Todo", "12.99", "Big burrito with rice, beans, cheese, lettuce, tomato & your choice of steak, grilled chicken or a mix."),
  ("Taco Burrito", "11.99", "Big burrito with beans, lettuce, tomato, cheese & ground beef."),
  ("Chicken Burrito", "11.99", "Big burrito with beans, lettuce, tomato, cheese & shredded chicken."),
  ("Supremo Burrito", "9.99", "Big burrito with beans, lettuce, tomato & cheese."),
  ("Burrito Dinner #1", "11.29", "One burrito with ground beef or shredded chicken, with rice & beans on the side."),
  ("Burrito Dinner #2", "12.29", "One burrito with grilled chicken or steak, with rice & beans on the side."),
 ]),
 ("soups", "Soups & Salads", None, [
  ("Tortilla Soup Combo", "11.29", "Tortilla soup with rice, avocado, cilantro, a little cheese & crispy tortilla strips. Served with a mini grilled chicken quesadilla, rice & beans on the side."),
  ("Seafood Soup", "11.99", "A Louisiana favorite with crawfish tails & shrimp."),
  ("Shrimp Cocktail", "15.99", "Shrimp in Clamato & lime with avocado, cilantro & pico de gallo."),
  ("Border Salad", "12.29", "Chicken & shrimp with lettuce, tomatoes, cheese, chips, guacamole, sour cream & rice."),
  ("Compadre's Crispy Chicken Salad", "11.99", "Bed of lettuce topped with crispy chicken, tortilla chips, tomato, shredded cheese, olives, fresh mushrooms, onions & bell peppers."),
  ("Beef or Chicken & Shrimp Salad", "11.29", "Served in a taco bowl with lettuce, tomatoes, black olives, beans & sour cream."),
  ("Shrimp Salad", "12.29", "Served in a taco bowl with lettuce, tomatoes, black olives, beans & sour cream."),
  ("Taco Salad", "10.29", "Served in a taco bowl with lettuce, shredded cheese, beans, ground beef, tomatoes, black olives & sour cream."),
  ("Fajita Salad", "11.29", "Grilled chicken or steak served in a taco bowl with lettuce, shredded cheese, beans, tomatoes, black olives & sour cream."),
  ("Mexican Chili Pie", "10.49", "A full serving of beef & chili over tortilla chips, topped with lettuce, tomatoes, sour cream & cheese."),
  ("Guacamole Salad", "Sm $6.50 · Lg $8.50", ""),
  ("Regular Salad", "4.50", ""),
 ]),
 ("burgers", "Burgers & More", "Every burger comes with fries, plus lettuce, tomato, pickles, fresh onion and mayo & mustard packets on the side.", [
  ("Cheeseburger", "11.79", "Burger topped with cheese. Add bacon 12.99"),
  ("Jalapeño Cheeseburger", "11.99", "Burger topped with cheese & pickled jalapeños."),
  ("Loaded Burger", "13.29", "Burger topped with cheese, grilled mushrooms, grilled onions & bacon."),
  ("Jalapeño Chicken Wrap", "12.29", "Grilled chicken, shredded cheese, jalapeños & avocado wrapped in a tortilla, served with fries, lettuce & tomato."),
  ("Fajita Sandwich", "11.49", "Grilled chicken or steak topped with cheese."),
  ("Torta Sandwich", "12.29", "Pastor, carnitas, steak or grilled chicken."),
  ("Chicken Tenders", "11.29", "4 chicken tenders, served with fries & lettuce."),
  ("Ribeye Steak", "24.29", "Hand-cut 14 oz USDA Choice Angus. Choice of baked potato (plain or loaded) or fries, plus a salad & dinner roll."),
  ("Chicken Fried Steak", "13.29", "Tender breaded beef with gravy. Choice of baked potato (plain or loaded) or fries, plus a salad & dinner roll."),
 ]),
 ("kids", "Kids", "Kids meals come with rice & beans or fries, except the Pollo con Queso.", [
  ("Pollo con Queso", "6.95", "A plate of rice topped with grilled chicken & queso. No side."),
  ("Chicken Tenders", "5.95", "2 pieces."),
  ("Cheeseburger", "5.95", "Burger with cheese only."),
  ("Pizza Sticks", "5.95", "2 pieces."),
  ("Taco", "5.95", "Ground beef or shredded chicken with cheese. Make it a soft taco 0.50"),
  ("Burrito", "5.95", "Bean, ground beef or shredded chicken."),
  ("Enchilada", "5.95", "Cheese, shredded chicken or ground beef."),
  ("Quesadilla", "5.95", "Cheese, shredded chicken or ground beef."),
 ]),
 ("alacarte", "À la Carte", None, [
  ("Tostada", "4.59", "Bean, ground beef or shredded chicken: beans, lettuce, tomato & cheese. Guacamole: guacamole, lettuce, tomato & cheese, no beans."),
  ("Enchilada", "3.99", "Beef, chicken or cheese."),
  ("Taco", "2.79", "Ground beef or shredded chicken in a crispy corn shell, with lettuce, tomato & cheese."),
  ("Soft Taco", "3.29", "Ground beef or shredded chicken in a soft flour tortilla, with lettuce, tomato & cheese."),
  ("Mexican Taco", "3.79", "Soft corn tortilla topped with cilantro & onion. Steak, grilled chicken, chorizo, carnitas or al pastor."),
  ("Fajita Taco", "3.79", "Grilled chicken or steak in a soft flour tortilla, with lettuce, tomato & cheese."),
  ("Fish Taco", "3.79", "Grilled or deep-fried fish in a soft flour tortilla, topped with lettuce, tomato & cheese."),
  ("Shrimp Taco", "3.99", "Shrimp in a soft flour tortilla, topped with lettuce, pico de gallo & cheese."),
  ("Avocado Taco", "3.29", "Deep-fried avocado in a soft flour tortilla, topped with lettuce, tomato & cheese."),
  ("Tamale", "2.29", ""),
  ("Chile Relleno", "5.29", ""),
  ("Burrito", "5.79", ""),
  ("Chimichanga", "7.59", ""),
  ("Quesadilla", "7.99", ""),
  ("Soup", "4.29", ""),
  ("Plain Baked Potato", "5.29", ""),
  ("Steamed Veggies", "5.29", ""),
  ("Bag of Chips", "2.29", ""),
 ]),
 ("sides", "Sides", None, [
  ("Rice", "2.39", ""), ("Refried Beans", "2.39", ""), ("Charro Beans", "2.39", ""),
  ("Corn or Flour Tortillas", "1.99", ""), ("French Fries", "4.99", ""),
  ("Side of Grilled Chicken or Steak", "6.29", ""), ("Salsa", "Sm $4.29 · Lg $5.29", ""), ("Shredded Cheese", "2.79", ""),
  ("Pico de Gallo", "2.49", ""), ("Guacamole", "1.69+", "1 scoop 1.69 · Small (2 scoops) 3.29 · Large (4 scoops) 5.59"), ("Sour Cream", "1.29", ""), ("Jalapeños", "1.29", ""),
 ]),
 ("desserts", "Desserts", None, [
  ("Molten Lava Cake", "7.99", ""), ("Cake", "6.00", ""), ("Fried Cheesecake", "5.99", ""),
  ("Fried Ice Cream", "5.29", ""), ("Churros", "2.50", ""), ("Ice Cream (4 oz)", "1.99", ""), ("Sopapilla", "1.25", ""),
 ]),
]

# Lunch menu (lunch.html)
LUNCH = [
 ("lunchplates", "Lunch Plates", "Served with rice, beans, lettuce & tomato.", [
  ("L1", "8.99", "Two crispy beef tacos. Make them soft tacos +1.00"),
  ("L2", "9.99", "Chile relleno."),
  ("L3", "9.99", "Beef burrito."),
  ("L4", "9.99", "Chicken tostada & tamale."),
  ("L5", "9.99", "Beef tostada & tamale."),
  ("L6", "9.99", "Two enchiladas."),
  ("L7", "9.99", "Beef taco & cheese enchilada."),
  ("L8", "9.99", "Beef taco & beef enchilada."),
  ("L9", "9.99", "Taquitos topped with lettuce, sour cream & tomato."),
  ("L10", "9.99", "Two small burritos."),
  ("L11", "9.99", "Small beef chimichanga."),
  ("L12", "11.99", "Shrimp rancheros — grilled shrimp & veggies with melted cheese, with tortillas."),
  ("L13", "9.99", "Three tamales topped with chili."),
  ("L14", "9.99", "Small quesadilla with grilled chicken or steak."),
  ("L15", "9.99", "Chicken Monterrey — grilled chicken with melted cheese."),
  ("L16", "12.29", "Huevos con chorizo, with tortillas."),
 ]),
 ("lunchfajitas", "Lunch Fajitas", "Your choice of meat grilled with bell peppers, onions & a little tomato. Served with guacamole, sour cream, shredded cheese, pico de gallo, lettuce, charro beans & flour tortillas.", [
  ("Chicken", "11.29", ""),
  ("Beef", "11.99", ""),
  ("Chicken & Beef", "11.99", ""),
  ("Shrimp", "12.99", ""),
  ("Chicken or Beef & Shrimp", "12.99", ""),
  ("Trio", "12.99", "Chicken, beef & shrimp."),
 ]),
]

# Daily lunch specials: only served during lunch hours on their day.
DAILY = [
 ("Monday", "8.99", "Taco Salad", "Served in a taco bowl, with ground beef or shredded chicken."),
 ("Tuesday", "8.99", "Sour Cream Chicken Enchiladas", "With rice & beans."),
 ("Wednesday", "9.99", "Beef or Chicken Fajitas", "Grilled with bell peppers, onions & tomato, with all the regular fajita sides."),
 ("Thursday", "9.29", "Quesadilla", "With shredded chicken or ground beef, rice & beans."),
 ("Friday", "9.99", "Chimichanga", "With ground beef or shredded chicken, rice & beans."),
]

CATERING = [
 ("First Choice", "12.29", ["1 tamale", "1 flauta", "1 taco", "Rice & beans"]),
 ("Second Choice", "14.99", ["2 enchiladas — chicken, beef or cheese, choice of sauce", "1 flauta", "1 taco", "Rice & beans", "Queso dip"]),
 ("Third Choice", "14.99", ["2 tacos", "1 enchilada — chicken, beef or cheese, choice of sauce", "1 tamale", "Rice & beans", "Queso dip"]),
 ("Fourth Choice", "12.99", ["Chicken or beef quesadilla with lettuce, pico, sour cream & guacamole", "Flautas / taquitos", "Enchiladas — chicken, beef or cheese, choice of sauce", "Queso dip"]),
 ("Fifth Choice", "16.99", ["Steak & chicken fajitas with guacamole, sour cream, tomatoes, pico, cheese & lettuce", "Flour tortillas", "Tacos", "Refried beans & rice", "Queso dip"]),
 ("Sixth Choice", "15.99", ["Steak & chicken fajitas with guacamole, sour cream, tomatoes, pico, cheese & lettuce", "Flour tortillas", "Refried beans & rice", "Queso dip"]),
]

# Photo gallery (files are photo-<name>.webp next to index.html)
GALLERY_FOOD = [
 ("sampler-platter", "Sampler Platter"), ("fiesta-nachos", "Fiesta Nachos"), ("quesadilla", "Quesadilla"),
 ("tortilla-soup", "Tortilla Soup"), ("nachos", "Nachos"), ("cheeseburger", "Cheeseburger"),
]
GALLERY_PLACE = [
 ("welcome-sign", "¡Bienvenidos!"), ("beer", "Ice-cold beer", "tall"), ("dining-room", "Our dining room"),
 ("margaritas", "Margaritas", "tall"), ("mural-room", "The mural room"), ("patio", "Our patio"),
]

e = html.escape

def fmt_price(p):
    if not p: return ""
    if "$" in p: return p
    plus = p.endswith("+")
    return ("from " if plus else "") + "$" + p.rstrip("+")

def menu_html(menu=MENU):
    chips, secs = [], []
    for sid, title, note, items in menu:
        chips.append(f'<a class="chip" href="#m-{sid}">{e(title)}</a>')
        rows = []
        for name, price, desc in items:
            rows.append(
                f'<li class="item"><div class="item-top"><span class="item-name">{e(name)}</span>'
                + ('' if "·" in price else '<span class="dots" aria-hidden="true"></span>')
                + f'<span class="item-price{" multi" if "·" in price else ""}">{e(fmt_price(price))}</span></div>'
                + (f'<p class="item-desc">{e(desc)}</p>' if desc else "") + '</li>')
        secs.append(
            f'<section class="menu-sec" id="m-{sid}"><h3>{e(title)}</h3>'
            + (f'<p class="sec-note">{e(note)}</p>' if note else "")
            + f'<ul class="items">{"".join(rows)}</ul></section>')
    return "".join(chips), "".join(secs)

def catering_html():
    out = []
    for title, price, lines in CATERING:
        lis = "".join(f"<li>{e(l)}</li>" for l in lines)
        out.append(f'<article class="cater-card"><h3>{e(title)}</h3>'
                   f'<p class="cater-price">${price} <span>per person</span></p><ul>{lis}</ul></article>')
    return "".join(out)

def gallery_html(items, captions=True):
    out = []
    for f, c, *extra in items:
        cls = " tall" if "tall" in extra else ""
        out.append(f'<figure class="ph{cls}"><img src="photo-{f}.webp" alt="{e(c)}" loading="lazy" decoding="async">'
                   + (f'<figcaption>{e(c)}</figcaption>' if captions else '') + '</figure>')
    return "".join(out)

chips, sections = menu_html()
logo_b64 = base64.b64encode(open("logo.png", "rb").read()).decode()
tpl = open("template.html", encoding="utf-8").read()
maps_embed = "https://www.google.com/maps?q=" + html.escape(MAPS_Q.replace(" ", "+").replace("'", "%27")) + "&output=embed"
maps_dir = "https://www.google.com/maps/dir/?api=1&destination=" + MAPS_Q.replace(" ", "+").replace("'", "%27").replace(",", "%2C")
def render(home, title):
    return (tpl.replace("{{HOME}}", home).replace("{{TITLE}}", title).replace("{{LOGO}}", "data:image/png;base64," + logo_b64)
          .replace("{{CHIPS}}", chips).replace("{{MENU}}", sections)
          .replace("{{CATERING}}", catering_html())
          .replace("{{GALLERY_FOOD}}", gallery_html(GALLERY_FOOD)).replace("{{GALLERY_PLACE}}", gallery_html(GALLERY_PLACE, captions=False))
          .replace("{{PHONE}}", PHONE_DISPLAY).replace("{{TEL}}", PHONE_TEL)
          .replace("{{ADDR1}}", ADDRESS_1).replace("{{ADDR2}}", ADDRESS_2)
          .replace("{{TOAST}}", TOAST).replace("{{FACEBOOK}}", FACEBOOK)
          .replace("{{MAPEMBED}}", maps_embed).replace("{{DIRECTIONS}}", html.escape(maps_dir)))

out = render("", "Jose's Compadre Mexican Grill · North Little Rock, AR")
open("index.html", "w", encoding="utf-8").write(out)
print("built index.html", len(out))

# ---- lunch.html: same header, footer and styles; different main content ----
def daily_html():
    cards = []
    for day, price, name, desc in DAILY:
        cards.append(f'<article class="day-card" data-day="{day}"><span class="today-tag">Today</span>'
                     f'<p class="day-label">{e(day)}</p><h3>{e(name)}</h3>'
                     + (f'<p class="day-desc">{e(desc)}</p>' if desc else "")
                     + f'<p class="day-price">${price}</p></article>')
    return "".join(cards)

_, lunch_secs = menu_html(LUNCH)
lunch_main = f"""<main id="top">
<section class="page-head">
  <div class="wrap">
    <a class="back" href="./#menu">&larr; Full menu</a>
    <span class="eyebrow">11 am – 3 pm</span>
    <h2>Lunch Menu</h2>
    <div class="notice">
      <p><strong>Lunch hours are 11 am – 3 pm.</strong></p>
      <p>Lunch plates and lunch fajitas are available all day. <strong>After 3 pm, add $1.45.</strong></p>
      <p>Daily specials are served only during lunch hours on their day.</p>
    </div>
  </div>
</section>
<div class="serape" aria-hidden="true"></div>
<section class="menu" id="specials">
  <div class="wrap">
    <span class="eyebrow">Monday – Friday</span>
    <h2>Daily Lunch Specials</h2>
    <div class="day-grid">{daily_html()}</div>
  </div>
</section>
<section class="menu lunch-menu" id="menu">
  <div class="wrap">
    <div class="menu-cols">{lunch_secs}</div>
    <div class="order-band"><a class="btn btn-primary" href="{TOAST}" target="_blank" rel="noopener">Order Online for Pickup</a>
      <a class="btn btn-light" href="./#menu">See the Full Menu</a></div>
    <p class="advisory">Prices subject to change.</p>
  </div>
</section>
</main>"""
base = render("./", "Lunch Menu · Jose's Compadre Mexican Grill")
i, j = base.index('<main id="top">'), base.index('</main>') + len('</main>')
lunch_page = base[:i] + lunch_main + base[j:]
open("lunch.html", "w", encoding="utf-8").write(lunch_page)
print("built lunch.html", len(lunch_page))

import streamlit as st
import urllib.parse

WHATSAPP_NUMBER = "+923153324597"

st.set_page_config(
    page_title="TechCart",
    page_icon="📱",
    layout="wide",
)

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #f5f7ff 0%, #eef7ff 100%);
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        div[data-testid="stRadio"] > div {
            background: rgba(255,255,255,0.8);
            border-radius: 12px;
            padding: 0.35rem 0.5rem;
            border: 1px solid #dfeafc;
        }
        div[data-testid="stVerticalBlock"] > div {
            border-radius: 16px;
        }
        [data-testid="stImage"] img {
            border-radius: 14px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        }
        .stButton > button, .stLinkButton > a {
            border-radius: 10px;
            border: none;
            font-weight: 600;
            background: linear-gradient(90deg, #2563eb, #3b82f6);
            color: white;
            padding: 0.6rem 1rem;
        }
        .stButton > button:hover, .stLinkButton > a:hover {
            background: linear-gradient(90deg, #1d4ed8, #2563eb);
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def whatsapp_link(product_name: str, price: str) -> str:
    message = (
        "Hello! I am interested in ordering:\n"
        f"Product: {product_name}\n"
        f"Price: {price}\n"
        "Please provide more details."
    )
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(message)}"


st.title("💻 TechCart")
st.caption("Smart Products. Simple shopping.")

menu = st.radio(
    "Menu",
    ["Home", "Products", "Categories", "About", "Contact"],
    horizontal=True,
)

st.divider()

if menu == "Home":
    st.markdown("### Welcome to TechCart")
    st.subheader("Smart Products. Simple Shopping.")
    st.write(
        "Discover useful and affordable technology products "
        "for your everyday needs."
    )

    st.markdown("---")
    st.header("Why Shop With Us?")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### ✅ Quality Products")
        st.write("We offer reliable and useful products.")

    with col2:
        st.markdown("### 💰 Affordable Prices")
        st.write("Get great products at reasonable prices.")

    with col3:
        st.markdown("### 🚚 Easy Ordering")
        st.write("Order your favorite products easily.")

    st.markdown("---")
    st.header("Featured Picks")
    featured = st.columns(3)
    products = [
        ("Premium Earbuds", "earbuds.png", "Rs. 1500", "Comfortable wireless earbuds"),
        ("HP Laptop", "laptop.png", "Rs. 15000", "8th generation laptop"),
        ("HP Mouse", "mouse.png", "Rs. 2000", "Wireless laptop mouse"),
    ]

    for col, (name, image, price, desc) in zip(featured, products):
        with col:
            st.image(image, use_container_width=True)
            st.subheader(name)
            st.write(desc)
            st.write(f"Price: {price}")
            st.link_button("🛍️ Shop Now", whatsapp_link(name, price))

elif menu == "Products":
    st.header("Our Products")
    st.write("Explore our collection of smart products.")
    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("earbuds.png", use_container_width=True)
        st.subheader("Premium Earbuds")
        st.write("Comfortable wireless earbuds")
        st.markdown("**Price: Rs. 1500**")
        st.link_button("🛍️ Shop Now", whatsapp_link("Premium Earbuds", "Rs. 1500"))

    with col2:
        st.image("laptop.png", use_container_width=True)
        st.subheader("HP Laptop")
        st.write("8th generation laptop")
        st.markdown("**Price: Rs. 15000**")
        st.link_button("🛍️ Shop Now", whatsapp_link("HP Laptop", "Rs. 15000"))

    with col3:
        st.image("mouse.png", use_container_width=True)
        st.subheader("HP Mouse")
        st.write("Wireless laptop mouse")
        st.markdown("**Price: Rs. 2000**")
        st.link_button("🛍️ Shop Now", whatsapp_link("HP Mouse", "Rs. 2000"))

elif menu == "Categories":
    st.header("Product Categories")
    st.write("Browse our collection by category.")

    cat1, cat2, cat3 = st.columns(3)

    with cat1:
        st.markdown("### 🎧 Audio")
        st.write("Wireless earbuds and sound accessories")

    with cat2:
        st.markdown("### 💻 Computing")
        st.write("Laptops, accessories, and productivity devices")

    with cat3:
        st.markdown("### 🖱️ Accessories")
        st.write("Mice, keyboards, and useful add-ons")

    st.divider()
    st.info("Need help choosing a product? Message us on WhatsApp and we will guide you.")

elif menu == "About":
    st.header("About TechCart")
    st.write(
        "TechCart is a modern electronics store focused on smart, useful, "
        "and affordable products for everyday life."
    )

    st.subheader("Our Mission")
    st.write(
        "To make technology simple, accessible, and valuable for customers who want "
        "reliable products without the hassle."
    )

    st.subheader("Why Customers Choose Us")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("✅ Trusted quality")
    with col2:
        st.markdown("✅ Affordable pricing")
    with col3:
        st.markdown("✅ Fast support")

elif menu == "Contact":
    st.header("Contact Us")
    st.write("We are here to help you with product details, pricing, and orders.")

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("WhatsApp")
        st.write(f"Call or message: {WHATSAPP_NUMBER}")
        st.link_button("Chat on WhatsApp", f"https://wa.me/{WHATSAPP_NUMBER}")

    with c2:
        st.subheader("Store Hours")
        st.write("Monday - Saturday")
        st.write("9:00 AM - 8:00 PM")

    st.divider()
    st.markdown(
        "Looking for a custom recommendation? Send us a message with the product name and your budget, and we will help you choose the best option."
    )

import streamlit as st


st.title("hi")
from streamlit_extras.buy_me_a_coffee import button

button(username="fake-username", floating=False, width=221)

@extra
def button(
    username: str,
    floating: bool = True,
    text: str = "Buy me a coffee",
    emoji: str = "",
    bg_color: str = "#FFDD00",
    font: Font = "Cookie",
    font_color: str = "#000000",
    coffee_color: str = "#000000",
    width: int = 220,
):
    button = f"""
        <script type="text/javascript"
            src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js"
            data-name="bmc-button"
            data-slug="{username}"
            data-color="{bg_color}"
            data-emoji="{emoji}"
            data-font="{font}"
            data-text="{text}"
            data-outline-color="#000000"
            data-font-color="{font_color}"
            data-coffee-color="{coffee_color}" >
        </script>
    """

    html(button, height=70, width=width)

    if floating:
        st.markdown(
            f"""
            <style>
                iframe[width="{width}"] {{
                    position: fixed;
                    bottom: 60px;
                    right: 40px;
                }}
            </style>
            """,
            unsafe_allow_html=True,
        )

import streamlit as st
import llm_tutorial
import streamlit.components.v1 as components

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Controls Generator")

with st.sidebar:
    risk = st.text_input("Mention risk name...", value="")
    num_controls = st.number_input(
        "Number of Control Results...", min_value=3, max_value=10
    )
    clicked = st.button("Submit")

if clicked:
    response = llm_tutorial.generate_controls(risk, num_controls)

    st.header(risk)
    controls = response["controls"]
    # st.write(controls)
    # components.html(controls)
    st.markdown(controls, unsafe_allow_html=True)
    print(controls)
    # st.write("Controls to be followed:")
    # for item in controls:
    #     st.write(item)

import streamlit as st
import matplotlib.pyplot as plt

# 1. Configuración de la página
st.set_page_config(page_title="TITU IA", page_icon="🎓")

# 2. Título principal
st.title("🎓 TITU: Tu Profesor de Ingeniería")
st.markdown("---")

# 3. Menú lateral
opcion = st.sidebar.selectbox("¿Qué quieres hacer?", ["Inicio", "Calculadora Eléctrica", "Subir Planos"])

if opcion == "Inicio":
    st.write("### ¡Bienvenido! Soy TITU.")
    st.write("Estoy aquí para ayudarte con tus proyectos de electricidad. ¡Aprendamos juntos!")

elif opcion == "Calculadora Eléctrica":
    st.subheader("⚡ Calculadora de Ley de Ohm")
    v = st.number_input("Voltaje (V):", min_value=0.0, value=12.0)
    r = st.number_input("Resistencia (Ω):", min_value=0.1, value=2.0)
    if st.button("Calcular"):
        st.success(f"La corriente es: {v/r} Amperios")

elif opcion == "Subir Planos":
    st.subheader("📐 Analizador de Planos")
    archivo = st.file_uploader("Sube tu imagen aquí:", type=['png', 'jpg', 'jpeg'])
    if archivo:
        st.image(archivo, caption="Plano cargado correctamente")

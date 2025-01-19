import streamlit as st

st.title("Gestión de Inventario y Ventas")

with st.sidebar:
    st.header("Nueva Venta")
    fecha = st.date_input("Fecha")
    producto = st.text_input("Producto")
    cantidad = st.number_input("Cantidad", min_value=1, step=1)
    precio = st.number_input("Precio", min_value=0.0, step=0.01)
    metodo_pago = st.selectbox("Método de pago", ["bizum", "efectivo", "tarjeta"])


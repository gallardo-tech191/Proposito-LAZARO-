import streamlit as st
import time

VIDA_UTIL_MAXIMO = 10.0
IMPACTO_DE_CO2 = 12.5
COSTO_REEMPLAZO = 150.0


def calcular_vida_restante(years, horas):
    porcentaje_tiempo = (years / VIDA_UTIL_MAXIMO) * 100
    desgaste = (horas / 10000.0) * 10.0
    restante = 100.0 - (porcentaje_tiempo + desgaste)
    return max(0.0, round(restante, 1))


def evaluar_destino(porcentaje_vida):
    if porcentaje_vida >= 50.0:
        return "Apto para Postas de Salud Rurales (Donación)"
    elif porcentaje_vida >= 20.0:
        return "Requiere Reacondicionamiento / Repuestos Biomédicos"
    else:
        return "Reciclaje Técnico de Componentes / Extraccion de Componentes Utiles "
    
def calcular_impacto(peso):
    co2 = peso * IMPACTO_DE_CO2
    ahorro = peso * COSTO_REEMPLAZO
    return round(co2, 2), round(ahorro, 2)

#ELABORACION DE LA PAGINA WEB
def main():
    st.set_page_config(
        page_title="EcoGen - Plataforma de Economía Circular en Equipos Médicos",
        layout="centered",
    )

    st.title(" EcoGen: Economía Circular en Equipos Médicos")
    st.markdown(
        "*Plataforma para extender la vida útil del equipamiento"
        " hospitalario.*"
    )
    st.markdown("---")

    st.subheader("Registro de Equipo")

    equipo = st.selectbox(
        "Selecciona el equipo:",
        [
            "Pulsioxímetro de Pulso",
            "Monitor de Signos Vitales",
            "Electrocardiógrafo (ECG)",
            "Bomba de Infusión",
            "Concentrador de Oxígeno",
        ],
    )

    c1, c2 = st.columns(2)
    with c1:
        years = st.number_input(
            "Años de Operación:", min_value=0.0, max_value=20.0, value=3.0, step=0.5
        )
        peso = st.number_input(
            "Peso (kg):", min_value=0.5, max_value=100.0, value=5.0
        )

    with c2:
        horas = st.number_input(
            "Horas de Uso:", min_value=0, max_value=50000, value=2000, step=500
        )
        destino = st.selectbox(
            "Centro Beneficiario:",
            ["Centro de Salud Rural", "Posta Comunitario", "Hospital Regional C"],
        )

    if st.button("Evaluar Equipo y Triple Impacto"):
        vida_restante = calcular_vida_restante(years, horas)
        dictamen = evaluar_destino(vida_restante)
        co2, ahorro = calcular_impacto(peso)

        time.sleep(5)  # Simula un procesamiento de datos

        st.write("Calculando impacto ambiental y económico...")

        time.sleep(2)  # Simula un procesamiento adicional

        st.write("Generando la opcion mas adecuada para el medio ambiente....")

        time.sleep(2)
        st.success("¡Diagnóstico generado con éxito!")

        st.markdown("### Indicadores")
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.metric(" CO2 Evitado", f"{co2} kg")
        with col_m2:
            st.metric("Social", "1 Centro")
        with col_m3:
            st.metric(" Ahorro", f"${ahorro:.2f} USD")

        st.markdown("---")
        st.subheader(" Dictamen Técnico")
        st.write(f"**Vida Útil Restante:** {vida_restante}%")
        st.info(
            f"**Destino Recomendado:** {dictamen} para asignarse a **{destino}**."
        )


if __name__ == "__main__":
    main()
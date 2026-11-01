from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Anúncios de Carros", layout="wide")

BASE_DIR = Path(__file__).parent


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv(BASE_DIR / "vehicles_us.csv")
    df["date_posted"] = pd.to_datetime(df["date_posted"])
    df["manufacturer"] = df["model"].str.split().str[0]
    return df


car_data = load_data()

st.header("Dashboard de anúncios de venda de carros")
st.write(
    f"O conjunto de dados contém **{len(car_data):,}** anúncios. "
    "Use os controles abaixo para explorar os dados."
)

with st.expander("Ver amostra dos dados"):
    st.dataframe(car_data.head(50))

# --- Histograma -----------------------------------------------------------
st.subheader("Histogramas")
numeric_cols = ["price", "odometer", "model_year", "days_listed"]
hist_col = st.selectbox("Coluna para o histograma", numeric_cols)
color_by_condition = st.checkbox("Separar por condição do veículo", value=True)

fig_hist = px.histogram(
    car_data,
    x=hist_col,
    color="condition" if color_by_condition else None,
    title=f"Distribuição de {hist_col}",
)
st.plotly_chart(fig_hist, width="stretch")

# --- Gráfico de dispersão ---------------------------------------------------
st.subheader("Gráfico de dispersão")
x_axis = st.selectbox("Eixo X", ["odometer", "model_year", "days_listed"], index=0)
fig_scatter = px.scatter(
    car_data,
    x=x_axis,
    y="price",
    color="condition",
    opacity=0.6,
    title=f"Preço vs. {x_axis}",
)
st.plotly_chart(fig_scatter, width="stretch")

# --- Comparação de preço entre marcas ---------------------------------------
st.subheader("Comparação de distribuição de preço entre marcas")
manufacturers = sorted(car_data["manufacturer"].dropna().unique())
col1, col2 = st.columns(2)
brand_1 = col1.selectbox("Marca 1", manufacturers, index=0)
brand_2 = col2.selectbox(
    "Marca 2", manufacturers, index=min(1, len(manufacturers) - 1)
)
normalize = st.checkbox("Normalizar histograma (porcentagem)", value=True)

subset = car_data[car_data["manufacturer"].isin([brand_1, brand_2])]
fig_cmp = px.histogram(
    subset,
    x="price",
    color="manufacturer",
    barmode="overlay",
    histnorm="percent" if normalize else None,
    opacity=0.7,
    title=f"Preço: {brand_1} vs. {brand_2}",
)
st.plotly_chart(fig_cmp, width="stretch")

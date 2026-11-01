# Dashboard de anúncios de venda de carros

Aplicativo web feito com **Streamlit** e **Plotly Express** para explorar um
conjunto de dados de anúncios de carros usados (`vehicles_us.csv`).

## Funcionalidades

- Histogramas interativos (preço, odometer, ano do modelo, dias anunciado)
- Gráfico de dispersão de preço vs. outras variáveis
- Comparação da distribuição de preço entre duas marcas

## Como rodar localmente

```bash
python -m venv vehicles_env
source vehicles_env/bin/activate      # Windows: vehicles_env\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Estrutura

```
├── app.py               # aplicativo Streamlit
├── vehicles_us.csv      # conjunto de dados
├── notebooks/EDA.ipynb  # análise exploratória
├── requirements.txt
└── README.md
```

## Deploy no Render

1. Crie um **Web Service** no [render.com](https://render.com) apontando para este repositório.
2. **Build Command:** `pip install -r requirements.txt`
3. **Start Command:** `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
4. Escolha o plano gratuito e aguarde o deploy.

**Link do app:** _(cole aqui a URL do Render)_

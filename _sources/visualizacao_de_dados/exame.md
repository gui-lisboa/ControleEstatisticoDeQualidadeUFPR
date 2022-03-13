# Exame

```{admonition} Exercício
:class: tip

Dados sobre habitação e mercado imobiliário são de extrema relevância em diversos tipos de pesquisa. Considere um conjunto de dados sobre 506 setores censitários da cidade de Boston/EUA, no censo de 1970. Acesse-o em R via require(mlbench); data(BostonHousing); BostonHousing.

```

Repositório para os dashboards: <https://github.com/gui-lisboa/BostonHousing_Shiny_vs_Dash>

Link para os dashboards:

- Shiny: <https://guilisboa.shinyapps.io/BostonHousing>
- Dash: <https://bostonhousing-vizdados.herokuapp.com>

## Construa um dashboard para esta base de dados utilizando r-shiny

```{figure} ./imagens/exame-shiny.PNG
:align: center

Dashboard em Shiny
```

``` r
library(shiny)
library(ggplot2)
library(plyr)
library(rjson)
library(tidyr)

require(mlbench)
data(BostonHousing)
bostonHousingMetaData <- fromJSON(file = "./boston-housing-meta.json")

ui <- fluidPage(
  
  titlePanel("Boston Housing - Painel criado com Shiny"),
  
  sidebarLayout(
    
    sidebarPanel(
      h3("Variáveis"),
      selectInput(inputId = "variavel",
                  label = "Opções",
                  choices = names(BostonHousing),
                  multiple = FALSE),
      plotOutput(outputId = "graficoResumo"),
      h4("Estrutura"),
      verbatimTextOutput(outputId = "estrutura"),
      h4("Sobre"),
      textOutput("sobre"),
      width = 3
    ),
    
    mainPanel(
      h3("Relação com MEDV"),
      plotOutput(outputId = "graficoRegressao"),
      h3("Mapa de Densidade"),
      selectInput(inputId = "variavelMapa",
                  label = "Opções",
                  choices = names(BostonHousing),
                  multiple = FALSE),
      plotOutput(outputId = "mapaDensidade"),
    )

  )
  
)

server <- function(input, output){
  
  output$graficoResumo <- renderPlot({
    if(is.factor(BostonHousing[[input$variavel]])) {
      coluna <- BostonHousing[[input$variavel]]
      data <- data.frame(
        categoria = levels(coluna),
        freq = count(coluna)[2]
      )
      ggplot(data, aes(y=freq, x="", fill=categoria)) +
      geom_bar(stat = "identity", width = 1) +
      coord_polar("y", start=0) +
      labs(title = paste("Contagem de ", input$variavel)) +
      theme_void()
    }
    else {
      ggplot(BostonHousing, aes_string(y=input$variavel)) +
      geom_boxplot() +
      labs(title = paste("Boxplot de ", input$variavel))
    }
  })
  
  output$estrutura <- renderPrint({
    str(BostonHousing[[input$variavel]])
  })
  
  output$sobre <- renderPrint({
    bostonHousingMetaData[[input$variavel]]
  })
  
  output$graficoRegressao <- renderPlot({
    ggplot(BostonHousing, aes_string(y="medv", x=input$variavel)) +
    geom_point() +
    geom_smooth(method=lm)
  })
  
  output$mapaDensidade <- renderPlot({
    ggplot(BostonHousing, aes_string(y=input$variavelMapa, x=input$variavel)) +
    stat_density2d(aes(fill = ..density..), geom = 'tile', contour = F)
  })
  
}

shinyApp(ui = ui, server = server)

```

## Construa um dashboard semelhante ao do item a. utilizando outra ferramenta de sua preferência (PowerBI, Kibana, Google Data Studio, Tableau etc.)

```{figure} ./imagens/exame-dash.PNG
:align: center

Dashboard usando Dash
```

``` python
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import json

BARRA_LATERAL_SHINY = {
    "min-height": "20px",
    "padding": "19px",
    "margin-bottom": "20px",
    "background-color": "#f5f5f5",
    "border": "1px solid #e3e3e3",
    "border-radius": "4px",
    "-webkit-box-shadow": "inset 0 1px 1px rgb(0 0 0 / 5%)",
    "box-shadow": "inset 0 1px 1px rgb(0 0 0 / 5%)",
}

with open("./boston-housing-meta.json", "r") as json_file:
    boston_housing_metadata = json.load(json_file)

data_url = "https://raw.githubusercontent.com/scikit-learn/scikit-learn/0d378913be6d7e485b792ea36e9268be31ed52d0/sklearn/datasets/data/boston_house_prices.csv"
boston_housing = pd.read_csv(data_url, skiprows=2)
boston_housing.columns = boston_housing_metadata.keys()

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

barra_lateral = html.Div(
    [
        html.H3("Variáveis"),
        dcc.Dropdown(
            id="variavel",
            options=[
                {"label": column, "value": column} for column in boston_housing.columns
            ],
        ),
        dcc.Graph(id="graficoResumo"),
        html.H4("Estrutura"),
        html.P(id="estrutura"),
        html.H4("Sobre"),
        html.P(id="sobre"),
    ],
    className="col-sm-3",
    style=BARRA_LATERAL_SHINY,
)

principal = html.Div(
    [
        html.H3("Relação com MEDV"),
        dcc.Graph(id="graficoRegressao"),
        html.Div(
            [
                html.H3("Mapa de Densidade"),
                dcc.Dropdown(
                    id="variavelMapa",
                    options=[
                        {"label": column, "value": column}
                        for column in boston_housing.columns
                    ],
                ),
            ],
            className="row"
        ),
        dcc.Graph(id="mapaDensidade")
    ],
    className="col-sm-8",
)

titulo = html.H1("Boston Housing - Painel criado com Dash", className="row")
painel = html.Div([barra_lateral, principal], className="row")
app.layout = html.Div([titulo, painel], style={"padding-left": "10px", "height": "100vh"})
server = app.server

@app.callback(
    Output("graficoResumo", "figure"),
    Output("estrutura", "children"),
    Output("sobre", "children"),
    Output("graficoRegressao", "figure"),
    Input("variavel", "value"),
)
def atualizar(variavel):
    if variavel is None:
        raise PreventUpdate
    if(variavel == "chas"):
        contagem = boston_housing[variavel].value_counts()
        graficoResumo = px.pie(names=contagem.index, values=contagem.values)
    else:
        graficoResumo = px.box(boston_housing, y=variavel)
    estrutura = str(boston_housing[variavel].dtype)
    sobre = boston_housing_metadata[variavel]
    graficoRegressao = px.scatter(boston_housing, x=variavel, y="medv", trendline="ols")
    return graficoResumo, estrutura, sobre, graficoRegressao

@app.callback(
    Output("mapaDensidade", "figure"),
    Input("variavelMapa", "value"),
    Input("variavel", "value"),
)
def atualizar(variavelMapa, variavel):
    if variavel is None or variavelMapa is None:
        raise PreventUpdate
    mapaDensidade = px.density_heatmap(boston_housing, x=variavel, y=variavelMapa)
    return mapaDensidade

if __name__ == "__main__":
    app.run_server(debug=True)

```

## Compare os dois e interprete-os

### Comparação

A barra lateral com a caixa para seleção da variável ficou muito semelhante entre as duas bibliotecas. Foi tomado como referência o padrão do Shiny, por isso foi necessário adicionar um CSS a fim de espelhar o estilo. A disposição dos elementos na DOM é mais direta usando componentes do Shiny, para replicar a aparência com Dash é preciso ter uma base melhor de CSS ou utilizar bibliotecas de componentes (como Dash Bootrap Components usado no exemplo). Caso o desenvolvedor opte por não seguir o padrão do Shiny, me pareceu mais trabalhoso adicionar customizações.

Já a criação dos gráficos principais, o Shiny baseado em R e na biblioteca ggplot2 foi mais eficiente para criar a reta do modelo de regressão linear entre a variável escolhida e MEDV, uma vez que é muito simples adicionar o intervalo da reta. Entretanto o mapa de calor foi muito mais direto com o Dash, o algoritmo que divide as regiões é menos granular que o padrão do stat_density2d do ggplot, mas o efeito pareceu mais agradável para os valores do Boston Housing.

A interatividade é mais direta e escalável no Dash. Poder decorar funções com Outputs e Inputs é mais interessante caso haja muitos elementos e fique enviável manter todo código em um único arquivo.

### Interpretação

Dois principais fatores parecem influênciar o preço dos imóveis (MEDV). De forma positiva, a quantidade de quartos (RM).

```{figure} ./imagens/exame-dash-rm-vs-medv.PNG
:align: center

Relação entre RM e MEDV
```

Já a poluição (NOX) exerce uma pressão negativa no preço dos imóveis.

```{figure} ./imagens/exame-dash-nox-vs-medv.PNG
:align: center

Relação entre NOX e MEDV
```

Também é possível notar que os imóveis mais antigos estão expostos a mais poluição.

```{figure} ./imagens/exame-dash-nox-age.PNG
:align: center

Relação entre RM e MEDV
```

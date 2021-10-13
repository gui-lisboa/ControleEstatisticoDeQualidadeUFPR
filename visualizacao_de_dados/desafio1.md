# Desafio 1

```{admonition} Desafio
:class: tip

Criar um relatório em rmarkdown que contenha pelo menos 10 gráficos errados ou não efetivos.
```

## 1. Escala linear representada por área

```{figure} http://eagereyes.org/media/2008/FastFood.jpg
:align: center

Receita de redes de restaurantes (US$ Bilhões)
```

O gráfico acima tem como escala receitas de redes de restaurantes, em bilhões de dólares, e usa a altura das logomarcas para alinhar o valor da receita com o eixo vertical. Porém, a fim de não distorcer as logomarcas, o autor mantém as larguras proporcionais, fazendo com que a impressão fique distorcida. Por exemplo, a receita da Starbucks for de US\$ 4,1 bilhões, cerca de 1/3 da receita de US\$ 11,3 bilhões do Burguer King, entretanto o tamanho da logomarca ocupa menos de 1/4 da área que representa a rede concorrente.

> Fonte: [Linear vs. Quadratic Change, Robert Kosara](https://eagereyes.org/blog/2008/linear-vs-quadratic-change)

---

## 2. Infográficos carregados para informações simples

```{figure} https://ychef.files.bbci.co.uk/1600x900/p054jykn.png
:align: center

Quantidade de torradas com avocado para dar entrada em uma casa de 90$m^2$ fora do centro das cidades
```

O infográfico é um entre 5 similares que quantificam a quantidade que pode ser economizada por não comprar torradas com avocado. Entretanto, a quantidade de torradas ocupa a mesma área em todos os gráficos, a escala de cada torrada que diminui. Além disso, para entender essa relação nas 10 cidades, é preciso ver todos os 5 gráficos.

> Fonte: [Avocado Toast Index, BBC](https://www.bbc.com/worklife/article/20170530-the-avocado-toast-index-how-many-breakfasts-to-buy-a-house)

---

## 3. Mapa de cores

```{figure} https://eagereyes.org/wp-content/uploads/2013/07/evapotranspiration-map-600x483.jpg
:align: center

Fração de precipitação perdida por evapotranspiração entre 1971-2000
```

O gráfico dá a entender que há uma grande mudança na região central dos Estados Unidos, saltando de uma faixa verde para amarela. Observando a legenda, nota-se que a escala segue do verde escuro (0,7 - 0,79) para o amarelo escuro (0,8 - 0,89). Assim o impacto na mudança da cor superestima a diferença real.

> Fonte: [How The Rainbow Color Map Misleads, Robert Kosara](https://eagereyes.org/basics/rainbow-color-map)

## 4. Única barra

<iframe src="https://www.portaltransparencia.gov.br/graficos/embed/funcao-especifica/visao-geral/barras-horizontais-empilhada?ano=2021&codigoFuncao=12&titulo=Vis%C3%A3o%20geral%20da%20distribui%C3%A7%C3%A3o%20por%20sub%C3%A1rea%20(subfun%C3%A7%C3%A3o)" width="100%" height="400px" frameborder="0" style="border:0" allowfullscreen></iframe>

O gráfico acima não deixa claro quais os valores pagos nas subfunções não associadas à função educação. Só é possível saber os valores calculando a diferença ou usando o ponteiro sobre a área verde. Um gráfico com duas barras separadas para cada categoria traria a mesma informação de maneira mais direta.

> Fonte [Portal da Transparência](https://www.portaltransparencia.gov.br/graficos/funcao-especifica/visao-geral/barras-horizontais-empilhada?ano=2021&codigoFuncao=12&titulo=Vis%C3%A3o%20geral%20da%20distribui%C3%A7%C3%A3o%20por%20sub%C3%A1rea%20(subfun%C3%A7%C3%A3o))

## 5. 
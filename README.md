# Gupy-Web-Scraping-Driva

#### Desafio de Web Scraping proposto pela empresa Driva para seus candidatos ao estágio em Dados
---

#### Análise: https://docs.google.com/document/d/1Q2Hv6fwsCMD5IxKETXQfx06xqpmXcYtN89ShI6NRYoY/edit?usp=sharing


#### Neste desafio foram usadas as bibliotecas BeautifulSoup, Requests e CSV. O Requests foi utilizado para fazer a requisição da página a qual seria feito o Web Scraping, o CSV foi utilizado para criar o arquivo .csv com os headers respectivos e para escrever no arquivo e o BeautifulSoup foi utilizado para obter as informações da página da Web passado pelo Requests.
---

```python
dictVaga = {"Nome": "", "Empresa": "", "Local": "", "Modelo": "", "Tipo": "", "Vaga para PcD": ""}
vagas = soup.find_all('a', class_="sc-a3bd7ea-1 kCVUJf")

for vaga in vagas:
    empresa = vaga.find('p', class_="sc-efBctP dpAAMR sc-a3bd7ea-6 cQyvth").text
    nomeVaga = vaga.find('h2', class_="sc-llJcti jgKUZ sc-a3bd7ea-5 XNNQK").text
    dictVaga.update({"Nome": nomeVaga, "Empresa": empresa})
    dados = vaga.find_all('div', class_="sc-23336bc7-2 hCmVmU")
    i = 0

    # Loop que itera pelas informações de local, tipo de emprego, modelo do emprego e se é vaga para PcD
    for dado in dados:
        if (i == 0):
            dictVaga.update({"Local": dado.text})
        elif (i == 1):
            dictVaga.update({"Tipo": dado.text})
        elif (i == 2):
            dictVaga.update({"Modelo": dado.text})
        elif (i == 3):
            dictVaga.update({"Vaga para PcD": "Sim"})
        i += 1
    if (dictVaga.get("Vaga para PcD") == ""):
        dictVaga.update({"Vaga para PcD": "Não"})

    # Grava as informações no CSV
    writer.writerow(dictVaga)
```
A ideia principal dessa parte do código é o Web Scraping em usa maioria usando o nome específico da classe, já que apenas duas se repetem. Nessas classes é feito uma iteração para obter a informação de cada html tag de cada. No loop interno, há 4 condicionais if, as quais tem o propósito de ver qual informação deve ser armazenada em qual chave do dicionário dictVaga. Por fim, é gravados as informações do dicionário no arquivo .csv

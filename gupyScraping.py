from bs4 import BeautifulSoup
import requests
import csv

# Obtem a url, faz o request da pagina e converte de html para texto
url = 'https://portal.gupy.io/job-search/term=desenvolvedor'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Cria o header e abre o CSV
header = ["Nome", "Empresa", "Local", "Tipo", "Modelo", "Vaga para PcD"]
csvfile = open("Vagas.csv", "w", newline="", encoding="utf-8")
writer = csv.DictWriter(csvfile, fieldnames=header)
writer.writeheader()

# Cria o dicionário no qual as informações irão ser guardadas
d = {"Nome": "", "Empresa": "", "Local": "", "Modelo": "", "Tipo": "", "Vaga para PcD": ""}
vagas = soup.find_all('a', class_="sc-a3bd7ea-1 kCVUJf")

# Loop que itera pelas vagas
for vaga in vagas:
    empresa = vaga.find('p', class_="sc-efBctP dpAAMR sc-a3bd7ea-6 cQyvth").text
    nomeVaga = vaga.find('h2', class_="sc-llJcti jgKUZ sc-a3bd7ea-5 XNNQK").text
    d.update({"Nome": nomeVaga, "Empresa": empresa})
    dados = vaga.find_all('div', class_="sc-23336bc7-2 hCmVmU")
    i = 0

    # Loop que itera pelas informações de local, tipo de emprego, modelo do emprego e se é vaga para PcD
    for dado in dados:
        if (i == 0):
            d.update({"Local": dado.text})
        elif (i == 1):
            d.update({"Tipo": dado.text})
        elif (i == 2):
            d.update({"Modelo": dado.text})
        elif (i == 3):
            d.update({"Vaga para PcD": "Sim"})
        i += 1
    if (d.get("Vaga para PcD") == ""):
        d.update({"Vaga para PcD": "Não"})

    # Grava as informações no CSV
    writer.writerow(d)

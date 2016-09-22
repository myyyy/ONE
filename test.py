import requests
import bs4
root_url = 'http://wufazhuce.com/article/1536'
response = requests.get(root_url)
soup = bs4.BeautifulSoup(response.text,"html.parser")

for i in soup.select('.comilla-cerrar'):
    cerrar = i.get_text().strip()
for i in soup.select('.articulo-titulo'):
    titulo = i.get_text().strip()

for i in soup.select('.articulo-autor'):
    autor = i.get_text().strip()
for i in soup.select('.articulo-contenido'):
    contenido = i.get_text().strip()
print cerrar
print titulo
print autor
print contenido
filename = 'ONE-ARTICLE\\'+titulo+'.md'
file = open('test.md', 'w')
file.write('> '+cerrar+'\n\n')
file.write('###'+titulo+'\n')
file.write('####'+autor+'\n')
file.write(contenido)
file.close()
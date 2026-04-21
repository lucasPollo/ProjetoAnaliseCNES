-1 clonar o repositorio

git clone https://github.com/lucasPollo/ProjetoAnaliseCNES.git
cd ProjetoAnaliseCnes

-2 ativar o ambiente virtual

python -m venv venv
venv\Scripts\activate  

-3 instalar dependencias

pip install -r requirements.txt

-4 rodar o servidor
python manage.py runserver


-5 teste de endpoints localmente

http://127.0.0.1:8000/api/estabelecimento/2569302/resumo/
http://127.0.0.1:8000/api/indicadores/distribuicao-cbo/?municipio=260960
http://127.0.0.1:8000/api/analise/sobrecarga/




-------------------------------------------------------------------
Dicionário de Dados

-No primeiro endopoint retorna o id do cnes, o nome do
estabelecimento, o id do municipio, o nome do municipio e total de profissionais, teve que
ser usado join com as tabelas de municipios e  profissionaisvinculosnosestabelecimentos

cnes = cnes_id
nomefantasia = nome
idmunicipio = municipio
nomemunicipio = nome_municipio
contagem de id profissionais = total_profissionais


-No segundo endpoint retorna o nome do municipio, o id do cbo, o
nome do cbo e o total de profssionais, foi utilizado junçao com
estabelecimentos, municipios e especialidades

municipio = nomemunicipio
idespecialidade = cbo
nomedaespecialidade = nome_cbo
soma de profissioanis = total








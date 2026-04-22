Guia de instalacão e setup

-Temos dois bancos de dados, o primeiro default(dbInterno) eo segundo de leitura(dbCnes),
para configuração, crie cada um localmente(Dbeaver ou PgAdmin) e adicione os dois no arquivo de settings.py, os dados necessarios para cada um estão no arquivo .env

-1 clonar o repositorio

git clone https://github.com/lucasPollo/ProjetoAnaliseCNES.git
cd ProjetoAnaliseCnes

-2 criar e ativar o ambiente virtual

python -m venv venv
venv\Scripts\activate  

-3 instalar dependencias

pip install -r requirements.txt

-4 rodar o servidor
python manage.py runserver


-5 teste de endpoints localmente

cnes para teste:
2682818
2760223
2127849

http://127.0.0.1:8000/api/estabelecimento/2569302/resumo/



id municipio para teste:
430350
430410
420540


http://127.0.0.1:8000/api/indicadores/distribuicao-cbo/?idmunicipio=260960




http://127.0.0.1:8000/api/analise/sobrecarga/


-------------------------------------------------------------------
Dicionário de Dados

-No primeiro endpoint(estabelecimento) retorna o id do cnes, o nome do
estabelecimento, o id do municipio, o nome do municipio e total de profissionais, teve que
ser usado join com as tabelas de municipios e  profissionaisvinculosnosestabelecimentos


dados na esquerda = nomes reais no db
dados na direita = nomes usados nos retornos json

cnes = cnes_id
nomefantasia = nome
idmunicipio = municipio
nomemunicipio = nome_municipio
contagem de id profissionais = total_profissionais


-No segundo endpoint(indicadores) retorna o nome do municipio, o id do cbo, o
nome do cbo e o total de profssionais, foi utilizado junção com
estabelecimentos, municipios e especialidades


municipio = nomemunicipio
idespecialidade = cbo
nomedaespecialidade = nome_cbo
soma de profissioanis = total


-No ultimo endpoint(analise) retorna o id do 
profissional e a soma total de carga horaria superior a 60 horas

idprofissional = id_profissional
soma de carga horaria = carga_total



-----------------------------------------------------------------------------
Desenho da Arquitetura(explicação visual em imgs/arquiteturaProjeto)


VIEW:
Responsável por receber as 
requisições HTTP dos usuários (endpoints da API) 
e retornar as respostas em formato JSON


SERVICE:
Responsável por processar 
os dados recebidos do repository e aplicar as regras do sistema

REPOSITORY:
Responsável por executar as 
consultas SQL diretamente no banco 
de dados CNES, essa camada isola o SQL das 
demais partes do sistema


--------------------------------------------------------------------
Explicação Tecnica

O mapeamento dos dados foi feito através das tuplas retornadas, com o uso do cursor.execute, foi
feita a conversão das tuplas em dicionarios, utilizei cursor.description e zip com
dict para estruturar os dados melhor no repositorio de analise, e nos outros apenas fetchone e fetchall
Falando sobre a segurança, utilizei de parametros nas consultas sql, passando valores recebidos 
utilizandos %s, para que o próprio db trate esses valores de forma segura, além disso utilizei a 
estrutura de conexões with connections, que fecha automaticamento o cursor após a consulta requerida garantindo
ainda mais segurança contra sql injection














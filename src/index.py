import shutil, os, json

# Adcionar um novo registro ao JSON
def escreverJson(data, arquivo):
    with open(arquivo, "w") as f:
        json.dump(data, f, indent=4);

# Renomear todos os arquivos para que posteriormente possa renomear novamente na ordem correta
def renomear(caminho, extensao):
   i = 1;
   for filename in os.listdir(caminho):
      if filename.endswith(format(extensao)):
         meu_dest = "" + str(i) + "i" + extensao;
         meu_caminho = caminho + filename;
         meu_dest = caminho + meu_dest;
         os.rename(meu_caminho, meu_dest);
         i += 1;

# Renoameando os arquivos de forma correta, numéricamente.
# exemplo: 1, 2, 3, 4... o dois sendo cópia do um e assim sucessivamente 
def renomearCopias(caminho, extensao):
   i = 1;
   for filename in os.listdir(caminho):
      if filename.endswith(format(extensao)):
         meu_dest = "" + str(i) + extensao;
         meu_caminho = caminho + filename;
         meu_dest = caminho + meu_dest;
         os.rename(meu_caminho, meu_dest);
         i += 1;

# arquivo onde será armazenado o registro da pasta em que seus arquivos ja foram duplicados
arquivo = "data.json";
# a extensão dos arquivos que serão copiados na pasta
extensao = ".png";
#alterar de acordo com a pasta que quiser
caminho = "C:/Users/Lucas/Desktop/pasta_teste/";
# armazenando todas as pastas do caminho escolhido
pastas = os.listdir(caminho);
pastas.sort(key = int);

#  abrindo o arquivo com os registros e armazenando em uma variavel
with open(arquivo, 'r') as openfile:
   json_data = json.load(openfile);

# array onde sera armazenado os nomes das pastas que estão no diretório escolhido e esta no registro do JSON
pasta_obj = []
for obj in json_data['pastas']:
   if obj['pasta'] in pastas:
      pasta_obj.append(obj['pasta'])

pasta_obj.sort(key = int)

# substituindo os registros no JSON para apenas as pastas onde ja foram duplicadas e que elas estejam correspondentes ao diretório em que estão
assoc = dict()
assoc["pastas"] = []
for i in pasta_obj:
   y = {"pasta": i}
   assoc["pastas"].append(y);


with open(arquivo, "w") as f:
   json.dump(assoc, f, indent=4);

#abrindo novamente o json e armazenando seus registros em um array
with open(arquivo, 'r') as openfile:
   json_data2 = json.load(openfile);

#array com o nome das pastas do JSON
i = 0
pastasJson = []
for item in json_data2['pastas']:
   pastasJson.append(item["pasta"])
   i += 1

pastasJson.sort(key = int);

#array que será armazenado as pastas que ainda não foram duplicadas
diferente = [];
for item in pastas:
   if item not in pastasJson:
      diferente.append(item)

diferente.sort(key = int);

#loop para duplicar os arquivos que estão dentro das pastas ainda não duplicadas e renomeando corretamente e depois registrando no json
for item in diferente:
   caminhoFinal = caminho + item + "/";
   i = 1
   for folders, subfolders, filenames in os.walk(caminhoFinal):
      for filename in filenames:
         if filename.endswith(format(extensao)):
                        shutil.copy(os.path.join(folders, filename), os.path.join(folders, "" + str(i) + "_copia" + extensao))
                        i += 1
   if __name__ == '__main__':
      renomear(caminhoFinal, extensao);
      renomearCopias(caminhoFinal, extensao);
   with open(arquivo) as json_file:
      data = json.load(json_file);
      temp = data["pastas"];
      y = {"pasta": item};
      temp.append(y);
   escreverJson(data, arquivo);
   print("Deu ceeeeeeeeeeerto")
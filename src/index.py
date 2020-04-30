import shutil, os, json

def escreverJson(data, arquivo):
    with open(arquivo, "w") as f:
        json.dump(data, f, indent=4);

def renomear(caminho, extensao):
   i = 1;
   for filename in os.listdir(caminho):
      if filename.endswith(format(extensao)):
         meu_dest = "" + str(i) + "i" + extensao;
         meu_caminho = caminho + filename;
         meu_dest = caminho + meu_dest;
         os.rename(meu_caminho, meu_dest);
         i += 1;

def renomearCopias(caminho, extensao):
   i = 1;
   for filename in os.listdir(caminho):
      if filename.endswith(format(extensao)):
         meu_dest = "" + str(i) + extensao;
         meu_caminho = caminho + filename;
         meu_dest = caminho + meu_dest;
         os.rename(meu_caminho, meu_dest);
         i += 1;

arquivo = "data.json";
extensao = ".png";
#alterar de acordo com a pasta que quiser
caminho = "C:/Users/kldbr/Desktop/new_test/";
pastas = os.listdir(caminho);
pastas.sort(key = int);
ultimaPosicao = len(pastas) - 1;

with open(arquivo, 'r') as openfile:
   json_object = json.load(openfile);

nei = []
for obj in json_object['pastas']:
   if obj['pasta'] in pastas:
      nei.append(obj['pasta'])

assoc = dict()
assoc["pastas"] = []
for pi in nei:
   y = {"pasta": pi}
   assoc["pastas"].append(y);


with open(arquivo, "w") as f:
   json.dump(assoc, f, indent=4);

with open(arquivo, 'r') as openfile:
   json_object2 = json.load(openfile);


i = 0
pastasJson = []
for item in json_object2['pastas']:
   pastasJson.append(item["pasta"])
   i += 1

pastasJson.sort(key = int);
diferente = [];
for item in pastas:
   if item not in pastasJson:
      diferente.append(item)

diferente.sort(key = int);


for item in diferente:
   caminhoFinal = caminho + item + "/";
   i = 1
   for folders, subfolders, filenames in os.walk(caminhoFinal):
      for filename in filenames:
         if filename.endswith(format(extensao)):
                        shutil.copy(os.path.join(folders, filename), os.path.join(folders, "" + str(i) + "_copia" + extensao))
                        print("deu certo")
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

import shutil, os

def renomear(caminho):
   i = 1
   for filename in os.listdir(caminho):
      if filename.endswith(format('.png')):
         meu_dest ="" + str(i) + extensao
         meu_caminho =caminho + filename
         meu_dest =caminho + meu_dest
         os.rename(meu_caminho, meu_dest)
         i += 1

extensao = '.png'
#print("digite o caminho onde está as pastas de origem e destino: ")
caminho = os.getcwd() + "/"
print("digite o nome da pasta de origem: ")
pasta_origem = input()
#print("digite o nome da pasta de destino: ")
#pasta_final = input()
caminho_origem = caminho + pasta_origem
caminho_final = caminho

for folders, subfolders, filenames in os.walk(caminho_origem):
    for filename in filenames:
        if filename.endswith(format(extensao)):
            shutil.copy(os.path.join(folders, filename), caminho_final)
            print("deu certo")

if __name__ == '__main__':
   renomear(caminho_final + '/')

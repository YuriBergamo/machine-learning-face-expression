# machine-learning-face-expression
Algoritmo basico de reconhecimento de expressoes faciais usando a lib do python opencv

## primeiros passos
Os primeiros passos de reconhecimento de expressões faciais consiste no reconhecimento das faces. Para entendermos mais sobre isso fiz um exemplo em python que reconhece o rosto e marca com o retangulo (pasta face-detection)

## Principios do reconhecimento de imagem
É bom entendermos como funciona as funçes do opencv que chamamos. 
A primeira que chamamos é a CascadeClassifier, que é um algoritmo baseado em passos (steps) de reconhecimento facial. A ideai inicial era que para cada imagem a i.a cria 6000 classificadores para identificar se aquela imagem em questão é ou não um rosto. Porém esse teste é feito praticamente pixel por pixel, então  é como se ela identifica-se pixel por pixel a imagem e pergunta-se: "Isso é um rosto?"... "Isso é um rosto?"
Para obter essa resposta, a i.a deveria obter esse 6000 classificadores de cada pedaço da imagem, o que demoraria um tempo considerável, já que as imagens hj possuem pelo menos 1020x720px e é claro que o reconhecimento de uma imagem demoraria muito tempo para um computador com processamento mediano.
Por isso a opencv tem essa função chamada Cascade, que é um método de identificação que aplica de 30~50 passos para uma "triagem" dos pixels. Se ele passar nos passos, será aplicado os classificadores, se não, o algoritmo nem chega a executar, fazendo o trabalho de horas se transformar em real time.

 
## Para começar a executar o exemplo
  ### primeiro vamos instalar o python
  
No linux já vem instalado, porém faça os seguintes passos
`python3 - V`
se retornar uma versão superior a 3.3 ok
se não faça
```
sudo apt-get update
sudo apt-get -y upgrade
```
ira atualizar seu linux e consequentemente ira baixar a nova versao do python

No Windows é só baixar do site e next-next-next finish

### depois instalar o opencv
No linux também já vai estar instalado, só para garantir dé os comandos
```
sudo apt-get update
sudo apt-get -y upgrade
```
e teste no console assim
```
pyhton
>>> import cv2
```
se voce rodar esse comando e nao obter erro algum esta tudo certo :D
  

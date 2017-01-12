# machine-learning-face-expression
Algoritmo basico de reconhecimento de expressoes faciais usando a lib do python angus.ai

## how it works?
  A entrada de dados consiste em um input stream de imagens continuas (video) ou pre-carregado ou a live que ira servir de amostragem para o algoritmo
  
  A saida de dados sera um JSON com o retorno da i.a com as seguintes entidades
    
  -  **input_size**: sera a resolucao da imagem que foi enviada, quanto maior a resolucao, melhor sera o reconhecimento
  -  **nb_faces** : sera o numero de faces reconhecidas
  -  **roi** : para cada face um roi sera calculado, que sera tamanho e posicionamento do quadrado onde a face foi detectada
  -  **roi_confidence** : sera o quanto a imagem reconhecida e real ou nao (lembrando 0 é o menos real e 1 é o mais real)
  -  **neutral** : indica em uma escala de 0 a 1 se o rosto é neutro 
  -  **happiness**: indica em uma escala de 0 a 1 se o rosto esta contente
  -  **surprise** : indica em uma escala de 0 a 1 se o rosto está surpreso
  -  **anger**: indica em uma escala de 0 a 1 se o rosto esta nervoso
  -  **sadness** : indica em uma escala de 0 a 1 se o rosto esta triste
  

## como usar esse treco?  
 Exite a opção de usar a api em python (não phyton... serio, isso nao existe kkk) e em java. Como somos *hardusers* vamos ir pro python!
 
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

### executando
  

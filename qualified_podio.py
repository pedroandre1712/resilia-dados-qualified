def podio_olimpico(tempo_chegada1, tempo_chegada2,tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3):
  # Implemente aqui a lógica da função
  a = {tempo_chegada1:nome_corredor1, tempo_chegada2:nome_corredor2, tempo_chegada3:nome_corredor3}
  b = [tempo_chegada1, tempo_chegada2, tempo_chegada3]
  b.sort()
  espaco = " minutos\n"
  variavel_de_retorno = "1 - " + a[b[0]] + " - " + str(b[0]) + espaco +"2 - " + a[b[1]] + " - " + str(b[1]) + espaco +"3 - " + a[b[2]] + " - " + str(b[2]) + espaco
  return variavel_de_retorno
def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
    # Implemente aqui a lógica da função
  a = [tempo_chegada1, tempo_chegada2, tempo_chegada3]
  a.sort()
  espaco = " minutos\n"
  variavel_de_retorno = "1 - " + str(a[0]) + espaco + "2 - " + str(a[1]) + espaco + "3 - " + str(a[2]) + espaco
  return variavel_de_retorno
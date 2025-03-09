source("objetivo_g/utils.R")

calculaMedia <- function (vetor, verbose = TRUE){

  assertVetorNumerio(vetor)

  if (verbose) {
    #todo formatar
    print(paste('Calculando media de ', paste(vetor, collapse = ', ')))
  }

  #aparentemente em R sempre retorna o ultimo valor numa função, não precisa usar return
  mean(vetor)

}

#executa somente se este for o arquivo principal
if (sys.nframe() == 0) {
  print(calculaMedia(c(1, 5, 4.3)))
}

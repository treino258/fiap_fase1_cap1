source("objetivo_g/utils.R")
source("objetivo_g/calcula_media.R")

desvioSimples <- function (vetor, verbose = TRUE){
  media <- calculaMedia(vetor, verbose = FALSE)

  desvio_simples <- vetor - media

  if (verbose) {
    #todo formatar
    print(paste('O desvio simples é: ', paste(desvio_simples, collapse = ', ')))

  }
  return(desvio_simples)

}

desvioAbsolutoMedio <- function (vetor, verbose = TRUE){
  desvios <- desvioSimples(vetor, FALSE)

  absoluto_medio <- mean(abs(desvios))

  if (verbose){
    #todo formatar
    print(paste('O desvio absoluto médio é:', paste(absoluto_medio, collapse = ', ')))
  }

  return(absoluto_medio)

}

desvioPadraoAmostral <- function (vetor, verbose = TRUE){

  assertVetorNumerio(vetor)

  desvio_padrao <- sd(vetor)

  print(desvio_padrao)

  if (verbose){
    #todo formatar
    print(paste('O desvio padrão é:', desvio_padrao))
  }

  return(desvio_padrao)

}

desvioRelativoPercentual <- function (vetor, verbose = TRUE){

  dam <- desvioAbsolutoMedio(vetor, verbose = FALSE)
  media <- calculaMedia(vetor, verbose = FALSE)

  desvio_relativo <- (dam / media) * 100

  if (verbose){
    #todo formatar percentual
    print(paste("O desvio relativo percentual é: ", desvio_relativo))
  }

  return(desvio_relativo)

}


#executa somente se este for o arquivo principal
if (sys.nframe() == 0) {

  x <- c(1, 5, 4.3)

  print(desvioSimples(x))
  print(desvioAbsolutoMedio(x))
  print(desvioPadraoAmostral(x))
  print(desvioRelativoPercentual(x))
}

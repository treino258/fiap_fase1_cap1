source("objetivo_g/read_file.R")
source("objetivo_g/calcula_media.R")
source("objetivo_g/calcula_desvio.R")

sair <- function (){
    sair <- tolower(trimws(readline(prompt = "Tem certeza que deseja sair? (s/n)")))

    if (sair == 's'){
        quit(save = "no")
    } else if (sair == 'n'){
        print("voltando ao menu")
    } else {
        print("Opção invalida, voltando ao menu")
    }
}

menu <- function(){

  data <- loadData()


  while(TRUE){
    cat(strrep("-", 20), "\n")
    cat(sprintf("%10s\n", "Menu"))
    cat(strrep("-", 20), "\n")
    print("1 - Calcular media")
    print("2 - Calcular desvio simples")
    print("3 - Calcular desvio absoluto medio")
    print("4 - Calcular desvio padrao amostral")
    print("5 - Calcular desvio relativo percentual")
    print("6 - Sair")

    opcao <- trimws(readline(prompt = "Digite a opcao: "))

    switch(opcao,
      '1' = calculaMedia(data),
      '2' = desvioSimples(data),
      '3' = desvioAbsolutoMedio(data),
      '4' = desvioPadraoAmostral(data),
      '5' = desvioRelativoPercentual(data),
      '6' = sair(),
      print('Opcao invalida')
    )
  }
}

if (sys.nframe() == 0) {
  menu()
}
install.packages(c("openmeteo"), lib= 'ir_alem/lib', repos = "https://cloud.r-project.org/")
library('openmeteo', lib.loc = "ir_alem/lib")
library('tibblify', lib.loc = "ir_alem/lib")
library('withr', lib.loc = "ir_alem/lib")
library('purrr', lib.loc = "ir_alem/lib")
library('testthat', lib.loc = "ir_alem/lib")
library('dplyr', lib.loc = "ir_alem/lib")
library('tidyr', lib.loc = "ir_alem/lib")

#Repo: https://github.com/tpisel/openmeteo

if (sys.nframe() == 0) {

 weather_now('Sao Paulo', timezone = 'America/Sao_Paulo')
 weather_forecast('Sao Paulo',
                  start = Sys.Date(),
                  end = Sys.Date()+ 7,
                  daily = "temperature_2m_max",
                  timezone = 'America/Sao_Paulo')
 weather_history('Sao Paulo',
                  start = Sys.Date() - 8,
                  end = Sys.Date() - 1,
                  daily = "temperature_2m_max",
                 timezone = 'America/Sao_Paulo')
 # weather_variables()


}
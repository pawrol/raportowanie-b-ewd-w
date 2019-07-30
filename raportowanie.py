import traceback
try:
  raise Exception('Komunikat błędu')
exceprt:
  plik_bledow = open('plik_bledow.txt', 'w')
  plik_bledow.write(traceback.format_exc())
  plik_bledow.close()

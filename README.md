# adayazilim-reservation
mulakat



flask web framework üzerine HTTP API
POST request ile check_reservation fonksiyonu hizmete açık.

endpoint : /reservation -> accepts json -> returns json


API'a public erisim icin

https://berf.pythonanywhere.com/are_we_online/

buradan online olup olmadigimizi test edebilir

https://berf.pythonanywhere.com/reservation/ url'sine HTTP POST istegi gonderebilirsiniz

ornek :

requests.post("https://berf.pythonanywhere.com/reservation/",json=c3).json()


{'RezervasyonYapilabilir': True,
 'YerlesimAyrinti': [{'KisiSayisi': 1, 'VagonAdi': 'Vagon 1'},
  {'KisiSayisi': 2, 'VagonAdi': 'Vagon 2'},
  {'KisiSayisi': 3, 'VagonAdi': 'Vagon 3'}]}

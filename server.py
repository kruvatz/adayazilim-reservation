# assumptions

# -  kisi sayisi 0 ve ya negatif olmadığı

# -  vagonda 1 den kucuk ( mesela 0.9 ) yer varsa insan sigdirilmayacagi

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/reservation/', methods=['POST'])
def reservation():
    print(check_reservation(request.json))
    return check_reservation(request.json)

@app.route('/are_we_online/', methods=['GET'])
def are_we_online():
    return "it's working!"

    
    

def get_total_available_seat_numbers(vagonlar):
    return sum([get_available_seat_number(vagon) for vagon in vagonlar])
            

def get_available_seat_number(vagon):
    avail_seats = int(vagon["Kapasite"]*0.7) - vagon["DoluKoltukAdet"] # floor da yapan int donusumu, yarim insan olur mu :)
    if avail_seats > 0:
        return avail_seats
    return 0
                
    
def check_reservation(input_):
    flag_Farkli_Vagon = input_["KisilerFarkliVagonlaraYerlestirilebilir"]
    toplamKisi=input_["RezervasyonYapilacakKisiSayisi"]
    tren=input_["Tren"]
    vagonlar=tren["Vagonlar"]
    
    if flag_Farkli_Vagon:
        
        if get_total_available_seat_numbers(vagonlar) < toplamKisi:
            
            return {        
                "RezervasyonYapilabilir":False,
                "YerlesimAyrinti":[]
                        }

        # rezervasyon yapilabilir
        return_dict={
                    "RezervasyonYapilabilir":True,
                    "YerlesimAyrinti":[]
                }
        # bastan doldurmaya baslayalim
        for vagon in vagonlar:
            
            if not toplamKisi: #eger herkes yerlestirilmisse cikabiliriz
                break
            
            vagon_avail=get_available_seat_number(vagon)
            if not vagon_avail: # yer yok
                continue
            #yer var
            
            # eger bos yer kalan kisi sayisindan fazlaysa kisi sayisi kadar insan yerlesecek
            yerlesenKisiSayisi = toplamKisi if vagon_avail > toplamKisi else vagon_avail
            
            yeniAyrinti = {"VagonAdi":vagon["Ad"],"KisiSayisi":yerlesenKisiSayisi}
            return_dict["YerlesimAyrinti"].append(yeniAyrinti)
            
            # yerlestirdiklerimizi cikaralim
            toplamKisi-=yerlesenKisiSayisi
        
        return return_dict
        
    else:
        # amacimiz 1 vagon bulmak, o vagon toplam kisi sayisini sigdirabilsin
        return_dict={
                    "RezervasyonYapilabilir":False,  # false assumed
                    "YerlesimAyrinti":[]
                }
        
        for vagon in vagonlar:
            vagon_avail=get_available_seat_number(vagon)
            
            if vagon_avail < toplamKisi:
                continue # diger vagona bakalim
            
            # bulundu
            yeniAyrinti = {"VagonAdi":vagon["Ad"],"KisiSayisi":toplamKisi}
            
            return_dict["RezervasyonYapilabilir"]=True
            return_dict["YerlesimAyrinti"].append(yeniAyrinti)
            
            break
        
        return return_dict
        
        
        
        
        
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=105)
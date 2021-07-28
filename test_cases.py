class Cases:
    
 
    
    # Cases

    # farkli -> true , bos yer = 20, kisi = 3
    test_cases = { 
    "c1" : {
        "Tren":
        {
            "Ad":"Başkent Ekspres",
            "Vagonlar":
            [
                {"Ad":"Vagon 1", "Kapasite":100, "DoluKoltukAdet":50},
                {"Ad":"Vagon 2", "Kapasite":90, "DoluKoltukAdet":80},
                {"Ad":"Vagon 3", "Kapasite":80, "DoluKoltukAdet":80}
            ]
        },
        "RezervasyonYapilacakKisiSayisi":3,
        "KisilerFarkliVagonlaraYerlestirilebilir":True
    },

    # farkli -> true , bos yer = 0, kisi = 3
    "c2" : {
        "Tren":
        {
            "Ad":"Başkent Ekspres",
            "Vagonlar":
            [
                {"Ad":"Vagon 1", "Kapasite":70, "DoluKoltukAdet":50},
                {"Ad":"Vagon 2", "Kapasite":90, "DoluKoltukAdet":80},
                {"Ad":"Vagon 3", "Kapasite":80, "DoluKoltukAdet":80}
            ]
        },
        "RezervasyonYapilacakKisiSayisi":3,
        "KisilerFarkliVagonlaraYerlestirilebilir":True
    },

    # farkli -> true , bos yer = 6, kisi = 6
    "c3" : {
        "Tren":
        {
            "Ad":"Başkent Ekspres",
            "Vagonlar":
            [
                {"Ad":"Vagon 1", "Kapasite":100, "DoluKoltukAdet":69},
                {"Ad":"Vagon 2", "Kapasite":100, "DoluKoltukAdet":68},
                {"Ad":"Vagon 3", "Kapasite":100, "DoluKoltukAdet":67}
            ]
        },
        "RezervasyonYapilacakKisiSayisi":6,
        "KisilerFarkliVagonlaraYerlestirilebilir":True
    },


    # farkli -> true , bos yer = 6, kisi = 7
    "c4" : {
        "Tren":
        {
            "Ad":"Başkent Ekspres",
            "Vagonlar":
            [
                {"Ad":"Vagon 1", "Kapasite":100, "DoluKoltukAdet":69},
                {"Ad":"Vagon 2", "Kapasite":100, "DoluKoltukAdet":68},
                {"Ad":"Vagon 3", "Kapasite":100, "DoluKoltukAdet":67}
            ]
        },
        "RezervasyonYapilacakKisiSayisi":7,
        "KisilerFarkliVagonlaraYerlestirilebilir":True
    },



    # farkli -> false , bos yer = 6, kisi = 3
    "c5" : {
        "Tren":
        {
            "Ad":"Başkent Ekspres",
            "Vagonlar":
            [
                {"Ad":"Vagon 1", "Kapasite":100, "DoluKoltukAdet":69},
                {"Ad":"Vagon 2", "Kapasite":100, "DoluKoltukAdet":68},
                {"Ad":"Vagon 3", "Kapasite":100, "DoluKoltukAdet":67}
            ]
        },
        "RezervasyonYapilacakKisiSayisi":3,
        "KisilerFarkliVagonlaraYerlestirilebilir":False
    },


    # farkli -> false , bos yer = 6, kisi = 4
    "c6" : {
        "Tren":
        {
            "Ad":"Başkent Ekspres",
            "Vagonlar":
            [
                {"Ad":"Vagon 1", "Kapasite":100, "DoluKoltukAdet":69},
                {"Ad":"Vagon 2", "Kapasite":100, "DoluKoltukAdet":68},
                {"Ad":"Vagon 3", "Kapasite":100, "DoluKoltukAdet":67}
            ]
        },
        "RezervasyonYapilacakKisiSayisi":4,
        "KisilerFarkliVagonlaraYerlestirilebilir":False
    }
        
    }
    
    def __init__(self):
        pass
def discount(persenan):
    def hargaDiskon(harga):
        ans = harga - (harga * persenan / 100)
        return ans
    return hargaDiskon


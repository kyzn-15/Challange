def discount(rate):
    return lambda harga: harga - (harga * rate / 100)
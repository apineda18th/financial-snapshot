def payout_annuity(pmt, r, n):
    
    return (pmt * (1-(r/n)**(-n*r)))/(r/n)

print(payout_annuity(1000, 0.05, 12))

def fv(pv, r, n):
    return pv * (1 + r)**n
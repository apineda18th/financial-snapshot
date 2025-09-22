def payout_annuity(pmt, r, n):
    
    return (pmt * (1-(r/n)**(-n*f)))/(r/n)

print(payout_annuity(1000, 0.05, 12))  
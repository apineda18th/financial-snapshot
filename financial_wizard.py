def payout_annuity(pv, r, n):
    """
    The payout annuity calculates the expected payout of annuity given a PV and earned r
    :param pv: present value
    :param r: rate of interest per period
    :param n: total number of payment periods
    :return: pmt
    """
    
    return (pv * r)/(1 - (1+r)**-n)


def fv_ordinary_annuity(pmt, r, n):
    """
    This is used to figure out how much a series of regular deposits will grow to in the future
    :param pmt: payment (each period)
    :param r: discount rate
    :param n: total number of payment periods
    :return: future value
    """
    return pmt * ((1 + r)**n-1)/(r)

def pv_ordinary_annuity(pmt, r, n):
    """
    Used to find the present value of a series of regular deposits
    :param pmt: payment (each period)
    :param r: discount rate
    :param n: number of payment periods
    :return: present value
    """
    return pmt * (1/r-1/(r*(1+r)**n))


def pmt_given_pv(pv, r, n):
    """
    Find the expected payments given the present value. For example, buying a home and trying to figure out what the monthly cost would be.
    :param pv: present va
    :param r: rate of interest per period
    :param n: number of payment periods
    :return:
    """
    return pv / (1/r-1/(r*(1+r)**n))


def perpetuity(pmt, r):
    """
    returns the fair value of a perpetuity given the expected payout and the discount factor
    :param pmt: payout
    :param r: discount factor
    :return:
    """
    return pmt / r

def fv_growing_ordinary_annuity(pmt, r, n, g):
    """
    returns the future value of a series of regular deposits that are growing at a g rate
    :param pmt: deposits per period
    :param r: discount factor per period
    :param n: number of periods
    :param g: growth rate
    :return: the future value of growing deposits
    """
    return pmt * ((1+r)**n-(1+g)**n)/(r-g)

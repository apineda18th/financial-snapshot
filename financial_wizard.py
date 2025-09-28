import numpy as np

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

def pv_annuity_due(pmt, r, n):
    """
    Used to find the present value of a series of regular deposits due immediately
    :param pmt: payment (each period)
    :param r: discount rate
    :param n: number of payment periods
    :return: present value
    """
    return pmt * ((1/r-1/(r*(1+r)**n))*(1+r))


def pmt_given_pv(pv, r, n):
    """
    Find the expected payments given the present value. For example, buying a home and trying to figure out what the monthly cost would be.
    :param pv: present value
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



def duration(cfs, ytm, bond_price):
    """
    Returns the weighted average time until cash flows are received, also known as Macaulay Duration
    :param cfs: cash flows (list or array)
    :param ytm: yield to maturity (as a decimal)
    :param bond_price: current bond price
    :return: Macaulay Duration
    """
    weighted_times = []
    for i in range(len(cfs)):
        pv = cfs[i] / (1 + ytm) ** (i+1)
        weight = pv / bond_price
        weighted_times.append(weight * (i+1))

    return np.sum(weighted_times)


def modified_duration(cfs, ytm, bond_price):
    """
    Returns the modified duration, which measures the price sensitivity of a bond to interest rate changes
    :param cfs: cash flows (list or array)
    :param ytm: yield to maturity (as a decimal)
    :param bond_price: current bond price
    :return: Modified Duration
    """
    d = duration(cfs, ytm, bond_price)
    return d / (1 + ytm)


def convexity(cfs, ytm, bond_price):
    """
    Returns the convexity of a bond, which measures the curvature in the relationship between bond prices and bond yields
    :param cfs: cash flows (list or array)
    :param ytm: yield to maturity (as a decimal)
    :param bond_price: current bond price
    :return: Convexity
    """
    convexity_sum = 0
    for i in range(len(cfs)):
        pv = cfs[i] / (1 + ytm) ** (i+1)
        convexity_sum += pv * (i+1) * (i+2)

    return convexity_sum / (bond_price * (1 + ytm) ** 2)


print(convexity([5, 5, 105], 0.05, 95.23))
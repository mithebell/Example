#! /usr/bin/env python
"""
A script to simulate a population of stars around the Andromeda galaxy
"""
import math
import random

def get_radec():
    """
    Determine Andromeda location in ra/dec degrees
    """
    # from wikipedia
    RA = '00:42:44.3'
    DEC = '41:16:09'

    # convert to decimal degrees
    D, M, S = DEC.split(':')
    DEC = int(D)+int(M)/60+float(S)/3600

    H, M, S = RA.split(':')
    RA = 15*(int(H)+int(M)/60+float(S)/3600)
    RA = RA/math.cos(DEC*math.pi/180)

    return RA, DEC

NSRC = 1_000_000

def make_stars(RA, DEC, NUM_STARS):
    """
    make 1000 stars within 1 degree of Andromeda
    """
    RAS = []
    DECS = []
    for i in range(NSRC):
        RAS.append(RA + random.uniform(-1, 1))
        DECS.append(DEC + random.uniform(-1, 1))
    return RAS, DECS

def main():
    RA, DEC = get_radec()
    RAS, DECS = make_stars(RA, DEC, NSRC)

    # now write these to a csv file for use by my other program
    with open('catalog.csv', 'w', encoding='utf-8') as F:
        print("id,ra,dec", file=F)
        for i in range(NSRC):
            print(f"{i:07d}, {RAS[i]:12f}, {DECS[i]:12f}", file=F)

if __name__ == '__main__':
    main()

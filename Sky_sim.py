#! /usr/bin/env python
"""
A script to simulate a population of stars around the Andromeda galaxy
"""
import math
import random
import argparse

def get_radec():
    """
    Determine Andromeda location in ra/dec degrees
    by converting RA and DEC from hexadecimal to decimal
    
    Returns
    -------
    ra : float
        The RA, in degrees, for Andromeda
    dec : float
        The DEC, in degrees for Andromeda
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

def make_stars(RA, DEC, NUM_STARS=1000000):
    """
    Generates 10^6 stars within 1 degree of Andromeda
    """
    RAS = []
    DECS = []
    for i in range(NSRC):
        RAS.append(RA + random.uniform(-1, 1))
        DECS.append(DEC + random.uniform(-1, 1))
    return RAS, DECS

def skysim_parser():
    """
    Configure the argparse for skysim

    Returns
    -------
    parser : argparse.ArgumentParser
        The parser for skysim.
    """
    parser = argparse.ArgumentParser(prog='sky_sim', prefix_chars='-')
    parser.add_argument('--RA', dest = 'RA', type=float, default=None,
                        help="Central ra (degrees) for the simulation location")
    parser.add_argument('--DEC', dest = 'DEC', type=float, default=None,
                        help="Central dec (degrees) for the simulation location")
    parser.add_argument('--out', dest='out', type=str, default='catalog.csv',
                        help='destination for the output catalog')
    return parser

if __name__ == "__main__":
    parser = skysim_parser()
    options = parser.parse_args()
    # if ra/dec are not supplied the use a default value
    if None in [options.RA, options.DEC]:
        RA, DEC = get_radec()
    else:
        RA = options.RA
        DEC = options.DEC
    
    RAS, DECS = make_stars(RA, DEC, )
    # now write these to a csv file for use by my other program
    with open(options.out,'w') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print(f"{i:07d}, {RAS[i]:12f}, {DECS[i]:12f}", file=f)
    print(f"Wrote {options.out}")
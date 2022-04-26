# -----------------------------------------------------------------------------
# Wsection.py -- create a standard W section
#       (c) Farshad Rasuli, 2021-2022
#
# E-Mail: farshad.rasuli@gmail.com
# github.com/farshadrasuli/OpenSeesPy/tree/main/OpenSees%20Examples/Example%205
# farshadrasuli.github.io/OpenSeesPy
#
# Inspired from:
# Wsection.tcl -- create a standard W section given the nominal section properties
#		Remo M. de Souza, 1999
# -----------------------------------------------------------------------------
'''
input arguments:
	secTag - section Tag number
	matTag - material Tag number 
	d  = nominal depth
	tw = web thickness
	bf = flange width
	tf = flange thickness
	nfdw = number of fibers along web depth 
	nftw = number of fibers along web thickness
	nfbf = number of fibers along flange width
	nftf = number of fibers along flange thickness
'''
# Section profile
#         /──────────bf─────────/         
#         ┌─────────────────────┐ /  /
#         │                     │ tf │
#         └────────┐   ┌────────┘ /  │
#                  │   │          │  │
#                  │ y │          │  │
#                  │ ▲ │          │  │
#                  │ │ │          │  │
#                  │ │ │          │  │
#              z◄──┼─┘ │          dw d
#                  │   │          │  │
#                  │   │          │  │
#                  │   │          │  │
#                  │   │          │  │
#                  │   │          │  │
#         ┌────────┘   └────────┐ /  │
#         │                     │ tf │
#         └─────────────────────┘ /  /
#                  /tw/
# 

import openseespy.opensees as ops
import openseespy.postprocessing.ops_vis as opsv

import matplotlib.pyplot as plt

def section(secTag, secTitle, matTag, d, bf, tf, tw, nfdw, nftw, nfbf, nftf):
    dw = d - 2*tf
    y1 = - d / 2
    y2 = - dw / 2
    y3 = dw / 2
    y4 = d / 2

    z1 = - bf / 2
    z2 = - tw / 2
    z3 =  tw / 2
    z4 =  bf / 2
    
    #            secType, secTag
    ops.section( 'Fiber', secTag)
    #           type, matTag, numSubdivIJ, numSubdivJK, yI, zI, yJ, zJ, yK, zK, yL, zL
    # bottom flange
    ops.patch('quad', matTag,        nfbf,        nftf, y1, z4, y1, z1, y2, z1, y2, z4)
    # web
    ops.patch('quad', matTag,        nftw,        nfdw, y2, z3, y2, z2, y3, z2, y3, z3)
    # top flange
    ops.patch('quad', matTag,        nfbf,        nftf, y3, z4, y3, z1, y4, z1, y4, z4)

    fib_sec = [
        ['section', 'Fiber', secTag, '-GJ', 0],
        ['patch', 'quad', matTag,        nfbf,        nftf, y1, z4, y1, z1, y2, z1, y2, z4],
        ['patch', 'quad', matTag,        nftw,        nfdw, y2, z3, y2, z2, y3, z2, y3, z3],
        ['patch', 'quad', matTag,        nfbf,        nftf, y3, z4, y3, z1, y4, z1, y4, z4]
              ]
    opsv.plot_fiber_section(fib_sec, matcolor='r')
    plt.axis('equal')
    plt.title(secTitle)
    plt.gca().invert_xaxis()
    plt.show()

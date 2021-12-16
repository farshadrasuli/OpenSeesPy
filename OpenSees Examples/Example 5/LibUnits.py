# ----------------------------------------------------------------------------
# LibUnits.py -- define system of units
#       (c) Farshad Rasuli, 2021
#
# E-Mail: farshad.rasuli@gmail.com
# github.com/farshadrasuli/OpenSeesPy/tree/main/OpenSees%20Examples/Example%205/
# farshadrasuli.github.io/OpenSeesPy
#
# Inspired from:
# LibUnits.tcl -- define system of units
#		Silvia Mazzoni & Frank McKenna, 2006
# -----------------------------------------------------------------------------

import math

# define UNITS
inch = 1.0			# define basic units -- output units
kip = 1.0 			# define basic units -- output units
sec = 1.0 			# define basic units -- output units
LunitTXT = "inch"			# define basic-unit text for output
FunitTXT = "kip"			# define basic-unit text for output
TunitTXT = "sec"			# define basic-unit text for output
m = inch / 0.0254	    		# define basic SI units -- output units
N = kip / 4.45e3          # define basic SI units -- output units
# define engineering units
ft = 12*inch
ksi = kip/math.pow(inch,2)
psi = 1.e-3*ksi
lbf = psi*inch*inch	        # pounds force
pcf = lbf/math.pow(ft,3)		# pounds per cubic foot
psf = lbf/math.pow(ft,3)		# pounds per square foot
in2 = inch*inch         		# inch^2
in4 = inch*inch*inch*inch 	# inch^4
cm = m / 100    		        # centimeter, needed for displacement input in MultipleSupport excitation
PI = 2*math.asin(1.0)	      # define constants
g = 32.2*ft/math.pow(sec,2) # gravitational acceleration
Ubig = 1.e10        		  	# a really large number
Usmall = 1/Ubig         		# a really small number

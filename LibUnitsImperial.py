# -----------------------------------------------------------------------------
# LibUnits.py -- define system of units
#       (c) Farshad Rasuli, 2021-2022
#
# E-Mail: farshad.rasuli@gmail.com
# github.com/farshadrasuli/OpenSeesPy
# farshadrasuli.github.io/OpenSeesPy
#
# Inspired from:
# LibUnits.tcl -- define system of units
#		Silvia Mazzoni & Frank McKenna, 2006
# -----------------------------------------------------------------------------

import math

# define UNITS

inch = 1.0                          # define basic units -- output units for length
sec = 1.0                           # define basic units -- output units for time
kip = 1.0                           # define basic units -- output units for force
Slug = kip*math.pow(sec,2)/inch     # define basic units -- output units for mass
rad = 1.0                           # define basic units -- output units for angles

MunitTXT = "Slug (kip-s²/in)"       # define basic unit text for mass output
LunitTXT = "inch"                   # define basic unit text for length output
TunitTXT = "sec"                    # define basic unit text for time output
FunitTXT = "kip"                    # define basic unit text for force output
AunitTXT = "rad"                    # define basic unit text for angle output

m = inch / 0.0254                   # define basic SI units -- output units
N = kip / 4448.2216                 # define basic SI units -- output units
kg = N*math.pow(sec,2)/m            # define basic SI units -- output units



# define engineering units
ft = 12*inch                        # foot

g = 32.17404856*ft/math.pow(sec,2)  # gravitational acceleration

ton = 1.e3*kg                       # metric tonne equal to 1,000 kilo-gram

degree = 180.0/math.pi*rad          # degree

ksi = kip/math.pow(inch,2)          # kilo-pounds per square inch
psi = 1.e-3*ksi                     # pounds per square inch
lbf = 1.e-3*kip                     # pounds force
plf = lbf/ft                        # pounds per linear foot
psf = lbf/math.pow(ft,2)            # pounds per square foot
pcf = lbf/math.pow(ft,3)            # pounds per cubic foot

slug = lbf*math.pow(sec,2)/ft       # Imperial mass = slug or pound-square second per inch

cm = 1.e-2*m                        # centimeter, needed for displacement input in Multiple Support excitation
mm = 1.e-3*m                        # mili-meter

kN = 1.e3*N                         # kilo-Newton
MN = 1.e6*N                         # Mega-Newton

kgf = N*g                           # kilo-gram-force
tonf = kgf/1000.0                   # tonne-force

Pa = N/math.pow(m,2)                # Newton per square meter
kPa = 1.e3*Pa                       # kilo-Pascal or kilo-Newton per square meter
MPa = 1.0e6*Pa                      # Mega-Pascal or Newton per square mili-meter or Mega-Newton per square meter
GPa = 1.0e9*Pa                      # Giga-Pascal or kilo-Newton per square mili-meter or Giga-Newton per square meter

in2 = math.pow(inch,2)              # inch²
in3 = math.pow(inch,3)              # inch³
in4 = math.pow(inch,4)              # inch⁴
ft2 = math.pow(ft,2)                # ft²
m2 = math.pow(m,2)                  # m²
m3 = math.pow(m,3)                  # m³
m4 = math.pow(m,4)                  # m⁴
cm2 = math.pow(cm,2)                # cm²
cm3 = math.pow(cm,3)                # cm³
cm4 = math.pow(cm,4)                # cm⁴
mm2 = math.pow(mm,2)                # mm²
mm3 = math.pow(mm,3)                # mm³
mm4 = math.pow(mm,4)                # mm⁴


pi = 2*math.asin(1.0)               # define π

Ubig = 1.e10                        # a really large number
Usmall = 1/Ubig                     # a really small number

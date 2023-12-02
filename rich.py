#!/usr/bin/env python3
"""
the command-line Mendeleeve table
"""

import sys
import random

notNums = ['57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '89' ,'90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '102', '103']

class MyTable:
    def __init__(self, symbol = None, elc = None, group = None, period = None):
        self.syl = str(symbol)
        self.elc = str(elc)
        self.group = str(group)
        self.pr = str(period)

    def launch(self):
        if self.syl:
            syl = self.syl
            if syl == "H":
                print("""
Symbol: H
Name: Hydrogen
Atomic Number: 1
Average Atomic Mass: 1.008
Group: 1
Period: 1
Layer Info: 1S¹
""")
            elif syl == "Li":
                print("""
Symbol: Li
Name: Lithium
Atomic Number: 3
Average Atomic Mass: 6.94
Group: 1
Period: 2
Layer Info: 1S²/2S²
""")
            elif syl == "Na":
                print("""
Symbol: Na
Name: Sodium
Atomic Number: 11
Average Atomic Mass: 22.99
Group: 1
Period: 3
Last Layer info: 1S²/2S² 2P⁶/3S¹
""")
            elif syl == "K" or syl == "K".lower():
                print("""
Symbol: K
Name: Potassium
Atomic Number: 19
Average Atomic Mass: 39.10
Group: 1
Period: 4
Layer info: 1S²/2S² 2P⁶/3S² 3P⁶ / 4S¹
""")
            elif syl == "Rb":
                print("""
Symbol: Rb
Name: Rubidium
Atomic Number: 37
Average Atomic Mass: 85.47
Group: 1
Period: 5
Layer info: 1S²/2S² 2P⁶/3S² 3P⁶ 3d¹⁰/ 4S² 4P¹
""")
            elif syl == "Cs":
                print("""
Symbol: Cs
Name: Caesium
Atomic Number: 55
Average Atomic Mass: 132.9
Group: 1
Period: 6
Layer info: 1S²/2S² 2P⁶/3S² 3P⁶ 3d¹⁰/ 4S² 4P⁶ 4d¹⁰/ 5S² 5P¹
""")

            elif syl == "Fr":
                print("""
Symbol: Fr
Name: Francium
Atomic Number: 87
Average Atomic Mass: 223
Group: 1
Period: 7
Layer info: 1S²/2S² 2P⁶/3S² 3P⁶ 3d¹⁰/ 4S² 4P⁶ 4d¹⁰/ 5S² 5P⁶ /
        """)
            
            elif syl == "Be":
                print("""
Symbol: Be
Name: Beryllium
Atomic Number: 4
Average Atomic Mass: 9.012
Group: 2
Period: 2
Layer info: 1S²/2S²
""")
            elif syl == "Mg":
                print("""
Symbol: Mg
Name: Magnesium
Atomic Number: 12
Average Atomic Mass: 24.31
Group: 2
Period: 3
Layer info: 1S²/2S² 2P⁶/ 3S²
""")
        
            elif syl == "Ca":
                print("""
Symbol: Ca
Name: Calcium
Atomic Number: 20
Average Atomic Mass: 40.08
Group: 2
Period: 4
Layer info: 1S²/2S² 2P⁶ 2d8/ 3S²
""")
            
            elif syl == "Sr":
                print("""
Symbol: Sr
Name: Strontium
Atomic Number: 38
Average Atomic Mass: 87.62
Group: 2
Period: 5
Layer info: 1S²/2S² 2P⁶ 2d10/ 3S² 3P⁶ 3d8/ 4S²
""")
                
            elif syl == "Ba":
                print("""
Symbol: Ba
Name: Barium
Atomic Number: 56
Average Atomic Mass: 137.3
Group: 2
Period: 6
""")
            
            elif syl == "Ra":
                print("""
Symbol: Ra
Name: Radium
Atomic Number: 88
Average Atomic Mass: 226
Group: 2
Period: 7
""")
            elif syl == "Sc":
                print("""
Symbol: Sc
Name: Scandium
Atomic Number: 21
Average Atomic Mass: 44.96
Group: 3
Period: 4
Layer info: 1S2 / 2S2 2P6/ 3S2 3P6 3d1 / 4S1
""")
                
            elif syl == "Y":
                print("""
Symbol: Y
Name: Yttrium
Atomic Number: 39
Average Atomic Mass: 88.91
Group: 3
Period: 5                        
""")
                
            elif syl == "Ti":
                print("""
Symbol: Ti
Name: Titanium
Atomic Number: 22
Average Atomic Mass: 47.88
Group: 4
Period: 4
Layer info: 1S2 / 2S2 2P6/ 3S2 3P6 3d2 / 4S2
""")
                
            elif syl == "Zr":
                print("""
Symbol: Zr
Name: Zirconium
Atomic Number: 40
Average Atomic Mass: 91.22
Group: 4
Period: 5
""")
                
            elif syl == "Hf":
                print("""
Symbol: Hf
Name: Hafnium
Atomic Number: 72
Average Atomic Mass: 178.5
Group: 4
Period: 6
""")
                
            elif syl == "Rf":
                print("""
Symbol: Rf
Name: Rutherfordium
Atomic Number: 104
Average Atomic Mass: 265
Group: 4
Period: 7
""")
                
            elif syl == "V":
                print("""
Symbol: V
Name: Vanadium
Atomic Number: 23
Average Atomic Mass: 50.94
Group: 5
Period: 4
Layer info: 1S2 / 2S2 2P6/ 3S2 3P6 3d2/ 4S2
""")
            elif syl == "Nb":
                print("""
Symbol: Nb
Name: Niobium
Atomic Number: 41
Average Atomic Mass: 92.91
Group: 5
Period: 5
""")
                
            elif syl == "Ta":
                print("""
Symbol: Ta
Name: Tantalum
Atomic Number: 73
Average Atomic Mass: 180.9
Group: 5
Period: 6
""")
                
            elif syl == "Db":
                print("""
Symbol: Db
Name: Dubinum
Atomic Number: 105
Average Atomic Mass: 268
Group: 5
Period: 7
""")

            elif syl == "Cr":
                print("""
Symbol: Cr
Name: Chromium
Atomic Number: 24
Average Atomic Mass: 52.00
Group: 6
Period: 4
Layer info: 1S2 / 2S2 2P6/ 3S2 3P6 3d4/ 4S2
""")
                
            elif syl == "Mo":
                print("""
Symbol: Mo
Name: Molybdenum
Atomic Number: 42
Average Atomic Mass: 95.96
Group: 6
Period: 5
Layer info: 1S2 / 2S2 2P6/ 3S2 3P6 3d10/ 4S2 4P6 4d4 / 5S2
""")
                
            elif syl == "W" or syl == "W".lower():
                print("""
Symbol: W
Name: Tungsten
Atomic Number: 74
Average Atomic Mass: 183.9
Group: 6
Period: 6
""")
                
            elif syl == "Sg":
                print("""
Symbol: Sg
Name: Seaborgium
Atomic Number: 106
Average Atomic Mass: 271
Group: 6
Period: 7
""")
                
            elif syl == "Mn":
                print("""
Symbol: Mn
Name: Manganese
Atomic Number: 25
Average Atomic Mass: 54.94
Group: 7
Period: 4
""")
            elif syl == "Tc":
                print("""
Symbol: Tc
Name: Technetium
Atomic Number: 43
Average Atomic Mass: 98
Group: 7
Period: 5
""")
            elif syl == "Re":
                print("""
Symbol: Re
Name: Rhenium
Atomic Number: 75
Average Atomic Mass: 186.2
Group: 7
Period: 6
""")
                
            elif syl == "Bh":
                print("""
Symbol: Bh
Name: Bohrium
Atomic Number: 107
Average Atomic Mass: 270
Group: 7
Period: 7
""")
                
            elif syl == "Fe":
                print("""
Symbol: Fe
Name: Iron
Atomic Number: 26
Average Atomic Mass: 55.85
Group: 8
Period: 4
""")
            elif syl == "Ru":
                print("""
Symbol: Ru
Name: Ruthenium
Atomic Number: 44
Average Atomic Mass: 101.1
Group: 8
Period: 5
""")
            
            elif syl == "Os":
                print("""
Symbol: Os
Name: Osmium
Atomic Number: 76
Average Atomic Mass: 190.2
Group: 8
Period: 6
""")
            
            elif syl == "Hs":
                print("""
Symbol: Hs
Name: Hassium
Atomic Number: 108
Average Atomic Mass: 277
Group: 8
Period: 7
""")
                
            elif syl == "Co":
                print("""
Symbol: Co
Name: Cobalt
Atomic Number: 27
Average Atomic Mass: 58.93
Group: 9
Period: 4
""")
            elif syl == "Rh":
                print("""
Symbol: Rh
Name: Rhodium
Atomic Number: 45
Average Atomic Mass: 101.1
Group: 9
Period: 5
""")
            elif syl == "Ir":
                print("""
Symbol: Ir
Name: Iridium
Atomic Number: 77
Average Atomic Mass: 192.2
Group: 9
Period: 6
""")
            elif syl == "Mt":
                print("""
Symbol: Mt
Name: Meitnerium
Atomic Number: 109
Average Atomic Mass: 276
Group: 9
Period: 7
""")
                
            elif syl == "Ni":
                print("""
Symbol: Ni
Name: Nickle
Atomic Number: 28
Average Atomic Mass: 58.69
Group: 10
Period: 4
""")
                
            elif syl == "Pd":
                print("""
Symbol: Pd
Name: Palladium
Atomic Number: 46
Average Atomic Mass: 106.4
Group: 10
Period: 5
""")
                
            elif syl == "Pt":
                print("""
Symbol: Pt
Name: Platinum
Atomic Number: 78
Average Atomic Mass: 195.1
Group: 10
Period: 6
""")
                
            elif syl == "Ds":
                print("""
Symbol: Ds
Name: Darmstadtium
Atomic Number: 110
Average Atomic Mass: 281
Group: 10
Period: 7
""")
                
            elif syl == "Cu":
                print("""
Symbol: Cu
Name: Copper
Atomic Number: 29
Average Atomic Mass: 63.55
Group: 11
Period: 4
""")
            elif syl == "Ag":
                print("""
Symbol: Ag
Name: Silver
Atomic Number: 47
Average Atomic Mass: 107.9
Group: 11
Period: 5
""")
            elif syl == "Au":
                print("""
Symbol: Au
Name: Gold
Atomic Number: 79
Average Atomic Mass: 197.0
Group: 11
Period: 6
""")
                
            elif syl == "Rg":
                print("""
Symbol: Rg
Name: Roentgenium
Atomic Number: 111
Average Atomic Mass: 280
Group: 11
Period: 7
""")
                
            elif syl == "Zn":
                print("""
Symbol: Zn
Name: Zinc
Atomic Number: 30
Average Atomic Mass: 65.39
Group: 12
Period: 4
""")
            
            elif syl == "Cd":
                print("""
Symbol: Cd
Name: Cadmium
Atomic Number: 48
Average Atomic Mass: 112.4
Group: 12
Period: 5
""")
                
            elif syl == "Hg":
                print("""
Symbol: Hg
Name: Mercury
Atomic Number: 80
Average Atomic Mass: 200.5
Group: 12
Period: 6
""")
            elif syl == "Cn":
                print("""
Symbol: Cn
Name: Copernicium
Atomic Number: 112
Average Atomic Mass: 285
Group: 12
Period: 7
""")
                
            elif syl == "B":
                print("""
Symbol: B
Name: Boron
Atomic Number: 5
Average Atomic Mass: 10.81
Group: 13
Period: 2
""")
            elif syl == "Al":
                print("""
Symbol: Al
Name: Aluminium
Atomic Number: 13
Average Atomic Mass: 26.98
Group: 13
Period: 3
""")

            elif syl == "Ga":
                print("""
Symbol: Ga
Name: Gallium
Atomic Number: 31
Average Atomic Mass: 69.72
Group: 13
Period: 4
""")
                
            elif syl == "In":
                print("""
Symbol: In
Name: Indium
Atomic Number: 49
Average Atomic Mass: 114.8
Group: 13
Period: 5
""")
            
            elif syl == "Tl":
                print("""
Symbol: Tl
Name: Thallium
Atomic Number: 81
Average Atomic Mass: 204.38
Group: 13
Period: 6
""")
                
            elif syl == "Nh":
                print("""
Symbol: Nh
Name: Nihonium
Atomic Number: 113
Average Atomic Mass: 284
Group: 13
Period: 7
""")
            
            elif syl == "C" or syl == "C".lower():
                print("""
Symbol: C
Name: Carbon
Atomic Number: 6
Average Atomic Mass: 12.01
Group: 14
Period: 2
""")
            elif syl == "Si":
                print("""
Symbol: Si
Name: Silicon
Atomic Number: 14
Average Atomic Mass: 28.09
Group: 14
Period: 3
""")
            
            elif syl == "Ge":
                print("""
Symbol: Ge
Name: Germanium
Atomic Number: 32
Average Atomic Mass: 72.64
Group: 14
Period: 4
""")
                
            elif syl == "Sn":
                print("""
Symbol: Sn
Name: Tin
Atomic Number: 50
Average Atomic Mass: 118.7
Group: 14
Period: 5
""")
            
            elif syl == "Pb":
                print("""
Symbol: Pb
Name: Lead
Atomic Number: 82
Average Atomic Mass: 207.2
Group: 14
Period: 6
""")
            
            elif syl == "Fl":
                print("""
Symbol: Fl
Name: Flerovium
Atomic Number: 114
Average Atomic Mass: 289
Group: 14
Period: 7
""")
                
            elif syl == "N" or syl == "N".lower():
                print("""
Symbol: N
Name: Nitrogen
Atomic Number: 7
Average Atomic Mass: 14.01
Group: 15
Period: 2
""")
            
            elif syl == "P" or syl == "P".lower():
                print("""
Symbol: P
Name: Phosphorus
Atomic Number: 15
Average Atomic Mass: 30.97
Group: 15
Period: 3
""")
            
            elif syl == "As":
                print("""
Symbol: As
Name: Arsenic
Atomic Number: 33
Average Atomic Mass: 74.92
Group: 15
Period: 4
""")
                
            elif syl == "Sb":
                print("""
Symbol: Sb
Name: Amtimoney
Atomic Number: 51
Average Atomic Mass: 121.8
Group: 15
Period: 5
""")
                
            elif syl == "Bi":
                print("""
Symbol: Bi
Name: Bismuth
Atomic Number: 83
Average Atomic Mass: 209.0
Group: 15
Period: 6
""")
                
            elif syl == "Mc":
                print("""
Symbol: Mc
Name: Moscovium
Atomic Number: 115
Average Atomic Mass: 288
Group: 15
Period: 7
""")
            
            elif syl == "O" or syl == "O".lower():
                print("""
Symbol: O
Name: Oxygen
Atomic Number: 8
Average Atomic Mass: 16.00
Group: 16
Period: 2
""")
            
            elif syl == "S" or syl == "S".lower():
                print("""
Symbol: S
Name: Sulfur
Atomic Number: 16
Average Atomic Mass: 32.06
Group: 16
Period: 3
""")  
              
            elif syl == "Se":
                print("""
Symbol: Se
Name: Selenium
Atomic Number: 34
Average Atomic Mass: 78.96
Group: 16
Period: 4
""")
            
            elif syl == "Te":
                print("""
Symbol: Te
Name: Tellurium
Atomic Number: 52
Average Atomic Mass: 127.6
Group: 16
Period: 5
""")
                
            elif syl == "Po":
                print("""
Symbol: Po
Name: Polonium
Atomic Number: 84
Average Atomic Mass: 209
Group: 16
Period: 6
""")
                
            elif syl == "Lv":
                print("""
Symbol: Lv
Name: Livermorium
Atomic Number: 116
Average Atomic Mass: 293
Group: 16
Period: 7
""")
                
            elif syl == "F" or syl == "F".lower():
                print("""
Symbol: F
Name: Fluorine
Atomic Number: 9
Average Atomic Mass: 19.00
Group: 17
Period: 2
""")
                
            elif syl == "Cl":
                print("""
Symbol: Cl
Name: Chlorine
Atomic Number: 17
Average Atomic Mass: 35.45
Group: 17
Period: 3
""")
                
            elif syl == "Br":
                print("""
Symbol: Br
Name: Bromine
Atomic Number: 35
Average Atomic Mass: 79.90
Group: 17
Period: 4
""")
                
            elif syl == "l":
                print("""
Symbol: l
Name: lodine
Atomic Number: 53
Average Atomic Mass: 126.9
Group: 17
Period: 5
""")
                
            elif syl == "At":
                print("""
Symbol: At
Name: Astatine
Atomic Number: 85
Average Atomic Mass: 210
Group: 17
Period: 6
""")
            elif syl == "Ts":
                print("""
Symbol: Ts
Name: Tennessine
Atomic Number: 117
Average Atomic Mass: 294
Group: 17
Period: 7
""")
                
            elif syl == "He":
                print("""
Symbol: He
Name: Helium
Atomic Number: 2
Average Atomic Mass: 4.003
Group: 18
Period: 1
""")
                
            elif syl == "Ne":
                print("""
Symbol: Ne
Name: Neon
Atomic Number: 10
Average Atomic Mass: 20.18
Group: 18
Period: 2
""")
                
            elif syl == "Ar":
                print("""
Symbol: Ar
Name: Argon
Atomic Number: 18
Average Atomic Mass: 39.95
Group: 18
Period: 3
""")
            elif syl == "Kr":
                print("""
Symbol: Kr
Name: Krypton
Atomic Number: 36
Average Atomic Mass: 83.79
Group: 18
Period: 4
""")
                
            elif syl == "Xe":
                print("""
Symbol: Xe
Name: Xenon
Atomic Number: 54
Average Atomic Mass: 131.3
Group: 18
Period: 5
""")
                
            elif syl == "Rn":
                print("""
Symbol: Rn
Name: Radon
Atomic Number: 86
Average Atomic Mass: 222
Group: 18
Period: 6
""")
                
            elif syl == "Og":
                print("""
Symbol: Og
Name: Oganesson
Atomic Number: 118
Average Atomic Mass: 294
Group: 18
Period: 7
""")
            
            #else:print(f"\nthe '{syl}' does not exists in Mendeleeve table.")
            
        if self.elc:
            elc = self.elc
            if elc == "1":
                print("""
Symbol: H
Name: Hydrogen
Atomic Number: 1
Average Atomic Mass: 1.008
Group: 1
Period: 1
Layer Info: 1S¹
""")
            elif elc == "2":
                print("""
Symbol: He
Name: Helium
Atomic Number: 2
Average Atomic Mass: 4.003
Group: 18
Period: 1
""")
                
            elif elc == "3":
                print("""
Symbol: Li
Name: Lithium
Atomic Number: 3
Average Atomic Mass: 6.94
Group: 1
Period: 2
Layer Info: 1S²/2S²
""")
                
            elif elc == "4":
                print("""
Symbol: Be
Name: Beryllium
Atomic Number: 4
Average Atomic Mass: 9.012
Group: 2
Period: 2
Layer info: 1S²/2S²
""")
                
            elif elc == "5":
                print("""
Symbol: B
Name: Boron
Atomic Number: 5
Average Atomic Mass: 10.81
Group: 13
Period: 2
""")
                
            elif elc == "6":
                print("""
Symbol: C
Name: Carbon
Atomic Number: 6
Average Atomic Mass: 12.01
Group: 14
Period: 2
""")
                
            elif elc == "7":
                print("""
Symbol: N
Name: Nitrogen
Atomic Number: 7
Average Atomic Mass: 14.01
Group: 15
Period: 2
""")
                
            elif elc == "8":
                print("""
Symbol: O
Name: Oxygen
Atomic Number: 8
Average Atomic Mass: 16.00
Group: 16
Period: 2
""")
                
            elif elc == "9":
                print("""
Symbol: F
Name: Fluorine
Atomic Number: 9
Average Atomic Mass: 19.00
Group: 17
Period: 2
""")
                
            elif elc == "10":
                print("""
Symbol: Ne
Name: Neon
Atomic Number: 10
Average Atomic Mass: 20.18
Group: 18
Period: 2
""")
                
            elif elc == "11":
                print("""
Symbol: Na
Name: Sodium
Atomic Number: 11
Average Atomic Mass: 22.99
Group: 1
Period: 3
Last Layer info: 1S²/2S² 2P⁶/3S¹
""")
                
            elif elc == "12":
                print("""
Symbol: Mg
Name: Magnesium
Atomic Number: 12
Average Atomic Mass: 24.31
Group: 2
Period: 3
Layer info: 1S²/2S² 2P⁶/ 3S²
""")
                
            elif elc == "13":
                print("""
Symbol: Al
Name: Aluminium
Atomic Number: 13
Average Atomic Mass: 26.98
Group: 13
Period: 3
""")
                
            elif elc == "14":
                print("""
Symbol: Si
Name: Silicon
Atomic Number: 14
Average Atomic Mass: 28.09
Group: 14
Period: 3
""")
                
            elif elc == "15":
                print("""
Symbol: P
Name: Phosphorus
Atomic Number: 15
Average Atomic Mass: 30.97
Group: 15
Period: 3
""")
                
            elif elc == "16":
                print("""
Symbol: S
Name: Sulfur
Atomic Number: 16
Average Atomic Mass: 32.06
Group: 16
Period: 3
""")  
                
            elif elc == "17":
                print("""
Symbol: Cl
Name: Chlorine
Atomic Number: 17
Average Atomic Mass: 35.45
Group: 17
Period: 3
""")
                
            elif elc == "18":
                print("""
Symbol: Ar
Name: Argon
Atomic Number: 18
Average Atomic Mass: 39.95
Group: 18
Period: 3
""")
                
            elif elc == "19":
                print("""
Symbol: K
Name: Potassium
Atomic Number: 19
Average Atomic Mass: 39.10
Group: 1
Period: 4
Layer info: 1S²/2S² 2P⁶/3S² 3P⁶ / 4S¹
""")
                
            elif elc == "20":
                print("""
Symbol: Ca
Name: Calcium
Atomic Number: 20
Average Atomic Mass: 40.08
Group: 2
Period: 4
Layer info: 1S²/2S² 2P⁶ 2d8/ 3S²
""")
            
            elif elc == "21":
                print("""
Symbol: Sc
Name: Scandium
Atomic Number: 21
Average Atomic Mass: 44.96
Group: 3
Period: 4
Layer info: 1S2 / 2S2 2P6/ 3S2 3P6 3d1 / 4S1
""")
                
            elif elc == "22":
                print("""
Symbol: Ti
Name: Titanium
Atomic Number: 22
Average Atomic Mass: 47.88
Group: 4
Period: 4
Layer info: 1S2 / 2S2 2P6/ 3S2 3P6 3d2 / 4S2
""")
                
            elif elc == "23":
                print("""
Symbol: V
Name: Vanadium
Atomic Number: 23
Average Atomic Mass: 50.94
Group: 5
Period: 4
Layer info: 1S2 / 2S2 2P6/ 3S2 3P6 3d2/ 4S2
""")
                
            elif elc == "24":
                print("""
Symbol: Cr
Name: Chromium
Atomic Number: 24
Average Atomic Mass: 52.00
Group: 6
Period: 4
Layer info: 1S2 / 2S2 2P6/ 3S2 3P6 3d4/ 4S2
""")
                
            elif elc == "25":
                print("""
Symbol: Mn
Name: Manganese
Atomic Number: 25
Average Atomic Mass: 54.94
Group: 7
Period: 4
""")
                
            elif elc == "26":
                print("""
Symbol: Fe
Name: Iron
Atomic Number: 26
Average Atomic Mass: 55.85
Group: 8
Period: 4
""")
            
            elif elc == "27":
                print("""
Symbol: Co
Name: Cobalt
Atomic Number: 27
Average Atomic Mass: 58.93
Group: 9
Period: 4
""")
                
            elif elc == "28":
                print("""
Symbol: Ni
Name: Nickle
Atomic Number: 28
Average Atomic Mass: 58.69
Group: 10
Period: 4
""")
                
            elif elc == "29":
                print("""
Symbol: Cu
Name: Copper
Atomic Number: 29
Average Atomic Mass: 63.55
Group: 11
Period: 4
""")
                
            elif elc == "30":
                print("""
Symbol: Zn
Name: Zinc
Atomic Number: 30
Average Atomic Mass: 65.39
Group: 12
Period: 4
""")
                
            elif elc == "31":
                print("""
Symbol: Ga
Name: Gallium
Atomic Number: 31
Average Atomic Mass: 69.72
Group: 13
Period: 4
""")
                
            elif elc == "32":
                print("""
Symbol: Ge
Name: Germanium
Atomic Number: 32
Average Atomic Mass: 72.64
Group: 14
Period: 4
""")
                
            elif elc == "33":
                print("""
Symbol: As
Name: Arsenic
Atomic Number: 33
Average Atomic Mass: 74.92
Group: 15
Period: 4
""")
                
            elif elc == "34":
                print("""
Symbol: Se
Name: Selenium
Atomic Number: 34
Average Atomic Mass: 78.96
Group: 16
Period: 4
""")
                
            elif elc == "35":
                print("""
Symbol: Br
Name: Bromine
Atomic Number: 35
Average Atomic Mass: 79.90
Group: 17
Period: 4
""")
                
            elif elc == "36":
                print("""
Symbol: Kr
Name: Krypton
Atomic Number: 36
Average Atomic Mass: 83.79
Group: 18
Period: 4
""")
                
            elif elc == "37":
                print("""
Symbol: Rb
Name: Rubidium
Atomic Number: 37
Average Atomic Mass: 85.47
Group: 1
Period: 5
Layer info: 1S²/2S² 2P⁶/3S² 3P⁶ 3d¹⁰/ 4S² 4P¹
""")
                
            elif elc == "38":
                print("""
Symbol: Sr
Name: Strontium
Atomic Number: 38
Average Atomic Mass: 87.62
Group: 2
Period: 5
Layer info: 1S²/2S² 2P⁶ 2d10/ 3S² 3P⁶ 3d8/ 4S²
""")
                
            elif elc == "39":
                print("""
Symbol: Y
Name: Yttrium
Atomic Number: 39
Average Atomic Mass: 88.91
Group: 3
Period: 5                        
""")
                
            elif elc == "40":
                print("""
Symbol: Zr
Name: Zirconium
Atomic Number: 40
Average Atomic Mass: 91.22
Group: 4
Period: 5
""")
                
            elif elc == "41":
                print("""
Symbol: Nb
Name: Niobium
Atomic Number: 41
Average Atomic Mass: 92.91
Group: 5
Period: 5
""")
                
            elif elc == "42":
                print("""
Symbol: Mo
Name: Molybdenum
Atomic Number: 42
Average Atomic Mass: 95.96
Group: 6
Period: 5
Layer info: 1S2 / 2S2 2P6/ 3S2 3P6 3d10/ 4S2 4P6 4d4 / 5S2
""")
                
            elif elc == "43":
                print("""
Symbol: Tc
Name: Technetium
Atomic Number: 43
Average Atomic Mass: 98
Group: 7
Period: 5
""")
                
            elif elc == "44":
                print("""
Symbol: Ru
Name: Ruthenium
Atomic Number: 44
Average Atomic Mass: 101.1
Group: 8
Period: 5
""")
                
            elif elc == "45":
                print("""
Symbol: Rh
Name: Rhodium
Atomic Number: 45
Average Atomic Mass: 101.1
Group: 9
Period: 5
""")
                
            elif elc == "46":
                print("""
Symbol: Pd
Name: Palladium
Atomic Number: 46
Average Atomic Mass: 106.4
Group: 10
Period: 5
""")
                
            elif elc == "47":
                print("""
Symbol: Ag
Name: Silver
Atomic Number: 47
Average Atomic Mass: 107.9
Group: 11
Period: 5
""")
                
            elif elc == "48":
                print("""
Symbol: Cd
Name: Cadmium
Atomic Number: 48
Average Atomic Mass: 112.4
Group: 12
Period: 5
""")
                
            elif elc == "49":
                print("""
Symbol: In
Name: Indium
Atomic Number: 49
Average Atomic Mass: 114.8
Group: 13
Period: 5
""")
                
            elif elc == "50":
                print("""
Symbol: Sn
Name: Tin
Atomic Number: 50
Average Atomic Mass: 118.7
Group: 14
Period: 5
""")
                
            elif elc == "51":
                print("""
Symbol: Sb
Name: Amtimoney
Atomic Number: 51
Average Atomic Mass: 121.8
Group: 15
Period: 5
""")
                
            elif elc == "52":
                print("""
Symbol: Te
Name: Tellurium
Atomic Number: 52
Average Atomic Mass: 127.6
Group: 16
Period: 5
""")
                
            elif elc == "53":
                print("""
Symbol: l
Name: lodine
Atomic Number: 53
Average Atomic Mass: 126.9
Group: 17
Period: 5
""")
                
            elif elc == "54":
                print("""
Symbol: Xe
Name: Xenon
Atomic Number: 54
Average Atomic Mass: 131.3
Group: 18
Period: 5
""")
                
            elif elc == "55":
                print("""
Symbol: Cs
Name: Caesium
Atomic Number: 55
Average Atomic Mass: 132.9
Group: 1
Period: 6
Layer info: 1S²/2S² 2P⁶/3S² 3P⁶ 3d¹⁰/ 4S² 4P⁶ 4d¹⁰/ 5S² 5P¹
""")
                
            elif elc == "56":
                print("""
Symbol: Ba
Name: Barium
Atomic Number: 56
Average Atomic Mass: 137.3
Group: 2
Period: 6
""")
            elif elc in notNums:
                print("will be soon.")
                
            elif elc == "72":
                print("""
Symbol: Hf
Name: Hafnium
Atomic Number: 72
Average Atomic Mass: 178.5
Group: 4
Period: 6
""")
            
            elif elc == "73":
                print("""
Symbol: Ta
Name: Tantalum
Atomic Number: 73
Average Atomic Mass: 180.9
Group: 5
Period: 6
""")
            elif elc == "74":
                print("""
Symbol: W
Name: Tungsten
Atomic Number: 74
Average Atomic Mass: 183.9
Group: 6
Period: 6
""")
                
            elif elc == "75":
                print("""
Symbol: Re
Name: Rhenium
Atomic Number: 75
Average Atomic Mass: 186.2
Group: 7
Period: 6
""")
                
            elif elc == "76":
                print("""
Symbol: Os
Name: Osmium
Atomic Number: 76
Average Atomic Mass: 190.2
Group: 8
Period: 6
""")
            
            elif elc == "77":
                print("""
Symbol: Ir
Name: Iridium
Atomic Number: 77
Average Atomic Mass: 192.2
Group: 9
Period: 6
""")
                
            elif elc == "78":
                print("""
Symbol: Pt
Name: Platinum
Atomic Number: 78
Average Atomic Mass: 195.1
Group: 10
Period: 6
""")
                
            elif elc == "79":
                print("""
Symbol: Au
Name: Gold
Atomic Number: 79
Average Atomic Mass: 197.0
Group: 11
Period: 6
""")
            
            elif elc == "80":
                print("""
Symbol: Hg
Name: Mercury
Atomic Number: 80
Average Atomic Mass: 200.5
Group: 12
Period: 6
""")
            elif elc == "81":
                print("""
Symbol: Tl
Name: Thallium
Atomic Number: 81
Average Atomic Mass: 204.38
Group: 13
Period: 6
""")
                
            elif elc == "82":
                print("""
Symbol: Pb
Name: Lead
Atomic Number: 82
Average Atomic Mass: 207.2
Group: 14
Period: 6
""")
            elif elc == "83":
                print("""
Symbol: Bi
Name: Bismuth
Atomic Number: 83
Average Atomic Mass: 209.0
Group: 15
Period: 6
""")
            elif elc == "84":
                print("""
Symbol: Po
Name: Polonium
Atomic Number: 84
Average Atomic Mass: 209
Group: 16
Period: 6
""")
            
            elif elc == "85":
                print("""
Symbol: At
Name: Astatine
Atomic Number: 85
Average Atomic Mass: 210
Group: 17
Period: 6
""")
                
            elif elc == "86":
                print("""
Symbol: Rn
Name: Radon
Atomic Number: 86
Average Atomic Mass: 222
Group: 18
Period: 6
""")
                
            elif elc == "87":
                print("""
Symbol: Fr
Name: Francium
Atomic Number: 87
Average Atomic Mass: 223
Group: 1
Period: 7
Layer info: 1S²/2S² 2P⁶/3S² 3P⁶ 3d¹⁰/ 4S² 4P⁶ 4d¹⁰/ 5S² 5P⁶ /
        """)
            
            elif elc == "88":
                print("""
Symbol: Ra
Name: Radium
Atomic Number: 88
Average Atomic Mass: 226
Group: 2
Period: 7
""")
                
            elif elc == "104":
                print("""
Symbol: Rf
Name: Rutherfordium
Atomic Number: 104
Average Atomic Mass: 265
Group: 4
Period: 7
""")
                
            elif elc == "105":
                print("""
Symbol: Db
Name: Dubinum
Atomic Number: 105
Average Atomic Mass: 268
Group: 5
Period: 7
""")
            
            elif elc == "106":
                print("""
Symbol: Sg
Name: Seaborgium
Atomic Number: 106
Average Atomic Mass: 271
Group: 6
Period: 7
""")
            
            elif elc == "107":
                print("""
Symbol: Bh
Name: Bohrium
Atomic Number: 107
Average Atomic Mass: 270
Group: 7
Period: 7
""")
                
            elif elc == "108":
                print("""
Symbol: Hs
Name: Hassium
Atomic Number: 108
Average Atomic Mass: 277
Group: 8
Period: 7
""")
                
            elif elc == "109":
                print("""
Symbol: Mt
Name: Meitnerium
Atomic Number: 109
Average Atomic Mass: 276
Group: 9
Period: 7
""")
                
            elif elc == "110":
                print("""
Symbol: Ds
Name: Darmstadtium
Atomic Number: 110
Average Atomic Mass: 281
Group: 10
Period: 7
""")
                
            elif elc == "111":
                print("""
Symbol: Rg
Name: Roentgenium
Atomic Number: 111
Average Atomic Mass: 280
Group: 11
Period: 7
""")
                
            elif elc == '112':
                print("""
Symbol: Cn
Name: Copernicium
Atomic Number: 112
Average Atomic Mass: 285
Group: 12
Period: 7
""")
                
            elif elc == "113":
                print("""
Symbol: Nh
Name: Nihonium
Atomic Number: 113
Average Atomic Mass: 284
Group: 13
Period: 7
""")
                
            elif elc == "114":
                print("""
Symbol: Fl
Name: Flerovium
Atomic Number: 114
Average Atomic Mass: 289
Group: 14
Period: 7
""")
                
            elif elc == "115":
                print("""
Symbol: Mc
Name: Moscovium
Atomic Number: 115
Average Atomic Mass: 288
Group: 15
Period: 7
""")
                
            elif elc == "116":
                print("""
Symbol: Lv
Name: Livermorium
Atomic Number: 116
Average Atomic Mass: 293
Group: 16
Period: 7
""")
                
            elif elc == "117":
                print("""
Symbol: Ts
Name: Tennessine
Atomic Number: 117
Average Atomic Mass: 294
Group: 17
Period: 7
""")
                
            elif elc == "118":
                print("""
Symbol: Og
Name: Oganesson
Atomic Number: 118
Average Atomic Mass: 294
Group: 18
Period: 7
""")
                

        if self.group:
            grp = self.group
            if grp == "1":
                print("""
H => 1
Li => 3
Na => 11
K => 19
Rb => 37
Cs => 55
Fr => 87
""")
            
            elif grp == "2":
                print("""
Be => 4
Mg => 12
Ca => 20
Sr => 38
Ba => 56
Ra => 88
""")
            elif grp == "3":
                print("""
Sc => 21
Y => 39
""")

            elif grp == "4":
                print("""
Ti => 22
Zr => 40
Hf => 72
Rf => 104
""")
                
            elif grp == "5":
                print("""
V => 23
Nb => 41
Ta => 73
Db => 105
""")
                
            elif grp == "6":
                print("""
Cr => 24
Mo => 42
W => 74
Sg =>  106
""")
                
            elif grp == "7":
                print("""
Mn => 25
Tc => 43
Re => 75
Bh => 107
""")
                
            elif grp == "8":
                print("""
Fe => 26
Ru => 44
Os => 76
Hs => 108
""")
                
            elif grp == "9":
                print("""
Co => 27
Rh = > 45
Ir => 77
Mt => 109
""")
                
            elif grp == "10":
                print("""
Ni => 28
Pd => 46
Pt => 78
Ds => 110
""")
            elif grp == "11":
                print("""
Cu => 29
Ag => 47
Au => 79
Rg => 111
""")
                
            elif grp == "12":
                print("""
Zn => 30
Cd => 48
Hg => 80
Cn => 112
""")
            
            elif grp == "13":
                print("""
B => 5
Al => 13
Ga => 31
In => 49
Tl => 81
Nh => 113
""")
            elif grp == "14":
                print("""
C => 6
Si => 14
Ge => 32
Sn => 50
Pb => 82
Fl => 114
""")
                
            elif grp == "15":
                print("""
N => 7
P => 15
As => 33
Sb => 51
Bi => 83
Mc => 115
""")
                
            elif grp == "16":
                print("""
O => 8
S => 16
Se => 34
Te => 52
Po => 84
Lv => 116
""")
                
            elif grp == "17":
                print("""
F => 9
Cl => 17
Br => 35
I => 53
At => 85
Ts => 117
""")
            elif grp == "18":
                print("""
He => 2
Ne => 10
Ar => 18
Kr => 36
Xe => 54
Rn => 86
Og => 118
""")

            


def Rich():
    try:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help" or sys.argv[1] == "?":
            print("""USAGE: rich [-s / --symbol] [-e / --electron] [-g / --group] <symbol> <electron> <group>:
symbol info: rich -s / --symbol Fe
electron info: rich -e / --electron 26
group info: rich -g / --group 4
""")

        elif sys.argv[1] == "-s" or sys.argv[1] == "--symbol":
            MyTable(symbol=sys.argv[2]).launch()
            
        elif sys.argv[1] == "-e" or sys.argv[1] == "--electron":
            MyTable(elc=sys.argv[2]).launch()
            
        elif sys.argv[1] == "-g" or sys.argv[1] == "--group":
            MyTable(group=sys.argv[2]).launch()
            

        else:print("USAGE: rich [-s / --symbol] <symbol>")

    except Exception as ESYS:
        print(ESYS)
        pass

Rich()
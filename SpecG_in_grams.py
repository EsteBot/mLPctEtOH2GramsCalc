# py simp GUI for LOCO_2_EXCEL 

import PySimpleGUI as sg

SG = float(input("Enter the specific gravity of the liquid you are diluting into H2O in g/mL).: "))
PS = float(input("Enter the percent (Vol/Vol) of the above liquid in the solution.   : "))
TV = float(input("Enter the total volume to be created in mL: "))

spec_grav   = SG
pct_of_soln = PS
tot_sol_vol = TV
water_vol   = round(TV-((PS/100)*TV),2)
dil_sol_vol = round(TV-water_vol,2)
dil_solnW   = round(SG*dil_sol_vol,2)
tot_solnW   = round(water_vol+dil_solnW,2)

ratio_solnW_by_totW =  dil_solnW/tot_solnW

print(spec_grav)
print(pct_of_soln)
print(tot_sol_vol)
print("The volume of H2O in the final solution is:\n"
+str(water_vol)+"mL.")
print("The volume of diluent in the final solution is:\n"
+str(dil_sol_vol)+"mL.")
print("The total weight of the final solution is:\n"
+str(tot_solnW)+"grams.")
print("The weight of the diluent in the final solution is:\n"
+str(dil_solnW)+"grams.")

V = input("To view the calculations for the above values, press 'v' then 'Enter'")

if V == 'v':
    print("End H2O volume = Total Volume - (Percent Vol/Vol * Total Volume)")
    print("End diluent volume = Total Volume - H2O Volume")
    print("End solution weight = End H2O Volume + diluent weight")
    print("End diluent weight = specific gravity of diluent * End Diluent Vol")
else:
    quit()


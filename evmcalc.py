#Coded by TheNebulaKing
#EVM Calculator

#ask user for input for what to be calculated,list of supported calculations.
prompt = str.upper(input('enter a what you would like to calculate: (CPI, CV, EAC, EAC2, EV, PV, SPI, SV, SV2) '))

#Calculate Cost Performance Index
if prompt == 'CPI':

	print('Cost Performance Index selected')
	EV = float(input(" Enter Earned Value: "))
	AC = float(input(" Enter Actual Cost: "))

	CPI = EV / AC
	print ('The Cost Performance Index result is:',CPI)

#Calculate Schedule Variance
elif prompt == 'SV':
	print('Schedule Variance selected')
	PV = float(input(" Enter Planned value: "))
	AC = float(input(" Enter Actual Cost: "))
	CV = float(input(" Enter Cost Variance: "))
	EV = CV + AC
	SV = PV - EV
	print(' The Schedule Variance is:',SV)

#Calculate Schedule Variance 2
elif prompt == 'SV2':
	print('Schedule Variance selected')
	EV = float(input(" Enter Earned Value: "))
	PV = float(input(" Enter Planned value: "))
	SV2 = EV - PV
	print('The Schedule Variance is:', SV2)

#Calculate Estimate at Completion
elif prompt == 'EAC':
	print('Estimate at Completion selected')
	AC = float(input(" Enter Actual Cost: "))
	ETC = float(input(" Enter Estimate at Completion: "))
	EAC = AC+ETC
	print('The Estimate at Completion is:',EAC)

#Calculate Estimate at Completion 2
elif prompt == 'EAC2':
	print('Estimate at Completion selected')
	AC = float(input(" Enter Actual Cost: "))
	BAC = float(input(" Enter Budget at Completion "))
	EV = float(input(" Enter Earned Value: "))
	EAC2 = AC + (BAC-EV)
	print('The Estimate at Completion is:',EAC2)

#Calculate Cost Variance
elif prompt == 'CV':
	print('Cost Variance selected')
	EV = float(input(" Enter Earned Value: "))
	AC = float(input(" Enter Actual Cost: "))
	CV = EV - AC
	print('The Cost Variance is:',CV)

#Calculate Planned Value
elif prompt == 'PV':
	print('Planned value selected')
	PC = float(input(" Enter Percent Complete(planned): "))
	TB = float(input(" Enter Task Budget: "))
	PV = PC * TB
	print('The Planned Value is:', PV)

#Calculate Estimated Value
elif prompt == 'EV':
	print('Estimated value selected')
	PC = float(input(" Enter Percent Complete(actual): "))
	TB = float(input(" Enter Task Budget: "))
	PV = PC * TB
	print('The Estimated Value is:', EV)

#Calculate Schedule Performance Index
elif prompt == 'SPI':
	print('Schedule Performance Index selected')
	EV = float(input(" Enter Earned Value: "))
	PV = float(input(" Enter Planned Value: "))
	SPI = EV / PV
	print('Schedule Performance Index:', SPI)

#Display list of supported calculations
elif prompt == 'list':
	print('CPI, CV, EAC, EAC2, EV, PV, SPI, SV, SV2')
		
#Display a message to enter a vailid calculation
else:
	print('Please enter a valid calculation such as CPI, CV, EAC, EAC2, EV, PV, SPI, SV, SV2')

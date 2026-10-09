code 1: caluclate electrical power
voltage = float(input("Enter voltage in volts: "))
current = float(input("Enter current in amperes: "))

power = voltage * current

print("Voltage:", voltage, "V")
print("Current:", current, "A")
print("Electrical Power:", power, "W")


Example output
If you enter voltage as 5 and current as 2, the output will be:
Enter voltage in volts: 5
Enter current in amperes: 2
Voltage: 5.0 V
Current: 2.0 A
Electrical Power: 10.0 W

Code 2 — Frequency Converter

frequency_hz = float(input("Enter frequency in Hz: "))

frequency_khz = frequency_hz / 1000
frequency_mhz = frequency_hz / 1000000

print("Frequency in Hz:", frequency_hz)
print("Frequency in kHz:", frequency_khz)
print("Frequency in MHz:", frequency_mhz)

Example output
Enter frequency in Hz: 5000000
Frequency in Hz: 5000000.0
Frequency in kHz: 5000.0
Frequency in MHz: 5.0

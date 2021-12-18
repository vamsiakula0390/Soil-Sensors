#%%
import time
from pymodbus.client.sync import ModbusSerialClient

client = ModbusSerialClient(method='rtu', port='COM4', timeout=1, stopbits = 1, bytesize = 8,  parity='N', baudrate= 9600)
client.connect()

while True:
    Ph = client.read_holding_registers(address=6, count=1, unit=1);
    M = client.read_holding_registers(address=18, count=1, unit=1);
    T = client.read_holding_registers(address=19, count=1, unit=1);
    E = client.read_holding_registers(address=21, count=1, unit=1);
    N = client.read_holding_registers(address=30, count=1, unit=1);
    print(N)
    P = client.read_holding_registers(address=31, count=1, unit=1);
    print(P)
    K = client.read_holding_registers(address=32, count=1, unit=1);
    print(K)
    print(Ph.registers[0]/100.0);
    time.sleep(0.5)
    print(M.registers[0]/10.0);
    time.sleep(0.5)
    print(T.registers[0]/10.0);
    time.sleep(1)
    print(E.registers[0]);
    time.sleep(0.5)
    print(N.registers[0]);
    time.sleep(0.5)
    print(P.registers[0]);
    time.sleep(0.5)
    print(K.registers[0]);
    time.sleep(2)
    
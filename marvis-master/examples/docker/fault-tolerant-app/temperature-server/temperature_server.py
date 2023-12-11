from multiprocessing import Process, Value
from random import gauss
from socket import socket, AF_INET, SOCK_DGRAM
from struct import pack
from time import sleep


def temperature_change(temperature):
  """
  continuously changes the value ``temperature``

  (Who said emulating reality is hard?)
  """
  while True:
    temperature.value += gauss(0, .1)
    sleep(.1)


def server(temperature):
  """
  serves forever: when receiving 'temp', replies current temperature
  """
  sock = socket(AF_INET, SOCK_DGRAM)
  sock.bind(('0.0.0.0', 4242))

  print('listening')
  while True:
    data, addr = sock.recvfrom(4)
    if data == b'temp':
      sock.sendto(pack('f', temperature.value), addr)


def main():
  temperature = Value('d', 20.0)

  Process(target=temperature_change, args=(temperature, )).start()

  server(temperature)


if __name__ == '__main__':
  main()

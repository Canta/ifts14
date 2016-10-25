# -*- coding: utf-8 -*-

def to_bin_array( numero ):
  if numero < 0:
    raise ValueError('El número debe ser mayor o igual a cero.')
  return list( str( "{0:b}".format(numero) ) )




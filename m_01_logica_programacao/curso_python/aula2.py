# \r\n -> CRLF = windows
# \n -> LF = linux

#isso são argumentos, dentro dos parametros
print(12, 34, 1011, sep="-", end='\r\n')#separador, espaço já vem por padrão
print(56, 78, sep="-", end='#\n')
print(9, 10, sep="-", end='##')# end exibe por último antes de pular a linhas
print(11, 12)


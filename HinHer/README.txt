Como compilar la práctica en la universidad:
1. cd /tmp
2. mkdir st
3. cd st
4. python3 -m venv venv
5. source venv/bin/activate.csh
6. pip3 install streamlit
7. pip3 install antlr4-python3-runtime==4.9.2
8. Ir a la carpeta del compilador
9. antlr4 -Dlanguage=Python3 -no-listener -visitor hm.g4


Como compilar la práctica en casa:
1. Ir a la carpeta del compilador
2. antlr4 -Dlanguage=Python3 -no-listener -visitor hm.g4
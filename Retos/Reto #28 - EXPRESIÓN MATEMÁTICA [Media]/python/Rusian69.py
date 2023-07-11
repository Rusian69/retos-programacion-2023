"""
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
"""
number = ["0","1","2","3","4","5","6","7","8","9", " "]
operation = ["+","-","*","/","%"]
def mat_expretion (expretion:str):
    result = False
    try:
        for index in expretion:
            if index in number or index in operation:
                result = True
            else:
                result = False
                return result
        return result
    except:
        return {"problema": "problema no identificado"}
print (mat_expretion("356 - 4 / 5 / 3"))

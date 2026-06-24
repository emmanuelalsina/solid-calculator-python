
# Importamos las herramientas ABC y abstractmethod de la librería abc.
# ABC nos permite CREAR moldes "incompletos" (clases abstractas) que no se pueden usar directamente,
# abstractmethod es el SELLO que le ponemos a un método para decir:
# "Este método TIENE que existir en cualquier clase que HEREDE de aquí, y cada clase 
# hija está obligada a borrar el 'pass' y escribir su propia lógica matemática".
from abc import ABC, abstractmethod

# Esta es la clase PADRE, CREA la estructura general (interfaz) mínima que toda operación debe tener.
# Hereda de ABC para convertirse en una clase abstracta (meramente sintaxis), es decir, un contrato que otros deben cumplir.
#
# 🔍 PARADIGMA: CLASE PADRE NORMAL vs. CLASE ABSTRACTA (ABC)
# En una clase padre normal, el padre ya sabe hacer cosas y los hijos solo heredan o cambian lo que quieren.
# Aquí, al usar ABC, el padre NO sabe calcular nada. Su único propósito en la vida es estructurar a los hijos.
# Por eso está PROHIBIDO hacer 'Operacion()' directamente (Python te lanzará un error si lo intentas).
# Obligatoriamente tienes que usar las clases hijas como Suma, Resta, etc., para que el código tenga sentido.
class Operacion(ABC):
    
    # 📝 EL CONTRATO OBLIGATORIO (A diferencia de la herencia normal)
    # En un padre normal, los métodos se heredan de forma opcional. Aquí, con '@abstractmethod',
    # obligamos a que CUALQUIER clase hija borre el 'pass' y escriba su propia lógica matemática.
    # Si creas una operación nueva y olvidas ponerle este método 'ejecutar', el programa se romperá.
    @abstractmethod
    
    #una clase abstracta es el cascarón , la idea, no el código en si.
    def ejecutar(self, num1, num2):
		    #'pass' significa "aquí no hay código, la clase hija es quien lo va a   escribir" Funciona como un marcador de posición temporal para sintaxis obligatoria
        pass

# Cada clase (hija) de aquí en adelante es un experto independiente con una sola responsabilidad.
# Si el jefe de Finanzas pide cambiar cómo se suma, solo tocamos esta clase,
# el resto del sistema ni se entera.
#la clase Suma hereda las reglas de Operacion,por eso se coloca dentro del (), no es parámetro, es sintaxis
#en java seria class Suma extends Operacion
class Suma(Operacion):
   
    # Hereda de Operacion dentro del (), así que está obligada a tener su propio 'ejecutar'.
    # Recibe dos números y regresa únicamente su suma. Nada más, nada menos.
    def ejecutar(self, num1, num2):
        #agregamos el código própio
        return num1 + num2

class Resta(Operacion):
    # Mismo contrato, diferente responsabilidad.
    # Esta clase solo sabe restar, y eso es todo lo que le importa al SRP.
    def ejecutar(self, num1, num2):
        #agregamos el código própio
        return num1 - num2
    
class Multiplicar(Operacion):
    # Mismo contrato, diferente responsabilidad.
    # Esta clase solo sabe multiplicar, y eso es todo lo que le importa al SRP.
    def ejecutar(self, num1, num2):
        #agregamos el código própio
        return num1 * num2    
    

class Dividir(Operacion):

    def ejecutar(self,num1,num2):
        return num1 / num2
    

# Crea la clase Calculadora. Ya no sabe hacer matemáticas, ahora es solo una coordinadora:
# Su única responsabilidad es saber a quién llamar, no cómo hacer el cálculo.
class Calculadora:
    
    #Imagina que es la fábrica de nacimiento del objeto. 
    #Python te obliga a ponerlo porque todo lo que escribas dentro del __init__ se va a crear en el mismísimo segundo en que crees una calculadora en tu code. 
    #Es lo primero que se ejecuta de forma automática para darle vida al objeto.
    def __init__(self):
    
	    #Cuando nace una calculadora nueva, se le pega en el cuerpo un archivador vacío llamado 'operaciones' (es un diccionario).
      # Aquí se van a guardar los expertos (Suma, Resta,etc.)guardando los otros metodos en pares clave-valor, en este caso seria , 'nombre' y método().
      # self. es necesario para que ese archivador quede pegado al cuerpo de esta calculadora y cualquier otro método pueda abrirlo después.
      #Si tú escribieras solo operaciones = {} (sin el self.) esa variable sería temporal. 
      # Nacería dentro del __init__ y moriría en cuanto el __init__ termine de ejecutarse.
        self.operaciones = {}

    # Este método es la puerta para contratar expertos (métodos) y meterlos al archivador (diccionario),RECIBE 3 COSAS:
     #self (para poder llegar al archivador que tiene pegado en el cuerpo
    # 'nombre' es la etiqueta (por ejemplo "suma") y 'operacion' es el experto (por ejemplo Suma()).
    # Sin este método, el archivador siempre estaría vacío y la calculadora no sabría a quién llamar.
    def registrar_operacion(self, nombre, operacion):
        
        
        # Abre el archivador (diccionario) usando self. para llegar a él desde este método
        # y guarda al experto bajo la etiqueta que recibió.
        #En los diccionarios, los corchetes [] sirven para crear o modificar un par clave-valor:
        #[nombre]: "Crea una etiqueta con el texto que venga en la variable nombre (por ejemplo, "suma")
        # = operacion y asígnale (guarda) al experto que venga en la variable
        #es decir el método() 
        #ejemplo :{"suma": Suma()}
        self.operaciones[nombre] = operacion

		#Este método se llama calcular y RECIBE 3 COSAS: el nombre de lo que            queremos hacer (ej. "suma"), 
		#y los dos números con los que operará el experto (num1, num2).
    def calcular(self, nombre_operacion, num1, num2):
        
        # Antes de buscar al experto, revisa si esa operación fue registrada alguna vez.
        # Si alguien pide "potencia" y nunca la registramos, es mejor avisarle con un error claro que regresar un resultado silencioso e incorrecto.
        #Cuando usas in o not in directamente sobre un diccionario en Python, 
        #Python es inteligente y busca únicamente entre las llaves (las etiquetas), ignorando los valores (los métodos) 
        # Va al archivador y revisa rápido las pestañas de las carpetas.
        if nombre_operacion not in self.operaciones:
        
		        # raise frena el juego en seco con un error limpio y un mensaje en español que tú mismo controlas
            raise ValueError("Esa operación no la conozco")

       # Abre el archivador y saca al experto que corresponde según la etiqueta.
       #Aquí volvemos a usar la sintaxis de corchetes [], pero como esta vez no hay un signo de (=) a la derecha,
       #  Python sabe que no estamos guardando nada, sino extrayendo un valor.
       # Lo guarda en una variable temporal para poder hablarle en la siguiente línea.
        operacion = self.operaciones[nombre_operacion]
        
        # ¡AQUÍ OCURRE LA MAGIA! 
        #La clase padre (Operacion) tiene el método ejecutar totalmente vacío (con un pass), como un cascarón, pero se debe reescribir 
        #Le dice al experto de la clase hija que ejecute SU versión del método.
        # Tras bambalinas es como escribir: Suma().ejecutar(num1, num2)
        #En la programación, cuando la clase hija escribe su propia versión de la función, reemplaza por completo a la del padre. 
        #  el código real que se va a ejecutar es el de la hija.
        # La calculadora no sabe sumar, solo le pide al objeto que sacó del archivador que haga su chamba. 
        
        return operacion.ejecutar(num1, num2)

# =====================================================================
# FASE FINAL: EL ENSAMBLAJE (Instanciar, Registrar y Usar)
# =====================================================================
#1. Creamos la calculadora coordinadora. Su archivador arranca vacío. ({})
#Aqui pasa lo de __init__ creando el archivador(diccionario) en cuanto se ejecutcalculadora = Calculadora()
calculadora = Calculadora()

# 2. Contratamos a cada experto (instanciamos las clases hijas) 
# y los metemos al archivador bajo su respectiva etiqueta clave-valor.
# A partir de este momento la calculadora sabe a quién delegar la chamba.
calculadora.registrar_operacion("suma", Suma())
calculadora.registrar_operacion("resta", Resta())
calculadora.registrar_operacion("multiplicación", Multiplicar())
calculadora.registrar_operacion("división",Dividir())

# ---------------------------------------------------------------------
# NOTA MENTAL PARA AGREGAR NUEVAS OPERACIONES (Ej. Multiplicar/Dividir):

# Si mañana quiero que mi calculadora multiplique, los pasos son 3:

#   Paso A: Creo la clase hija 'Multiplicacion(Operacion)' arriba.
#   Paso B: Sobrescribo su método 'ejecutar(num1, num2)' con la lógica real (num1 * num2).
#   Paso C: La registro aquí abajo: calculadora.registrar_operacion("multi", Multiplicacion())
# ¡Y listo! La clase Calculadora JAMÁS se vuelve a modificar por dentro.
# ---------------------------------------------------------------------

# 3. Ponemos a trabajar a la coordinadora.
# Ella no sabe matemáticas, pero buscará en su archivador la etiqueta "suma",
# sacará al objeto Suma() y le ordenará que ejecute sus números.
print(calculadora.calcular("suma", 5, 3))        # Salida: 8
print(calculadora.calcular("resta", 5, 3))       # Salida: 2
print(calculadora.calcular("multiplicación", 5, 3)) 
print(calculadora.calcular("división", 5, 3))       
# =====================================================================
# ⚡ NOTA DESEMPOLVADORA: EL VIAJE DEL DATO EN 'calculadora.calcular("resta", 20, 8)'
# =====================================================================
# En cuanto ejecutas esa línea, pasa lo siguiente en tu Mac:
#
#   1. ¿Seguridad?: El 'if' busca la palabra "resta" en las pestañas del diccionario. Como sí existe, te deja pasar.
#   2. ¿Extracción?: La calculadora abre el cajón 'self.operaciones["resta"]', saca al objeto experto 'Resta()'
#      y lo guarda en la variable 'operacion'.
#   3. ¿Delegación?: La línea 'return operacion.ejecutar(20, 8)' se convierte en 'Resta().ejecutar(20, 8)'.
#   4. ¿Cálculo?: Se activa el código matemático real de la clase hija (20 - 8), da 12, y el 'return' lo 
#      escupe hacia afuera para que lo guardes en tu variable 'resultado'.
# =====================================================================        
        
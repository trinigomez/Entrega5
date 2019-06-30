# Entrega 4 grupo 16
##### Integrantes:
* Diego Aguayo
* Solene de Geloes
* Trinidad Gómez
* Felipe Trejo

### Informacion importante

* Para agregar los id a los mensajes, se modifico el archivo messages.json, y el nuervo archivo se encuentra en el directorio de la entrega 4.
* Se agrego un nuevo archivo usuarios.json, para poder obtener informacion de los usuario. Se utilizo la base de datos de la entrega 1.


    
### Consultas GET

  * Para obtener un mensaje segun su id el URL correspondiente es <<'/informacion_mensaje/<int:mid>'>>.
  Donde mid es el id del mensaje deseado

  * Para obtener la informacion de un usuario y todos sus mensajes enviados el URl es <<'/mensaje_usuario/<int:mid>'>>
  Donde mid es el id del usuario

  * Para obtener mensajes intercambiados entre dos usuarios el URL es <<'/intercambio/<int:mid>/<int:mid2>'>>
  Donde mid es el id del usuario1 y mid2 el id del usuario2


### Frases que si o si deben estar:
  * El URL correspondientes a esta pregunta es <<'/mensaje1/<string:texto>')>>.
  Para ingresar las frases requeridas, hay que ingresar despues del "/" cada
  frase SEPARADA POR UN &


### Palabras deseables:
  * EL URl correspondiente a esta pregunta <<'/mensaje2/<string:texto>')>>.
  Para ingresar el texto de palabras deseables hay que ingresar despues del "/"
  cada palabra SEPARADA POR UN ESPACIO.

### Palabras no requeridas:
  * EL URl correspondiente a esta pregunta <<'/mensaje3/<string:texto>')>>.
  Para ingresar las palabras no requeridas, hay que ingresar despues del "/"
  cada palabra SEPARADA POR UN ESPACIO.

### Consulta POST
* EL URL correspondiente a esta consulta es
'/nuevo_msje'. Para ingresar los datos es necesario
que sea en forma de un diccionario con las siguientes llaves:
    * message
    * sender
    * receptant
    * lat
    * long
    * date
* Ejemplo de input en postman:  
  {"message": "hola!", "sender": 1, "receptant": 44, "lat": 22, "long": 23, "date": "2019-12-12"}


## Consulta Delete
* El URL correspondiente a esta consulta es '/eliminar_msje/< int:id >', donde el id
que se entrega en la ruta es el id correspondiente al mensaje
 que se quiere eliminar.

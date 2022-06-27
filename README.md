# Yaku-ET36

Yaku es un proyecto, que plantea la idea de realizar una huerta totalmente automatizada capaz de activar el riego en forma automática en función de la humedad en tierra y la cantidad de luz solar, permitiendo establecer los valores mínimos y máximos aceptables para comenzar el riego. 

A su vez tiene un depósito donde recolecta agua de lluvia para hacer un uso eficiente de este recurso indispensable. Ya que en caso de que el depósito de agua de lluvia se encuentre vacío, el sistema automáticamente empezará a utilizar agua de la red. 
Además cuenta con paneles solares permitiéndole reducir su consumo energético de la red.

Los datos obtenidos por los sensores, son reportados a un servidor en la nube permitiendo un monitoreo del estado actual del sistema y además consultar los valores históricos con el fin de obtener conclusiones sobre el cultivo. Dichos valores, son almacenados en una base de datos utilizando la API que nos ofrece el servicio Rainmaker, que es ofrecido por Espressif, empresa desarrolladora de la placa que utilizamos para el dispositivo.
Cuenta con una página web en la que se puede ver a detalle todo el contenido que abarca el proyecto, y revisar una galería de fotos del progreso de armado y evolución. 

Tiene también, una aplicación de celular (Android), asociada a ESP Rainmaker  en la que se consulta el estado actual o más reciente de cada uno de los sensores que contiene el dispositivo, también se puede ver el historial de los datos recabados de temperaturas, humedad,  mediante consultas por lapsos de tiempo, permite habilitar / deshabilitar el riego de forma manual y establecer nuevas condiciones para el riego.

![Diagrama del funcionamiento del dispositivo de YAKU](https://i.imgur.com/vbk0tUV.jpg)

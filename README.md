# nucleo_Apache-Deploy
Automatización de portada del Núcleo GNU/Linux con Apache

Para usarlo es necesario tener fabric
  apt-get install fabric
O bien desde pip
  pip install fabric

Tiene 3 opciones:
  1. install_apache : Instalará Apache desde sus repositorios
  2. deploy:          Desplegará la página
  3. undo:            Deshacer los cambios, incluso eliminando logs
Ejecutar con:
  fab -H <host> <opcion>
  
  
TODO
  Se deben usar variables en el script.

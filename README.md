# Formulario con Django

## Creamos el ambiente e instalamos Django

Este formulario lo vamos a crear dentro de un ambiente con Django 3.1.7 y procederemos así con la terminal Command Prompt

1. Creamos una carpeta para el proyecto
2. Abrimos la carpeta con visual studio Code y dentro de la terminal de Cmd creamos el ambiente con:
    
    ```python
    python -m venv ambiente
    ```
    
3. Luego pasamos a instalar Django con el comando, dentro de ambiente buscamos la carpeta scripts y ejecutamos activate para activar el entorno virtual
    
    ```python
    pip install Django==3.1.7
    ```
    
4. Luego pasamos a instalar 
    
    ```python
    pip install unipath
    ```
5. clonamos en el directorio Raiz
6. Dentro del proyecto nos aseguramos que podamos visualizar el archivo manage.py al escribir "dir" hacemos la migracion con estos comandos
    Primero : `python [manage.py](http://manage.py/) makemigrations`
    Segundo : `python [manage.py](http://manage.py/) migrate`

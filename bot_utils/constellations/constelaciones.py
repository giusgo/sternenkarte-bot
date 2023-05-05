import re
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go

class Estrella:
    
    def __init__(self, x: float, y: float, id_: str, brillo: float, hid: str, nombre: list = None) -> None:
        
        self.x = x 
        self.y = y
        
        self.id = id_
        self.brillo = brillo 
        self.hid = hid
        
        if nombre is not None:
            
            self.nombre = nombre 
        
        else: 
            
            self.nombre = []
    
    def __str__(self) -> str:
        
        return f"Estrella {self.nombre} ubicada en ({self.x}, {self.y}) con identificador: {self.id}"

class Constelacion: 
    
    def __init__(self, nombre: str) -> None:
        
        self.nodos = []
        self.aristas = {}

        self.nombre = nombre
        
        self.aristas_agregadas = []
    
    def add(self, estrella_1: str, estrella_2: str) -> None: 
        
        if estrella_1 not in self.nodos: 
            
            self.nodos.append(estrella_1)
        
        if estrella_2 not in self.nodos: 
            
            self.nodos.append(estrella_2)
        
        arista = tuple(sorted((estrella_1, estrella_2)))
        
        if arista not in self.aristas_agregadas:
            
            if estrella_1 in self.aristas:
                
                self.aristas[estrella_1].append(estrella_2)
                
            else:
                
                self.aristas[estrella_1] = [estrella_2]
            
            self.aristas_agregadas.append(arista)
    
    def __str__(self) -> str:
        
        nodos_str = "\n".join(["- " + str(nodo) for nodo in self.nodos])
        
        return f"Constelacion {self.nombre} formada por:\n{nodos_str}"

class StarNotFound(Exception):
    
    def __init__(self):
        pass

    def __str__(self):
        return 'La estrella no existe'

def inicializar_estrellas() -> tuple[list[Estrella], dict[str, tuple[str, str]]]:
    
    estrellas = []
    referencias = {}
        
    with open("stars.txt", "r") as f: 
        
        contenido = f.readlines()
        
        for linea in contenido:
            
            componentes = linea.strip().split(" ")
            
            coord_x = float(componentes[0])
            coord_y = float(componentes[1])
            id_ = float(componentes[3])
            brillo = float(componentes[4])
            hid = float(componentes[5])
            
            nombres_match = re.search(r'(?:\b[A-Z]+(?:\s+[A-Z0-9]+)*\b;?\s?)+', linea.strip())
            
            nombre = None
            
            if nombres_match is not None: 
                
                nombre_actual = nombres_match.group()

                if nombre_actual.find(";") != -1:
                    
                    nombre_no_procesado = nombre_actual.split(";")
                    
                    nombre = [estrella.strip() for estrella in nombre_no_procesado]
                
                else:

                    nombre = [nombre_actual]
            
            estrella = Estrella(coord_x, coord_y, id_, brillo, hid, nombre)
            estrellas.append(estrella)
            referencias[id_] = (coord_x, coord_y)
    
    return estrellas, referencias

def buscar_estrella(estrella: str, estrellas: list[Estrella]) -> str:
    
    for estrella_actual in estrellas: 
        
        if estrella in estrella_actual.nombre:
            
            return estrella_actual.id
    
    return "_"

def inicializar_constelaciones(estrellas: list) -> list[Constelacion]: 
    
    archivos = ["Boyero.txt", "Casiopea.txt", "Cazo.txt", "Cygnet.txt", "Geminis.txt", "Hydra.txt", "OsaMayor.txt", "OsaMenor.txt"]
    
    constelaciones = []
    
    for archivo in archivos: 
        
        with open(archivo, "r") as f: 
            
            contenido = f.readlines()

            nombre_constelacion = re.search(r"^[^.]+", archivo).group()
            
            constelacion = Constelacion(nombre_constelacion)
            
            for linea in contenido:
                
                componentes = linea.strip().split(",")
                
                estrella_1 = buscar_estrella(componentes[0], estrellas)
                estrella_2 = buscar_estrella(componentes[1], estrellas)
                
                if estrella_1 == "_" or estrella_2 == "_":
                    
                    raise StarNotFound
                
                constelacion.add(estrella_1, estrella_2)
            
            constelaciones.append(constelacion)
    
    return constelaciones

def graficar(referencias: dict, constelaciones: list = None) -> go.Figure:
    
    fig = go.Figure()

    #marker=dict(size=10, line=dict(width=1, color='white'))

    for estrella, coords in referencias.items():
        
        fig.add_trace(go.Scatter(x=[coords[0]], y=[coords[1]], mode='markers', name=str(estrella)))

    # agregar lineas
    
    if constelaciones is not None:
        
        for constelacion in constelaciones:
            
            for estrella, conexiones in constelacion.aristas.items():
                
                coords_estrella = referencias[estrella]
                
                for conexion in conexiones:
                    
                    coords_conexion = referencias[conexion]
                    
                    fig.add_trace(go.Scatter(x=[coords_estrella[0], coords_conexion[0]], y=[coords_estrella[1], coords_conexion[1]], mode='lines'))


    # establecer el título de la figura y los ejes
    fig.update_layout(
        title={
            'text': "Estrellas",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(color='#f8f8f2', size=20)
        },
        xaxis_title="Coordenada x",
        yaxis_title="Coordenada y",
        xaxis=dict(
            title_font=dict(color='#f8f8f2', size=18),
        ),
        yaxis=dict(
            title_font=dict(color='#f8f8f2', size=18),
        ),
        plot_bgcolor='#030420',
        paper_bgcolor='#030420',
        width=800, 
        height=800,
        legend=dict(
            font=dict(
                color='#f9f7f7'
            )
        )
    )
    fig.show()
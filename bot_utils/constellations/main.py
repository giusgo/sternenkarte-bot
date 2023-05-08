from constelaciones import inicializar_constelaciones, inicializar_estrellas, graficar
import os

def main(peticion: dict) -> bytes:
    
    estrellas, referencias = inicializar_estrellas()
    constelaciones = inicializar_constelaciones(estrellas)
    
    return enviar_peticion(peticion, referencias, constelaciones)
    
def enviar_peticion(peticion: dict, referencias: dict, constelaciones: list) -> bool:
    
    resultado = None 
    imagen = ""
    
    if peticion["req-type"] == "tde":
        
        imagen = "todas_estrellas.png"
        
        resultado = graficar(referencias, None, imagen)
    
    elif peticion["req-type"] == "tdc":
        
        constelacion = [constelaciones[peticion["constelacion"]]]
        
        imagen = f"{constelacion[0].nombre}.png"
        
        resultado = graficar(referencias, constelacion, imagen)
    
    elif peticion["req-type"] == "tddc":
        
        imagen = "todas_constelaciones.png"
        
        resultado = graficar(referencias, constelaciones, imagen)
    
    if resultado is not None and imagen != "" and not os.path.exists(f"bot_utils/constellations/images/{imagen}"):

        with open(f"bot_utils/constellations/images/{imagen}", "wb") as f:
            
            f.write(resultado)
    
    return resultado
from constelaciones import inicializar_constelaciones, inicializar_estrellas, graficar

def main(peticion: dict) -> None:
    
    estrellas, referencias = inicializar_estrellas()
    constelaciones = inicializar_constelaciones(estrellas)
    
    if enviar_peticion(peticion, referencias, constelaciones): print("Excelente")
    else: print("Coja juicio")
    
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
    
    if resultado is not None and imagen != "":

        with open(f"bot_utils/constellations/images/{imagen}", "wb") as f:
            
            f.write(resultado)
            
            return True 
    
    return False
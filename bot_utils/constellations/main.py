from constelaciones import inicializar_constelaciones, inicializar_estrellas, graficar

def main(peticion: dict) -> None:
    
    estrellas, referencias = inicializar_estrellas()
    constelaciones = inicializar_constelaciones(estrellas)
    
    enviar_peticion(peticion, referencias, constelaciones)
    
def enviar_peticion(peticion: dict, referencias: dict, constelaciones: list) -> int:
    
    resultado = None 
    
    if peticion["req-type"] == "tde":
        
        resultado = graficar(referencias)
    
    elif peticion["req-type"] == "tdc":
        
        constelacion = [constelaciones[peticion["constelacion"]]]
        
        resultado = graficar(referencias, constelacion)
    
    elif peticion["req-type"] == "tddc":
        
        resultado = graficar(referencias, constelaciones)
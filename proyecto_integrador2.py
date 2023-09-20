import readchar

def main():
    print("Presiona cualquier tecla para mostrarla. Presiona ↑ para salir.")
    
    while True:
        key = readchar.readkey()
        
        if key == '\x1b':  # El código de flecha es '\x1b' (Escape)
            arrow_key = readchar.readkey()
            if arrow_key == '[':
                direction = readchar.readkey()
                if direction == '\x1b':  # Flecha hacia arriba
                    print("¡Tecla de flecha hacia arriba presionada! Saliendo del programa.")
                    break
            else:
                print(f"Tecla presionada: {key}")
        else:
            print(f"Tecla presionada: {key}")

if __name__ == "__main__":
    main()
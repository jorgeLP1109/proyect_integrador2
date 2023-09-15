import msvcrt

def main():
    print("Presiona cualquier tecla para mostrarla. Presiona ↑ para salir.")
    
    while True:
        key = msvcrt.getch().decode('utf-8')
        
        if key == 'Alt+72':  # El código de flecha es '\x1b' (Escape)
            arrow_key = msvcrt.getch().decode('utf-8')
            if arrow_key == '[':
                direction = msvcrt.getch().decode('utf-8')
                if direction == 'A':  # Flecha hacia arriba
                    print("¡Tecla de flecha hacia arriba presionada! Saliendo del programa.")
                    break
            else:
                print(f"Tecla presionada: {key}")
        else:
            print(f"Tecla presionada: {key}")

if __name__ == "__main__":
    main()

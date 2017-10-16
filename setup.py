from cx_Freeze import setup, Executable

# On appelle la fonction setup



setup(
    name = "couverture",
    version = "1",
    description = "Calcule de la surface d une toiture",
    executables = [Executable("couverture.py")],
)

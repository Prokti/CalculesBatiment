from cx_Freeze import setup, Executable

# On appelle la fonction setup



setup(
    name = "couverture",
    version = "1",
    description = "Votre programme",
    executables = [Executable("couverture.py")],
)

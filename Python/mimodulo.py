{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "73ffe1c8-a0e4-4988-ab26-38474ec3820c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overwriting mimodulo.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile mimodulo.py\n",
    "\n",
    "def saludar(nombre):\n",
    "    return f\"Hola, {nombre}!\"\n",
    "\n",
    "pi = 3.1416\n",
    "\n",
    "class Persona:\n",
    "    def __init__(self, nombre):\n",
    "        self.nombre = nombre\n",
    "\n",
    "    def presentar(self):\n",
    "        return f\"Me llamo {self.nombre}\""
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

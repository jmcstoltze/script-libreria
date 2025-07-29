# 📚 Script-Libreria-Online 

**Solución digital completa** para gestionar catálogos de libros. Convierte datos desde Excel a JSON y muestra el contenido en una interfaz web moderna y responsive.

<div align="center">
  
  ## 🖥️ Vista Desktop
  <img src="screenshots/large-screen.png" alt="Vista escritorio" width="80%">
  <br>
  <hr>
  
  ## 📱 Vistas Móvil | Tablet
  
  <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 20px;">
    <img src="screenshots/pantalla-small.jpg" alt="Vista móvil" width="30%">
    <img src="screenshots/pantalla-small1.jpg" alt="Vista móvil 2" width="30%">
    <br><hr><br>
    <img src="screenshots/pantalla-small2.jpg" alt="Vista móvil 3" width="30%">
    <img src="screenshots/pantalla-mediana1.jpg" alt="Vista tablet 1" width="45%">
    <img src="screenshots/pantalla-mediana2.jpg" alt="Vista tablet 2" width="45%">
  </div>

</div>

---

## 🛠️ Stack Tecnológico

| Área       | Tecnologías                 |
|------------|-----------------------------|
| **Backend**  | Python 3, Pandas            |
| **Frontend** | HTML5, CSS3, JavaScript     |
| **Herramientas** | Git, GitHub Pages       |
| **Formato**  | Excel, JSON                 |

---

## ⚙️ Funcionamiento  

### 1. Estructura del proyecto  
```bash
.
├── README.md
├── assets/
│   ├── data/
│   │   └── biblioteca.json      # Output JSON
│   └── img/
│       └── portadas/           # Book covers
├── css/
│   └── styles.css              # Main styles
├── index.html                  # Entry point
├── js/
│   └── script.js               # Render logic
├── requirements.txt            # Python dependencies
├── screenshots/                # UI previews
└── scripts/
    ├── Proyecto-Biblioteca.xlsx # Source data
    └── excel_to_json.py        # Conversion script
```

### 2. Corazón del proyecto: `script.py`  
El script convierte los datos de Excel a JSON con **Pandas**, limpiando y formateando la información.

<div align="center">
  
  ## 🐍 Script Python - Proceso de Conversión
  
  <div style="display: flex; justify-content: center; gap: 30px; flex-wrap: wrap;">
    <div>
      <img src="screenshots/script-py1.png" alt="Parte 1 del script" width="100%">
      <p><em>Imports y funciones</em></p>
    </div>
    <div>
      <img src="screenshots/script-py2.png" alt="Parte 2 del script" width="100%">
      <p><em>Manejo principal</em></p>
    </div>
  </div>

</div>

### 3. Instalación del proyecto:

1. Clonar repositorio
```bash
git clone git@github.com:jmcstoltze/script-libreria.git
cd script-libreria
```
2. Configurar entorno virtual (recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```
3. Instalar dependencias
```bash
pip install -r requirements.txt
```
4. Ejecutar el script de conversión
```bash
python3 scripts/excel_to_json.py
```
5. Ejecutar el index.html (Recomendado con Live Server)

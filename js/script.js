const container = document.getElementById('librosContainer');

// 1. Función para mostrar errores
function showError(error) {
  console.error('Error completo:', error);
  container.innerHTML = `
    <div class="alert alert-danger">
      <h4>Error al cargar los libros</h4>
      <p>${error.message}</p>
      <p class="small">Ruta intentada: ${new URL('assets/data/biblioteca.json', window.location.href)}</p>
      <p class="small">Asegúrate de:</p>
      <ul class="small">
        <li>Usar un servidor local (Live Server)</li>
        <li>Que el archivo JSON exista en la ruta correcta</li>
        <li>Que no haya errores en el JSON</li>
      </ul>
    </div>
  `;
}

// 2. Función para renderizar libros
function renderBooks(libros) {

  // Ordenar por autor (A-Z) y luego por año de publicación (más reciente primero)
  libros.sort((a, b) => {
    const authorCompare = a.autor.localeCompare(b.autor);
    if (authorCompare !== 0) return authorCompare;
    return b.anioPublicacion - a.anioPublicacion;
  });

  libros.forEach(libro => {
    const portada = libro.portada || 'assets/img/portadas/default.jpg';
    const estadoBadge = `
      <div class="d-flex justify-content-end mb-2">
        <span class="badge ${libro.estado === 'Disponible' ? 'bg-success' : 'bg-secondary'}">${libro.estado}</span>
      </div>
    `;
    
    const col = document.createElement('div');
    col.className = 'col-sm-6 col-md-4 col-lg-3';

    const card = `
      <div class="card h-100 shadow-sm">
        <img src="${portada}" class="portada card-img-top" 
             alt="Portada de ${libro.titulo}"
             onerror="this.src='assets/img/portadas/default.jpg'" style="height: 300px; width: 202px; padding-left: 12%; padding-top:12%;">
        <div class="card-body d-flex flex-column">
          ${estadoBadge}
          <br>
          <div class="d-flex justify-content-between align-items-start">
            <h5 class="card-title">${libro.titulo}</h5>            
          </div>
          <p class="card-text text-muted">${libro.autor}</p>
          <p class="card-text small mb-1">${libro.descripcion}</p>
          <div class="mt-auto d-flex justify-content-between align-items-end">
            <small class="text-muted">${libro.genero.join(', ')}</small>
            <small class="text-secondary">${libro.anioPublicacion}</small>
          </div>
        </div>
      </div>
    `;

    col.innerHTML = card;
    container.appendChild(col);
  });
}

// 3. Cargar los datos
async function loadData() {
  try {
    // Intenta varias rutas posibles
    const possiblePaths = [
      'assets/data/biblioteca.json',
      './assets/data/biblioteca.json',
      '../assets/data/biblioteca.json'
    ];
    
    let response;
    for (const path of possiblePaths) {
      try {
        response = await fetch(path);
        if (response.ok) break;
      } catch (e) {
        console.warn(`Falló la ruta: ${path}`);
      }
    }
    
    if (!response || !response.ok) {
      throw new Error('No se pudo cargar el JSON desde ninguna ruta');
    }
    
    const data = await response.json();
    renderBooks(data.biblioteca.libros);
    
  } catch (error) {
    showError(error);
  }
}

// Iniciar la carga
loadData();
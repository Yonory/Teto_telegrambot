// Загрузка галереи при открытии страницы
window.onload = loadGallery;

async function loadGallery() {
    const gallery = document.getElementById('gallery');
    const counter = document.getElementById('counter');
    
    try {
        // Получаем список всех картинок
        const response = await fetch('/api/images');
        const data = await response.json();
        
        // Обновляем счётчик
        counter.textContent = `Всего изображений: ${data.total}`;
        
        // Очищаем галерею
        gallery.innerHTML = '';
        
        // Добавляем картинки
        data.images.forEach(filename => {
            const item = document.createElement('div');
            item.className = 'gallery-item';
            item.onclick = () => openModal(`/images/${filename}`);
            
            const img = document.createElement('img');
            img.src = `/images/${filename}`;
            img.alt = 'Teto';
            img.loading = 'lazy'; // Ленивая загрузка
            
            item.appendChild(img);
            gallery.appendChild(item);
        });
        
    } catch (error) {
        gallery.innerHTML = '<div class="loading">Ошибка загрузки</div>';
        console.error('Ошибка:', error);
    }
}

async function showRandom() {
    const modal = document.getElementById('modal');
    const modalImg = document.getElementById('modal-img');
    
    // Показываем случайную картинку в модальном окне
    modalImg.src = '/api/random?' + Date.now(); // + timestamp чтобы не кэшировалось
    modal.classList.add('active');
}

function openModal(src) {
    const modal = document.getElementById('modal');
    const modalImg = document.getElementById('modal-img');
    modalImg.src = src;
    modal.classList.add('active');
}

function closeModal() {
    const modal = document.getElementById('modal');
    modal.classList.remove('active');
}

// Закрытие по ESC
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeModal();
    }
});

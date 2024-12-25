window.onload = () => {
    const title = document.querySelector('.title');
    title.style.opacity = 0;
    title.style.transition = 'opacity 2s ease-in-out';
    setTimeout(() => {
        title.style.opacity = 1;
    }, 500);
};


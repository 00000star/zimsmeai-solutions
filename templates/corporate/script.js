
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('[data-mobile-toggle]');
  const links = document.querySelector('.nav-links');
  const actions = document.querySelector('.nav-actions');
  if (toggle && links && actions) {
    toggle.addEventListener('click', () => {
      links.classList.toggle('open');
      actions.classList.toggle('open');
    });
  }
});

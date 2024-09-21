const openButton = document.getElementById('myBtn')
const closeBtn =  document.querySelector('.close')
const modal =  document.querySelector('.bg-modal')

openButton.addEventListener('click', () => {
  modal.style.display ='flex'
},


closeBtn.addEventListener('click', () => {
  modal.style.display ='none'
})
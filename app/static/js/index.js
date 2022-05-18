

//getting DOM

let scrollBtn = document.getElementById("scroll-down")
let wondersContainer = document.getElementById('wonders') 

scrollBtn.onclick = ()=>{
  wondersContainer.scrollIntoView()
}
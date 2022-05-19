

//getting DOM

let scrollBtn = document.getElementById("scroll-down")
let wondersContainer = document.getElementById('wonders') 

scrollBtn.onclick = ()=>{
  wondersContainer.scrollIntoView()
}


//DOM elements


let dateTo = document.getElementById('date');
let displayRes= document.getElementById('nexteventdate');

let dateToValue = new Date(dateTo.value).getTime();


// function countDown(){
  let countDownTime = setInterval(function(){
    let now = new Date().getTime();
    let timeLeft=dateToValue-now;


    let days = Math.floor(timeLeft/(1000*60*60*24));
    let hours = Math.floor((timeLeft%(1000*60*60*24))/(1000*60*60));
    let mins = Math.floor((timeLeft%(1000*60*60))/(1000*60));
    let secs=Math.floor((timeLeft%(1000*60))/1000);


    displayRes.textContent = `${days} days ${hours} hours ${mins} mins ${secs} secs`


    if(timeLeft<0){
      clearInterval(countDownTime)
      displayRes.textContent = `Your event expired. Plan a new one`;
    }

  },1000)
// }


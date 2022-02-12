window.onload=async function(){
    disableScroll()
    await delay(5)
    reverseFlow()
    await delay(2)
    toggleElements()
    titleDelay()
    enableScroll()
    tableauViz()
}

function reverseFlow() {
    document.body.getElementsByTagName('h2')[0].style.opacity = "100%"
    document.body.getElementsByTagName('div')[3].style.animation = "reverse_flow_y 5s linear"
    document.body.getElementsByTagName('div')[4].style.animation = "reverse_flow_x 5s linear"
}

async function toggleElements() {
    document.body.getElementsByTagName('div')[5].style.opacity = "100%"
    document.body.getElementsByTagName('h1')[0].style.opacity = "0%"
    await delay(2)
    document.body.getElementsByTagName('div')[3].style.display = "none"
}

function tableauViz() {
    var divElement = document.getElementById('viz1644620998630');
    var vizElement = divElement.getElementsByTagName('object')[0];
    vizElement.style.width = "96%"
    vizElement.style.height = (divElement.offsetWidth*0.60)+'px'
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
}

function disableScroll() {
    window.onscroll = function() {
        window.scroll(0, 0)
    };
}

async function titleDelay() {
    await delay(1)
    document.body.getElementsByTagName('h1')[0].style.color = "#2a7ebf"
    document.body.getElementsByTagName('h1')[0].style.animation = "fade_in 8s linear"
    document.body.getElementsByTagName('div')[5].style.animation = "fade_out 8s linear"
    await delay(7.9)
    document.body.getElementsByTagName('div')[5].style.opacity = "0%"
    document.body.getElementsByTagName('h1')[0].style.opacity = "100%"
}

function delay(n){
return new Promise(function(resolve){
    setTimeout(resolve,n*1000)
})
}

function enableScroll() {
    window.onscroll = function() {}
}
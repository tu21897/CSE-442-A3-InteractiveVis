/**
* This is the js file that specifies the interaction in index.html.
*/

"use strict";

(function() {
  window.addEventListener("load", init);

  /**
  * Initialize the interative elements once the window is loaded.
  */
  async function init() {
    disableScroll();
    await delay(4.5);
    reverseFlow();
    await delay(1.5);
    showTitle();
    hideElements();
    await delay(3);
    enableScroll();
    tableauViz();
  }

  /**
   * Reverses the water wave animation
   */
  function reverseFlow() {
    qs(".water").style.animation = "reverse_flow_y 4s linear";
    qs(".waves").style.animation = "reverse_flow_x 4s linear";
  }

  /**
   * Displays the header
   */
  async function showTitle() {
    // Hides the header and animate them
    qs("h1").classList.add("hidden");
    qs("h1").style.color = "#2a7ebf";
    qs("h1").style.animation = "fade_in 3.5s ease-in";
    qs("h2.subtitle").classList.add("hidden");
    qs("h2.subtitle").classList.remove("invisible");
    qs("h2.subtitle").style.color = "#2a7ebf";
    qs("h2.subtitle").style.animation = "fade_color 3.5s linear";
    qs("h2.subtitle").style.color = "#bcbbbc";
    // Shows the header again
    qs("h1").classList.remove("hidden");
    qs("h2.subtitle").classList.remove("hidden");
  }

  /**
   * Hides unused elements after animation
   */
  async function hideElements() {
    qs(".scroll").classList.remove("invisible");
    await delay(2.2);
    qs(".water").classList.add("hidden");
    qs(".scroll").style.animation = "fade_out 1.5s linear";
    await delay(1.4);
    qs(".scroll").classList.add("invisible");
  }

  /**
   * Initialize Tableau visualization
   */
  function tableauViz() {
    let vizElement = qs(".tableauViz");
    vizElement.style.height = (id("viz1644620998630").offsetWidth * 0.60) + "px";
    let scriptElement = gen("script");
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
  }

  /**
   * Delay sec seconds
   * @param {number} sec number of seconds to delay
   * @returns a promise that resolved after sec seconds
   */
  function delay(sec) {
    return new Promise((res) => {
      setTimeout(res, sec * 1000);
    });
  }

  /**
   * Disables user's scrolling by fixing it at the top of webpage
   */
  function disableScroll() {
    // Reset to top
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;

    window.onscroll = () => { window.scroll(0, 0) };
  }

  /**
   * Enables user's scrolling activity
   */
  function enableScroll() {
    window.onscroll = () => {};
  }

  /**
  * Returns the element that has the ID attribute with the specified value.
  * @param {string} idName - element ID
  * @returns {object} DOM object associated with id.
  */
  function id(idName) {
    return document.getElementById(idName);
  }

  /**
  * Returns the first element that matches the given CSS selector.
  * @param {string} selector - CSS query selector.
  * @returns {object} The first DOM object matching the query.
  */
  function qs(selector) {
    return document.querySelector(selector);
  }

  /**
  * Returns the array of elements that match the given CSS selector.
  * @param {string} selector - CSS query selector
  * @returns {object[]} array of DOM objects matching the query.
  */
  function qsa(selector) {
    return document.querySelectorAll(selector);
  }

  /**
  * Returns a new element with the given tag name.
  * @param {string} tagName - HTML tag name for new DOM element.
  * @returns {object} New DOM object for given HTML tag.
  */
  function gen(tagName) {
    return document.createElement(tagName);
  }
})();

function displayInfo(evt, tab_y) {
  var i, tabcontent, tablinks;

  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tab_y).style.display = "block";
  evt.currentTarget.className += " active";
}

// someone find a better solution
function displayButton(evt, tab_x) {
  var i, tablinks, tablinks2, tabcontent, designDecisions, developmentProcess;
  tablinks = document.getElementsByClassName("tablinks");
  designDecisions = ['Overview2','Size & Position','Chart Types & Filters','Color & Labels','Axes & Shapes']
  developmentProcess = ['Overview','Data Cleaning','Visualization','Image Processing','HTML/CSS/JS']
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.display = "none";
  }
  tablinks2 = document.getElementsByClassName("tablinks2");
  for (i = 0; i < tablinks2.length; i++) {
    tablinks2[i].className = tablinks2[i].className.replace(" active", "");
  }
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  evt.currentTarget.className += " active";
  if (tab_x == 'Design Decisions') {
    document.getElementById(designDecisions[0]).style.display = "block";
    for (i = 0; i < designDecisions.length; i++) {
      tablinks[i].style.display = "block";
    }
  } else {
    document.getElementById(developmentProcess[0]).style.display = "block";
    for (i = tablinks.length - 1; i > (tablinks.length - 1 - developmentProcess.length); i--) {
      tablinks[i].style.display = "block";
    }
  }
}
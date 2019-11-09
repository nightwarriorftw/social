var scroll = window.requestAnimationFrame || 
                function(callback){
                    window.setTimeout(callback, 1000/60);
                };

/*  Grabing the elements we want to look for
    This will look for all the elements with 
    'show-on-scroll' class and return them as
    as array through which we can iterate  
*/
var elementsToShow = document.querySelectorAll('.show-on-scroll');



/*  isElementInViewPort isn't a JS function
    so we have made our own
*/

function isElementInViewport(element){
    if(typeof jQuery === "function" && element instanceof jQuery){
        element = element[0];
    }

    var rect = element.getBoundingClientRect();
    return (
        (rect.top <=0
            && rect.bottom >=0)
        ||
        (rect.bottom >= (window.innerHeight || document.documentElement.clientHeight) && 
            rect.top <= (window.innerHeight || document.documentElement.clientHeight))
        ||
        (rect.top >=0 &&
            rect.bottom <= (window.innerHeight || document.document.Element.clientHeight))
        
    );
}

// Looping function
function loop(){
    elementsToShow.forEach(function(element){
        if(isElementInViewport(element)){
            element.classList.add('is-visible');
        }
        else{
            element.classList.remove('is-visible');
        }
    });

    scroll(loop);
}

loop();

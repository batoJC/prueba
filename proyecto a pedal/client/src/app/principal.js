document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    M.Modal.init(elems, {});
});

document.addEventListener('domChanged', function() {
    startTooltip();
});


function startTooltip(){
    setTimeout(()=>{
        var elems = document.querySelectorAll('.tooltipped');
        M.Tooltip.init(elems, {});
        // console.log('stared tooltip..');
    },500);
}


function openModal(id){
    var element = document.querySelector('#'+id);
    let instance = M.Modal.getInstance(element);
    instance.open();
}

function closeModal(id){
    var element = document.querySelector('#'+id);
    let instance = M.Modal.getInstance(element);
    instance.close();
}


function editarActive(){
    elements = document.querySelectorAll('.input-field label');
    setTimeout(()=>{
        for (let i = 0; i < elements.length; i++) {
            elements[i].className = "active";
        }
    },300);
    console.log('ppp');
}

function editarDisable(){
    elements = document.querySelectorAll('.input-field label');
    setTimeout(()=>{
        for (let i = 0; i < elements.length; i++) {
            elements[i].className = "";
        }
    },300);
}

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    M.Modal.init(elems, {});
});

document.addEventListener('domChanged', function() {
    startTooltip();
});


function startTooltip(){
    var elems = document.querySelectorAll('.tooltipped');
    M.Tooltip.init(elems, {});
    console.log('stared tooltip..');
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


function reloadEditar(){
    elemento = document.querySelector('#document');
    elemento.focus();
    console.log(elemento);
    // elemento.focus();
    // elemento = document.getElementById('edit_nombre');
    // elemento.focus();
    // elemento = document.getElementById('edit_especie');
    // elemento.focus();
}

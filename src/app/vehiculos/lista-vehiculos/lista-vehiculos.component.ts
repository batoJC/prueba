import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-lista-vehiculos',
  templateUrl: './lista-vehiculos.component.html',
  styleUrls: ['./lista-vehiculos.component.css']
})
export class ListaVehiculosComponent implements OnInit {

  constructor() { }

  listaVehiculos = []

  ngOnInit() {
  }

  agregarVehiculo = (data) => {
    console.log(data);
    console.log('holi2');
    this.listaVehiculos.push(data);
  }

  getData = (placa) => {
    return this.listaVehiculos.find(function(element) {
      return element.id == placa;
    });
  }

  delete = (placa) => {
    this.listaVehiculos.splice(this.getData(placa),1);
  }
  
}

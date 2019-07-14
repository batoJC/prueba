import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-info-vehiculo',
  templateUrl: './info-vehiculo.component.html',
  styleUrls: ['./info-vehiculo.component.css']
})

export class InfoVehiculoComponent implements OnInit {

  @Output() salida = new EventEmitter

  constructor() { }

  vehiculo = {
    placa: 'HGT56',
    tipo_vehiculo: 'Motocicleta',
    marca: 'GATO',
    modelo: 'cupe',
    anyo: '2548',
    tipo_combustible: 'Gasolina',
    nombre_propietario: 'Juan Carlos',
    telefono_propietario: '984456456'
  }

  ngOnInit() {
  }


  load = (data) => {
    console.log('holi3');
    this.vehiculo = data;
  }

  guardar = () => {
    this.vehiculo = {
      placa: '',
      tipo_vehiculo: '',
      marca: '',
      modelo: '',
      anyo: '',
      tipo_combustible: '',
      nombre_propietario: '',
      telefono_propietario: ''
    }
  }

  agregar = () => {
    console.log('holi');
    this.salida.emit(this.vehiculo);
    this.vehiculo = {
      placa: '',
      tipo_vehiculo: '',
      marca: '',
      modelo: '',
      anyo: '',
      tipo_combustible: '',
      nombre_propietario: '',
      telefono_propietario: ''
    }
  }

}

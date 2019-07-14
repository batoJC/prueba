import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class OperationFacturaService {

  constructor() { 
    this.listaServicios =  [
      {
          "id": 1,
          "FechaHora": "28-06-2019 07:54 a.m.",
          "Placa": "NAJ019",
          "Tipo": "Auto",
          "Marca": "Renault",
          "Modelo": "Twingo",
          "Anio": "2006",
          "Combustible": "Gasolina",
          "Propietario": {
              "Codigo": 1,
              "Nombre": "Roberto Melendez",
              "Contacto": "3134567890"
          }
      },
      {
          "id": 2,
          "FechaHora": "28-06-2019 08:13 a.m.",
          "Placa": "DKV581",
          "Tipo": "Auto",
          "Marca": "Renault",
          "Modelo": "Twingo",
          "Anio": "2006",
          "Combustible": "Gasolina",
          "Propietario": {
              "Codigo": 2,
              "Nombre": "María Barreto",
              "Contacto": "3172345123"
          }
      },
      {
          "id": 3,
          "FechaHora": "28-06-2019 08:32 a.m.",
          "Placa": "DKW 81",
          "Tipo": "Moto",
          "Marca": "Yamaha",
          "Modelo": "RX 115",
          "Anio": "2010",
          "Combustible": "Gasolina",
          "Propietario": {
              "Codigo": 3,
              "Nombre": "Pepito Pérez",
              "Contacto": "8781500"
          }
      },
      {
          "id": 4,
          "FechaHora": "28-06-2019 08:40 a.m.",
          "Placa": "HHT 81 A",
          "Tipo": "Moto",
          "Marca": "Suzuki",
          "Modelo": "AX 100",
          "Anio": "2005",
          "Combustible": "Gasolina",
          "Propietario": {
              "Codigo": 4,
              "Nombre": "Simón Bolivar",
              "Contacto": "3002341524"
          }
      },
      {
          "id": 5,
          "FechaHora": "28-06-2019 08:45 a.m.",
          "Placa": "MLS 81 A",
          "Tipo": "Moto",
          "Marca": "Suzuki",
          "Modelo": "BWS",
          "Anio": "2012",
          "Combustible": "Gasolina",
          "Propietario": {
              "Codigo": 4,
              "Nombre": "Claudia Guerrero",
              "Contacto": "3005557772"
          }
      },
      {
          "id": 6,
          "FechaHora": "28-06-2019 08:50 a.m.",
          "Placa": "HHT 81 A",
          "Tipo": "Auto",
          "Marca": "Audi",
          "Modelo": "A5",
          "Anio": "2015",
          "Combustible": "Gasolina",
          "Propietario": {
              "Codigo": 4,
              "Nombre": "Arnoldo Iguarán",
              "Contacto": "3143323345"
          }
      },
      {
          "id": 7,
          "FechaHora": "28-06-2019 08:58 a.m.",
          "Placa": "YTW 23 A",
          "Tipo": "Moto",
          "Marca": "Suzuki",
          "Modelo": "AX 100",
          "Anio": "2010",
          "Combustible": "Gasolina",
          "Propietario": {
              "Codigo": 4,
              "Nombre": "Simón Bolivar",
              "Contacto": "3002341524"
          }
      },
      {
          "id": 8,
          "FechaHora": "28-06-2019 09:03 a.m.",
          "Placa": "HHT 81 A",
          "Tipo": "Moto",
          "Marca": "Suzuki",
          "Modelo": "AX 115",
          "Anio": "2018",
          "Combustible": "Gasolina",
          "Propietario": {
              "Codigo": 4,
              "Nombre": "Mario Jímenez",
              "Contacto": "3002341524"
          }
      },
      {
          "id": 9,
          "FechaHora": "28-06-2019 09:09 a.m.",
          "Placa": "FGD 811",
          "Tipo": "Auto",
          "Marca": "Toyota",
          "Modelo": "Prado",
          "Anio": "2019",
          "Combustible": "ACPM",
          "Propietario": {
              "Codigo": 4,
              "Nombre": "James Rodríguez",
              "Contacto": "3126662226"
          }
      },
      {
          "id": 10,
          "FechaHora": "28-06-2019 09:00 a.m.",
          "Placa": "UER 81 B",
          "Tipo": "Moto",
          "Marca": "Yamaha",
          "Modelo": "DT",
          "Anio": "2002",
          "Combustible": "Gasolina",
          "Propietario": {
              "Codigo": 21,
              "Nombre": "Hernando Hernández",
              "Contacto": "30012312312"
          }
      }
  ];
  }

  listaServicios = []

  getData = () =>{
    return this.listaServicios;  
  }

  getDatos = (id) => {
    return this.listaServicios.find(function(element) {
      return element.id == id;
    });
  }

}

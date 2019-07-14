import { Component, OnInit } from '@angular/core';
import { OperationFacturaService } from '../operation-factura.service';

@Component({
  selector: 'app-lista-fatura',
  templateUrl: './lista-fatura.component.html',
  styleUrls: ['./lista-fatura.component.css']
})
export class ListaFaturaComponent implements OnInit {

  listaFacturas = []

  constructor(private servicioFactura : OperationFacturaService) { }

  ngOnInit() {
    this.listaFacturas = this.servicioFactura.getData();
  }



}

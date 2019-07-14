import { Component, OnInit } from '@angular/core';
import { OperationFacturaService } from '../operation-factura.service';
import { ActivatedRoute, Params } from '@angular/router';

@Component({
  selector: 'app-editar-factura',
  templateUrl: './editar-factura.component.html',
  styleUrls: ['./editar-factura.component.css']
})
export class EditarFacturaComponent implements OnInit {

  registro = null;

  constructor(private servicioFactura : OperationFacturaService,private rutaActiva: ActivatedRoute) { }

  ngOnInit() {
    this.registro = this.servicioFactura.getDatos(this.getUrlParameter('id'));
  }

  getUrlParameter = (parameterName: string) => {
      return this.rutaActiva.snapshot.paramMap.get(parameterName);
  }






}

import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { FacturaRoutingModule } from './factura-routing.module';
import { ListaFaturaComponent } from './lista-fatura/lista-fatura.component';
import { EditarFacturaComponent } from './editar-factura/editar-factura.component';

@NgModule({
  declarations: [ListaFaturaComponent, EditarFacturaComponent],
  imports: [
    CommonModule,
    FormsModule
  ],
  exports: [
    ListaFaturaComponent,
    EditarFacturaComponent
  ]
})
export class FacturaModule { }

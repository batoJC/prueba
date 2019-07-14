import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { ListaVehiculosComponent } from './lista-vehiculos/lista-vehiculos.component';
import { InfoVehiculoComponent } from './info-vehiculo/info-vehiculo.component';

@NgModule({
  declarations: [ListaVehiculosComponent, InfoVehiculoComponent],
  imports: [
    CommonModule,
    FormsModule
  ],
  exports: [
    ListaVehiculosComponent
  ]
})
export class VehiculosModule { }

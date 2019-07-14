import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { VehiculosModule } from './vehiculos.module';
import { ListaVehiculosComponent } from './lista-vehiculos/lista-vehiculos.component';

const routes: Routes = [
  {
    path: 'vehiculos',
    component: ListaVehiculosComponent
  }
];

@NgModule({
  imports: [
    RouterModule.forChild(routes),
    VehiculosModule
  ],
  exports: [RouterModule]
})
export class VehiculosRoutingModule { }

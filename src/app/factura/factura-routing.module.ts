import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FacturaModule } from './factura.module';
import { ListaFaturaComponent } from './lista-fatura/lista-fatura.component';
import { EditarFacturaComponent } from './editar-factura/editar-factura.component';

const routes: Routes = [
  {
    path: 'facturacion',
    component: ListaFaturaComponent
  },
  {
    path: 'factura/:id',
    component: EditarFacturaComponent
  },
];

@NgModule({
  imports: [
    RouterModule.forChild(routes),
    FacturaModule
  ],
  exports: [RouterModule]
})
export class FacturaRoutingModule { }

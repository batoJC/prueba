import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './general/home/home.component';
import { NotFoundComponent } from './template/not-found/not-found.component';
import { GeneralModule } from './general/general.module';
import { VehiculosRoutingModule } from './vehiculos/vehiculos-routing.module';
import { FacturaRoutingModule } from './factura/factura-routing.module';

const routes: Routes = [
  {
    path: 'home',
    component: HomeComponent
  },
  {
    path: '',
    pathMatch: 'full',
    redirectTo: '/home'
  },
  {
    path: '**',
    component: NotFoundComponent
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
    GeneralModule,
    VehiculosRoutingModule,
    FacturaRoutingModule
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }

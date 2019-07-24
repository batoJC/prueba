import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ClientRoutingModule } from './client/client-routing.module';

const routes: Routes = [];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
    ClientRoutingModule
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }

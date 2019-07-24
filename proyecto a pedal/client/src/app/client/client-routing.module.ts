import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ClientModule } from './client.module';
import { ListComponent } from './list/list.component';

const routes: Routes = [
  {
    path:'clients',
    component: ListComponent
  }
];

@NgModule({
  imports: [
    RouterModule.forChild(routes),
    ClientModule
  ],
  exports: [RouterModule]
})
export class ClientRoutingModule { }

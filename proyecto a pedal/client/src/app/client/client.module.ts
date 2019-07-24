import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';


import { ListComponent } from './list/list.component';
import { DataClientComponent } from './data-client/data-client.component';

@NgModule({
  declarations: [ListComponent, DataClientComponent],
  imports: [
    CommonModule,
    HttpClientModule,
    FormsModule
  ],
  exports: [
    ListComponent
  ]
})
export class ClientModule { }

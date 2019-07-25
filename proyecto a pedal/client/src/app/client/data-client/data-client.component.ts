import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { ClientModel } from 'src/app/models/ClientModel';
import { ClientOperationServiceService } from 'src/app/services/client-operation-service.service';

declare const openModal : any;
declare const closeModal : any;
declare const editarActive : any;
declare const editarDisable : any;

@Component({
  selector: 'app-data-client',
  templateUrl: './data-client.component.html',
  styleUrls: ['./data-client.component.css']
})
export class DataClientComponent implements OnInit {

  // @Output() salida = new EventEmitter();
  @Output() add = new EventEmitter();
  @Output() update = new EventEmitter();
  
  client: ClientModel = {
    _id: null,
    document: null,
    name: null,
    last_name: null,
    cellphone: null,
    address: null
  }
  constructor(private service: ClientOperationServiceService) { }

  ngOnInit() {
  }

  saveProductData(): void {
    if(this.client._id != null){
      console.log(this.client);
      this.service.editClient(this.client).subscribe(client => {
        this.update.emit(this.client);
        this.closeModalAdd();
      });
    }else{
      this.service.saveClient(this.client).subscribe(client => {
        this.add.emit(this.client);
        this.closeModalAdd();
      });
    }
  }

  openModalAdd = () => {
    openModal('addClient');
  }

  closeModalAdd = () => {
    closeModal('addClient');
    this.client = {
      _id: null,
      document: null,
      name: null,
      last_name: null,
      cellphone: null,
      address: null
    }
    editarDisable();
  }

  loadData(data){
    let aux: ClientModel = data;
    this.client = Object.create(aux);
    this.openModalAdd();
    editarActive();
  }


}

import { Component, OnInit } from '@angular/core';
import Swal from'sweetalert2';
import { ClientOperationServiceService } from 'src/app/services/client-operation-service.service';
import { ClientModel } from 'src/app/models/ClientModel';

declare const startTooltip : any;

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {

  listClient: ClientModel[] = [];

  constructor(private service: ClientOperationServiceService) { 
    this.loadClientData();
  }

  ngOnInit() {
    startTooltip();
  }

  loadClientData(): void {
    this.service.loadClient().subscribe(clientList => {
      this.listClient = clientList;
      startTooltip();
    });
  }

  addClient(data){
    this.listClient.push(data);
    startTooltip();
    // Swal.fire('Client added correctly!!');
    Swal.fire(
      'Good Job!',
      'Client added correctly!',
      'success'
    );
  }

  mostrarAlert = () => {
    Swal.fire('Hello world!')
  }

  deleteClient(id){
    Swal.fire({
      title: 'Are you sure?',
      text: 'You will not be able to recover this registry!',
      type: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Yes, delete it!',
      cancelButtonText: 'No, keep it'
    }).then((result) => {
      if (result.value) {
        this.service.deleteClient(id).subscribe(res => {
          if(res){
            Swal.fire(
              'Deleted!',
              'Your registry of client has been deleted.',
              'success'
            ).then(() => {
              this.listClient.splice(this.search(id),1);
            });
          }else{
            Swal.fire('Oops...', 'Something went wrong!', 'error');
          }
        });
      } else if (result.dismiss === Swal.DismissReason.cancel) {
        Swal.fire(
          'Cancelled',
          'Your registry of client is safe :)',
          'error'
        )
      }
    })
  }


  search = (_id) =>{
  	for (var i = 0; i < this.listClient.length; i++) {
  		if (this.listClient[i]._id == _id) {
  			return i;
  		}
  	}
  	return null;
  }

  updateClient(data){
      this.listClient[this.search(data._id)] = data;
      Swal.fire(
        'Good Job!',
        'Client updated correctly!',
        'success'
      );
  }


}

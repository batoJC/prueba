import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { ClientModel } from '../models/ClientModel';
import { Observable } from 'rxjs';

const base_URL = 'http://localhost:3000/api/';



@Injectable({
  providedIn: 'root'
})


export class ClientOperationServiceService {

  constructor(private http: HttpClient) { }

  //save of client
  saveClient(client: ClientModel): Observable<ClientModel> {
    return this.http.post<ClientModel>(`${base_URL}client`,
      client,
      {
        headers: new HttpHeaders({
          'Content-Type':'application/json'
        })
      });
  }


  // list of client
  loadClient(): Observable<ClientModel[]> {
    return this.http.get<ClientModel[]>(`${base_URL}clientList`);
  }

  //edit one client
  editClient(client: ClientModel): Observable<ClientModel> {
    return this.http.put<ClientModel>(`${base_URL}client`,
      {
        _id: client._id,
        name: client.name,
        last_name: client.last_name,
        document: client.document,
        cellphone: client.cellphone,
        address: client.address,
      },
      {
        headers: new HttpHeaders({
          'Content-Type':'application/json'
        })
      });
  }

  //delete one client
  deleteClient(_id): Observable<Boolean> {
    return this.http.delete<Boolean>(`${base_URL}client/${_id}`);
  }

}

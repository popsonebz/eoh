import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Address} from "../model/address.model";

@Injectable()
export class AddressService {
  constructor(private http: HttpClient) { }
  baseUrl: string = 'http://127.0.0.1:5000/api/v1/addresses/';

  getAddresses() {
    return this.http.get<Address[]>(this.baseUrl);
  }

  getAddressById(id: number) {
    return this.http.get<Address>(this.baseUrl + id);
  }

  createAddress(address: Address) {
    return this.http.post(this.baseUrl, address);
  }

  updateAddress(address: Address) {
    return this.http.put(this.baseUrl + address.id, address);
  }

  deleteAddress(id: number) {
    return this.http.delete(this.baseUrl + id);
  }
}
import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";
import {AddressService} from "../service/address.service";
import {Address} from "../model/address.model";

@Component({
  selector: 'app-list-address',
  templateUrl: './list-address.component.html',
  styleUrls: ['./list-address.component.css']
})
export class ListAddressComponent implements OnInit {
  
  addresses: Address[];

  constructor(private router: Router, private addressService: AddressService) { }

  ngOnInit() {
    this.addressService.getAddresses()
      .subscribe( data => {
        this.addresses = data;
      });
  }

  addAddress(): void {
    this.router.navigate(['add-address']);
  };

  deleteAddress(address: Address): void {
    this.addressService.deleteAddress(address.id)
      .subscribe( data => {
        this.addresses = this.addresses.filter(u => u !== address);
      })
  };

  editAddress(address: Address): void {
    localStorage.removeItem("editAddressId");
    localStorage.setItem("editAddressId", address.id.toString());
    this.router.navigate(['edit-address']);
  };

}

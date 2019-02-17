import { Component, OnInit } from '@angular/core';

import {AddressService} from "../service/address.service";
import {Router} from "@angular/router";
import {Address} from "../model/address.model";
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {first} from "rxjs/operators";

@Component({
  selector: 'app-edit-address',
  templateUrl: './edit-address.component.html',
  styleUrls: ['./edit-address.component.css']
})
export class EditAddressComponent implements OnInit {

  address: Address;
  editForm: FormGroup;
  constructor(private formBuilder: FormBuilder,private router: Router, private addressService: AddressService) { }

  ngOnInit() {
    let addressId = localStorage.getItem("editAddressId");
    if(!addressId) {
      alert("Invalid action.")
      this.router.navigate(['list-address']);
      return;
    }
    this.editForm = this.formBuilder.group({
      id: [],
      email: ['', [Validators.required, Validators.pattern(/^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/)]],
      first_name: ['', Validators.required],
      last_name: ['', Validators.required],
      phone_number: ['', Validators.required],
      created_at: [''],
      modified_at: [''],
    });
    this.addressService.getAddressById(+addressId)
      .subscribe( data => {
        this.editForm.setValue(data);
      });
  }

  onSubmit() {
    this.addressService.updateAddress(this.editForm.value)
      .pipe(first())
      .subscribe(
        data => {
          this.router.navigate(['list-address']);
        },
        error => {
          alert(error);
        });
  }
}

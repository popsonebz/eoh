import { Component, OnInit } from '@angular/core';

import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {AddressService} from "../service/address.service";
import {first} from "rxjs/operators";
import {Router} from "@angular/router";

@Component({
  selector: 'app-add-address',
  templateUrl: './add-address.component.html',
  styleUrls: ['./add-address.component.css']
})
export class AddAddressComponent implements OnInit {

  constructor(private formBuilder: FormBuilder,private router: Router, private addressService: AddressService) { }

  addForm: FormGroup;

  ngOnInit() {
    this.addForm = this.formBuilder.group({
      id: [],
      email: ['', [Validators.required, Validators.pattern(/^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/)]],
      first_name: ['', [Validators.required, Validators.pattern(/[A-Za-z]+/)]],
      last_name: ['', [Validators.required, Validators.pattern(/[A-Za-z]+/)]],
      phone_number: ['', [Validators.required, Validators.pattern(/[0-9]+/)]],
    });
  }

  onSubmit() {
    this.addressService.createAddress(this.addForm.value)
      .subscribe( data => {
        this.router.navigate(['list-address']);
      });
  }

}

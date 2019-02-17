import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { AddAddressComponent } from './add-address/add-address.component';
import { EditAddressComponent } from './edit-address/edit-address.component';
import { ListAddressComponent } from './list-address/list-address.component';

import {routing} from "./app.routing";
import {AddressService} from "./service/address.service";

import {ReactiveFormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";

@NgModule({
  declarations: [
    AppComponent,
    AddAddressComponent,
    EditAddressComponent,
    ListAddressComponent
  ],
  imports: [
    BrowserModule,
    routing,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [AddressService],
  bootstrap: [AppComponent]
})
export class AppModule { }

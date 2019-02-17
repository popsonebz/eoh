import { RouterModule, Routes } from '@angular/router';
import {AddAddressComponent} from "./add-address/add-address.component";
import {ListAddressComponent} from "./list-address/list-address.component";
import {EditAddressComponent} from "./edit-address/edit-address.component";

const routes: Routes = [
 { path: 'list-address', component: ListAddressComponent },
  { path: 'add-address', component: AddAddressComponent },
  { path: 'edit-address', component: EditAddressComponent },
  {path : '', redirectTo: '/list-address', pathMatch: 'full'}
];

export const routing = RouterModule.forRoot(routes);
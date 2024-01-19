import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FoodItemChipListComponent } from './components/food-item-chip-list/food-item-chip-list.component';

const routes: Routes = [
  { path: '', component: FoodItemChipListComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FoodItemChipLargeComponent } from './components/food-item-chip-large/food-item-chip-large.component';
import { FoodItemChipListComponent } from './components/food-item-chip-list/food-item-chip-list.component';

@NgModule({
  declarations: [
    AppComponent,
    FoodItemChipLargeComponent,
    FoodItemChipListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

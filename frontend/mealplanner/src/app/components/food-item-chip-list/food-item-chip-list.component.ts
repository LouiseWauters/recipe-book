import { Component, OnInit } from '@angular/core';
import { FOOD } from 'src/app/mock-data/mock-food-items';
import { FoodItem } from 'src/app/models/food-item';

@Component({
  selector: 'app-food-item-chip-list',
  templateUrl: './food-item-chip-list.component.html',
  styleUrls: ['./food-item-chip-list.component.css']
})
export class FoodItemChipListComponent implements OnInit {

  foodItems: FoodItem[] = FOOD;

  constructor() { }

  ngOnInit(): void {
  }

}

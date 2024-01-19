import { Component, Input, OnInit } from '@angular/core';
import { FoodItem } from 'src/app/models/food-item';

@Component({
  selector: 'app-food-item-chip-large',
  templateUrl: './food-item-chip-large.component.html',
  styleUrls: ['./food-item-chip-large.component.css']
})
export class FoodItemChipLargeComponent implements OnInit {

  @Input() foodItem: FoodItem = {
    name: 'Spaghetti Bolognaise',
    id: 12,
    pic_path: 'https://img.hellofresh.com/c_fit,f_auto,fl_lossy,h_500,q_30,w_1024/hellofresh_s3/image/HF221017_R11_W47_NL_Q6114-1_MB_Main_low-b12bd184.jpg',
    plan: false
  }
  showOverlay = false;

  constructor() { }

  ngOnInit(): void {
  }

}

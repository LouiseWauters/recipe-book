import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FoodItemChipListComponent } from './food-item-chip-list.component';

describe('FoodItemChipListComponent', () => {
  let component: FoodItemChipListComponent;
  let fixture: ComponentFixture<FoodItemChipListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FoodItemChipListComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FoodItemChipListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

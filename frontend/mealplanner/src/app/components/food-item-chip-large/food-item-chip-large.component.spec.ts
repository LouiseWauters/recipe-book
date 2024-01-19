import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FoodItemChipLargeComponent } from './food-item-chip-large.component';

describe('FoodItemChipLargeComponent', () => {
  let component: FoodItemChipLargeComponent;
  let fixture: ComponentFixture<FoodItemChipLargeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FoodItemChipLargeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FoodItemChipLargeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

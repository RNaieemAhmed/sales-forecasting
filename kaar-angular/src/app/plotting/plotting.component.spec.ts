import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlottingComponent } from './plotting.component';

describe('PlottingComponent', () => {
  let component: PlottingComponent;
  let fixture: ComponentFixture<PlottingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PlottingComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PlottingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListaFaturaComponent } from './lista-fatura.component';

describe('ListaFaturaComponent', () => {
  let component: ListaFaturaComponent;
  let fixture: ComponentFixture<ListaFaturaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListaFaturaComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListaFaturaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

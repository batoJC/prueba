import { TestBed } from '@angular/core/testing';

import { OperationFacturaService } from './operation-factura.service';

describe('OperationFacturaService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: OperationFacturaService = TestBed.get(OperationFacturaService);
    expect(service).toBeTruthy();
  });
});

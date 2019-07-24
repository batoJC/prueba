import { TestBed } from '@angular/core/testing';

import { ClientOperationServiceService } from './client-operation-service.service';

describe('ClientOperationServiceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ClientOperationServiceService = TestBed.get(ClientOperationServiceService);
    expect(service).toBeTruthy();
  });
});

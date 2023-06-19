import { TestBed } from '@angular/core/testing';

import { IdserviceService } from './idservice.service';

describe('IdserviceService', () => {
  let service: IdserviceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(IdserviceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

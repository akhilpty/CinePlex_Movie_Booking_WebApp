import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class IdserviceService {


  private id:string
  setId(id: string) {
    this.id = id;
  }

  getId(): string {
    return this.id;
  }
  constructor() { }
}

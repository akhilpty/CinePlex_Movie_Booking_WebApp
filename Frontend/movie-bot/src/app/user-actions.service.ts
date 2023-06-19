import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class UserActionsService {
  GetBookin(token: string) {
    throw new Error('Method not implemented.');
  }


  private movieapiUrl = "http://127.0.0.1:8000/userapi/"
  private httpOption = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };
  
  constructor(private http:HttpClient,private router:Router) { }

  Listmovie(token: any): Observable<any> {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `token ${token}`
      })
    };
  
    return this.http.get(`${this.movieapiUrl}movie-list`, httpOptions);
  }
  Detailmovie(token: any,id:any): Observable<any> {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `token ${token}`
      })
    };
  
    return this.http.get(`${this.movieapiUrl}movie-details/${id}`, httpOptions);
  }
  Bookingmovie(data:any,id:any,token:any): Observable<any> {
      const httpOptions = {
        headers: new HttpHeaders({
          'Content-Type': 'application/json',
          'Authorization': `token ${token}`
        })
      };

    
      return this.http.post(`${this.movieapiUrl}movie-add/${id}`, data,httpOptions);

  }
  Paymentorder(token:any,id:any){
  
    
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `token ${token}`
      })
    };
   
    return this.http.get(`${this.movieapiUrl}new-order/${id}`,httpOptions);
  }
  Callbackorder(data:any ,token:any){
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `token ${token}`
      })
    };
  return this.http.post(`${this.movieapiUrl}callback`,data,httpOptions);

  }
  GetBooking(token:any) : Observable<any> {
    const httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `token ${token}`
    })
  }
 
return this.http.get<any>(`${this.movieapiUrl}my-bookings`,httpOptions);

}
GetPdf(token:any,id:any) : Observable<Blob> {
  console.log(token)
  
  const httpOptions = {
  headers: new HttpHeaders({
   
    'Authorization': `token ${token}`
  }),
  responseType: 'blob' as 'json'
};

return this.http.get<Blob>(`${this.movieapiUrl}ticket-pdf/${id}`,httpOptions);
}

}

import { Injectable, } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';
import { tap } from "rxjs/operators";

@Injectable({
  providedIn: 'root'
})
 

export class AuthService {
  private movieapiUrl = "http://127.0.0.1:8000/userapi/"


  constructor(private http: HttpClient, private route: Router) { }

  Signup(data: any): Observable<any> {
    return this.http.post<any>(`${this.movieapiUrl}register-user`, data)
  }

  login(data: any): Observable<any> {

    return this.http.post<any>(`${this.movieapiUrl}login-user`, data)
      .pipe(
        tap((response: any) => {
          const token = response.Token;
          const userid=response.userid
          
          
          localStorage.setItem("token", token)
         

                  })
      )


  }
  Logout(): Observable<any> {
    const token = localStorage.getItem('token');
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': `token ${token}`
      })
    };
   
      
    return this.http.post<any>(`${this.movieapiUrl}logout-user`, {},httpOptions)
    
}
}

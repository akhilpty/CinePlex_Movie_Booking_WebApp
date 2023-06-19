import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {

  constructor(private authService:AuthService,private router:Router) { }

  ngOnInit(): void {
  }
  Logout(): void {
    this.authService.Logout();
    localStorage.removeItem('token')
    localStorage.removeItem('userid')
    this.router.navigateByUrl("login");
    



}
}

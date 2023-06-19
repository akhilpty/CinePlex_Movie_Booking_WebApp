import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {UserActionsService} from '../user-actions.service'

@Component({
  selector: 'app-home-user',
  templateUrl: './home-user.component.html',
  styleUrls: ['./home-user.component.css']
})
export class HomeUserComponent implements OnInit {
  movies: any;
  constructor(private router:Router,private userService:UserActionsService) { }

  ngOnInit() {
    const token = localStorage.getItem('token');

    if (token == null) {
      this.router.navigateByUrl("login");
    } else {
      this.userService.Listmovie(token).subscribe(response => {
        this.movies = response;
    })
  }

  
}
}

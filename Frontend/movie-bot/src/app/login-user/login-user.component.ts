import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login-user',
  templateUrl: './login-user.component.html',
  styleUrls: ['./login-user.component.css']
})
export class LoginUserComponent implements OnInit {
  loginform = {
    username: '',
    password: ''
  };
  message:any
  
  constructor(private authService:AuthService,private router:Router) { }

  ngOnInit(): void {
  }
  onSubmit() {
    this.authService.login(this.loginform)
        .subscribe(
          data => {
         
         
          this.router.navigateByUrl('');
   
  },
  (error) => {
   this.message=error.message
  })
}
}



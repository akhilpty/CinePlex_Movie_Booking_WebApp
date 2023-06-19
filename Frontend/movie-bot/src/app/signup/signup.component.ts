import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {
  Signupform ={
    username: '',
    email:'',
    password: '',
    conf_password:''
  }
  message:any
  constructor(private authService:AuthService,private router:Router) { }

  ngOnInit(): void {
  }
  onSubmit(){
    this.authService.Signup(this.Signupform)
    .subscribe(
      response => {
        this.message=response.error
        
        this.router.navigateByUrl('login');

})
}
  }


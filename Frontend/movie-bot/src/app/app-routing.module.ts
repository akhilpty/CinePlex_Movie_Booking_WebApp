import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginUserComponent } from './login-user/login-user.component';
import { SignupComponent } from './signup/signup.component';
import { HomeUserComponent } from './home-user/home-user.component';
import { NavComponent } from './nav/nav.component';
import { DetailUserComponent } from './detail-user/detail-user.component';
import { MoviePaymentComponent } from './movie-payment/movie-payment.component';
import { MyBookingsComponent } from './my-bookings/my-bookings.component';



const routes: Routes = [
  {path:'',component:HomeUserComponent},
  {path:'login',component:LoginUserComponent},
  {path:'signup',component:SignupComponent},
  {path:'logout',component:NavComponent},
  {path:'detail/:id',component:DetailUserComponent},
  {path:'movie-payment',component:MoviePaymentComponent},
  {path:'my-bookings',component:MyBookingsComponent},
  {path:'pdf-booking/:id',component:MyBookingsComponent},
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

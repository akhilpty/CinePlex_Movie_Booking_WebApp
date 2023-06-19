import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginUserComponent } from './login-user/login-user.component';
import { SignupComponent } from './signup/signup.component';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HomeUserComponent } from './home-user/home-user.component';
import { NavComponent } from './nav/nav.component';
import { DetailUserComponent } from './detail-user/detail-user.component';
import { SafePipe } from './safe.pipe';
import { MoviePaymentComponent } from './movie-payment/movie-payment.component';
import { MyBookingsComponent } from './my-bookings/my-bookings.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginUserComponent,
    SignupComponent,
    HomeUserComponent,
    NavComponent,
    DetailUserComponent,
    SafePipe,
  
    MoviePaymentComponent,
    MyBookingsComponent,
   
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    CommonModule,
    FormsModule,
   
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

import { Component, OnInit } from '@angular/core';

import { ActivatedRoute, Router } from '@angular/router';
import { UserActionsService } from '../user-actions.service';
import { IdserviceService } from '../idservice.service';
declare var $: any;


interface seatForm {
  seat: string;
  price: number;
  count: number;
  language:string
}

@Component({
  selector: 'app-detailuser',
  templateUrl: './detail-user.component.html',
  styleUrls: ['./detail-user.component.css']
})
export class DetailUserComponent implements OnInit {;
  data: any;
  id: any;
  option:any

  seatForm: seatForm = {
    seat: '',
    price: 0,
    count: 0,
    language:''
  };
  options: any; // Declare options variable
 
  constructor(
    private userop: UserActionsService,
    private router: Router,
    private route: ActivatedRoute,
    private idService:IdserviceService
  ) {}

  ngOnInit(): void {
    const token = localStorage.getItem('token');
    if (token == null) {
      this.router.navigate(['/login']);
    } else {
      this.moviedetail();
    }
  }

  moviedetail(): void {
    const token = localStorage.getItem('token');
    this.id = this.route.snapshot.paramMap.get('id');
    this.userop.Detailmovie(token,this.id).subscribe(response => {
      this.data = response;

      
    });
  }

  openModal(): void {
    $('#myModal').modal('show');
  }

  closeModal(): void {
    $('#myModal').modal('hide');
  }

  updatePrice(): void {
    const seat = this.seatForm.seat;
    if (seat === 'diamond') {
      this.seatForm.price = 300.0;
    } else if (seat === 'gold') {
      this.seatForm.price = 180.0;
    } else if (seat === 'silver') {
      this.seatForm.price = 120.0;
    }
  }

  booking(): void {
    const token = localStorage.getItem('token');
    this.id = this.route.snapshot.paramMap.get('id');
    localStorage.setItem('id',this.id)
    this.idService.setId(this.id);
    this.userop.Bookingmovie(this.seatForm, this.id,token).subscribe(response => {
      

      
    });
    this.closeModal()
    this.router.navigateByUrl("movie-payment")
  }

  
}

import { Component, OnInit } from '@angular/core';
import { UserActionsService } from '../user-actions.service';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { IdserviceService } from '../idservice.service';

declare var Razorpay: any;
@Component({
  selector: 'app-movie-payment',
  templateUrl: './movie-payment.component.html',
  styleUrls: ['./movie-payment.component.css']
})
export class MoviePaymentComponent implements OnInit {
  options: any;
  id: any
  data: any
  resd: any
  dataid:any
  rzp:any
  orderstatusForm = {
    customer_details: "",
    order_id: "",
    payment_id: "",
    payment_signature: "",
  
    


  }
  constructor(private userop: UserActionsService,
    private router: Router,
    private route: ActivatedRoute,
    private idService: IdserviceService
  ) { }

  ngOnInit(): void {
    const componentInstance = this;
    const token = localStorage.getItem('token');
    this.id = localStorage.getItem("id")
    
    this.userop.Paymentorder(token, this.id).subscribe(responses => {
      this.data = responses
      
      this.dataid=this.data.data_id
      const orderid = this.data.order.id;
      
     
      this.options = {
        key: 'rzp_test_A5y00lngBViGdQ',
        name: this.data.movie_name,
        currency: "INR",
        seat: this.data.seat,
        order_id: orderid,
        handler: function (response) {
          this.resd = response
          componentInstance.orderstatusForm.customer_details = componentInstance.dataid
          componentInstance.orderstatusForm.order_id = this.resd.razorpay_order_id
          componentInstance.orderstatusForm.payment_id = this.resd.razorpay_payment_id
          componentInstance.orderstatusForm.payment_signature = this.resd.razorpay_signature
          const token = localStorage.getItem('token');
          
          componentInstance.userop.Callbackorder(componentInstance.orderstatusForm,token).subscribe(response => {
           

          })





        },
        prefill: {
          name: '',
          email: '',
          contact: ''
        },
        notes: {
          address: ''
        },
        theme: {
          color: '#0c238a'
        }
      };

      this.rzp = new Razorpay(this.options);
    
      
  
    });
   
   
   
  }
  paybutton(){
    this.rzp.open();
    localStorage.removeItem('id');
    this.goback()
  }
goback(){
 this.router.navigateByUrl('my-bookings')
}


}



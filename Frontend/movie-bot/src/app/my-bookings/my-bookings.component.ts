import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { UserActionsService } from '../user-actions.service';


@Component({
  selector: 'app-my-bookings',
  templateUrl: './my-bookings.component.html',
  styleUrls: ['./my-bookings.component.css']
})
export class MyBookingsComponent implements OnInit {
  movies :any
  userid:any
  id:any


  constructor(private router:Router,private userService:UserActionsService,private route: ActivatedRoute,) { }

  ngOnInit(): void {
    const token = localStorage.getItem('token');

    if (token == null) {
      this.router.navigateByUrl("login");
    } else {
      this.userService.GetBooking(token).subscribe((response :any) => {
        this.movies = response;
        console.log(this.movies)
        
        
      
  })

  
  }

}
DownloadPdf(): void {

  const token = localStorage.getItem('token');
  this.id = this.route.snapshot.paramMap.get('id');
  
  this.userService.GetPdf(token,this.id).subscribe((response: Blob) => {
      
      const link = document.createElement('a');
      link.href = URL.createObjectURL(response);
      link.download = 'movie_ticket.pdf';
      link.click();
      
     
      URL.revokeObjectURL(link.href);
      
    },
    (error) => {
      console.log('Error downloading PDF:', error);
    }
  );
}
}

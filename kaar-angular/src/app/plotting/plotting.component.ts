import { Component, OnInit } from '@angular/core';
import { Router, RouterLink } from '@angular/router';

@Component({
  selector: 'app-plotting',
  templateUrl: './plotting.component.html',
  styleUrls: ['./plotting.component.css']
})
export class PlottingComponent implements OnInit{

  constructor(private router: Router) {
    
  }

 ngOnInit(): void {

 }

  title = "plottinng";
  myimage:string = "assets/img/plot.png"



  onPrediction(){
    this.router.navigateByUrl('/upload');
  }
}

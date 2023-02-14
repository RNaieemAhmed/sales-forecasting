import { Component, OnInit } from '@angular/core';
import { FileUploadService } from './file-upload.service';
import { Router, RouterLink } from '@angular/router';


@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent implements OnInit {

  // Variable to store shortLink from api response
  message: string = "";
  loading: boolean = false; // Flag variable
  file?: any = null; // Variable to store file
  data: any = null;
  days: any = null;
  myimage:string = "assets/img/plot.png"
  fig: boolean=false;
  // Inject service
  constructor(private fileUploadService: FileUploadService,private router: Router) {
    
   }

  ngOnInit(): void {

  }

  // On file Select
  onChange(event?: any) {
    this.file = event.target.files[0];
  }

  onDayChange(event?: any){
    console.log(event.target.value)
    this.days = event.target.value;
  }

  // OnClick of button Upload
  onUpload() {
    this.loading = !this.loading;
    this.fig=!this.fig;
    console.log(this.file);
    console.log(this.days);
    this.fileUploadService.upload(this.file, this.days).subscribe(
      (event: any) => {
        if (typeof (event) === 'object') {

          // Short link via api response
          this.message = event.message;

          this.data = event.data;

          this.data.map((val:any) => {
            val.prediction = val.prediction.toFixed(3)
            val.date = val.date.slice(0,11)
            return val
          })

          console.log(this.data);

          // Flag variable
          this.loading = false; 
          
        }
      }
    );
  }
  onPlotting(){

    this.router.navigateByUrl('/plotting');
    this.fig = false;
  }
}

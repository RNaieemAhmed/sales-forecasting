import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { FileUploadComponent } from './file-upload/file-upload.component';
import { PlottingComponent } from './plotting/plotting.component';

const routes: Routes = [
  {
    path: "", component: LoginComponent,
  },
  {
    path: "home", component: LoginComponent,
  },
  {
    path: "plotting", component:PlottingComponent,
  },
  {
    path: 'upload', component: FileUploadComponent
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

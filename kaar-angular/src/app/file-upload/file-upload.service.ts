import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
	providedIn: 'root'
})
export class FileUploadService {

	baseApiUrl = "http://localhost:5000"

	constructor(private http: HttpClient) { }

	upload(file?: any, days?: Number): Observable<any> {

		const formData = new FormData();

		formData.append("file", file, file.name);
		formData.append("days", `${days}`)

		return this.http.post(this.baseApiUrl, formData)
	}
}
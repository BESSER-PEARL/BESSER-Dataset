




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class OutPatient  {

    private LocalDate date;
    private String location;
    private None patient;



    public OutPatient(
        LocalDate date,        String location,        None patient    ) {
        this.date = date;
        this.location = location;
        this.patient = patient;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public None getPatient() {
        return patient;
    }

    public void setPatient(None patient) {
        this.patient = patient;
    }


}
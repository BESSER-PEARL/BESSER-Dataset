




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class WaitingList  {

    private None ward_required;
    private None patient;
    private LocalDate date;



    public WaitingList(
        None ward_required,        None patient,        LocalDate date    ) {
        this.ward_required = ward_required;
        this.patient = patient;
        this.date = date;
    }


    public None getWard_required() {
        return ward_required;
    }

    public void setWard_required(None ward_required) {
        this.ward_required = ward_required;
    }
    public None getPatient() {
        return patient;
    }

    public void setPatient(None patient) {
        this.patient = patient;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }


}
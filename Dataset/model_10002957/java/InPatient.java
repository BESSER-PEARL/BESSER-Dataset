




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class InPatient  {

    private int duration;
    private None ward_required;
    private None patient;
    private LocalDate date_place;
    private LocalDate date_actual_leave;
    private None bed;
    private LocalDate date_expected_leave;





    private WaitingList waitinglist;


    public InPatient(
        int duration,        None ward_required,        None patient,        LocalDate date_place,        LocalDate date_actual_leave,        None bed,        LocalDate date_expected_leave    ) {
        this.duration = duration;
        this.ward_required = ward_required;
        this.patient = patient;
        this.date_place = date_place;
        this.date_actual_leave = date_actual_leave;
        this.bed = bed;
        this.date_expected_leave = date_expected_leave;
    }


    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
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
    public LocalDate getDate_place() {
        return date_place;
    }

    public void setDate_place(LocalDate date_place) {
        this.date_place = date_place;
    }
    public LocalDate getDate_actual_leave() {
        return date_actual_leave;
    }

    public void setDate_actual_leave(LocalDate date_actual_leave) {
        this.date_actual_leave = date_actual_leave;
    }
    public None getBed() {
        return bed;
    }

    public void setBed(None bed) {
        this.bed = bed;
    }
    public LocalDate getDate_expected_leave() {
        return date_expected_leave;
    }

    public void setDate_expected_leave(LocalDate date_expected_leave) {
        this.date_expected_leave = date_expected_leave;
    }

    public WaitingList getWaitinglist() {
        return waitinglist;
    }

    public void setWaitinglist(WaitingList waitinglist) {
        this.waitinglist = waitinglist;
    }

}
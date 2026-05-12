




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Appointment  {

    private int num;
    private None doctor;
    private LocalDate date;
    private None patient;
    private String room;





    private WaitingList waitinglist;


    public Appointment(
        int num,        None doctor,        LocalDate date,        None patient,        String room    ) {
        this.num = num;
        this.doctor = doctor;
        this.date = date;
        this.patient = patient;
        this.room = room;
    }


    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }
    public None getDoctor() {
        return doctor;
    }

    public void setDoctor(None doctor) {
        this.doctor = doctor;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public None getPatient() {
        return patient;
    }

    public void setPatient(None patient) {
        this.patient = patient;
    }
    public String getRoom() {
        return room;
    }

    public void setRoom(String room) {
        this.room = room;
    }

    public WaitingList getWaitinglist() {
        return waitinglist;
    }

    public void setWaitinglist(WaitingList waitinglist) {
        this.waitinglist = waitinglist;
    }

}
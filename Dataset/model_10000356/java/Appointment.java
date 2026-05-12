





import java.util.List;
import java.util.ArrayList;

public class Appointment  {

    private String date;
    private String location;
    private int time;





    private Doctor doctor;




    private Patient patient;


    public Appointment(
        String date,        String location,        int time    ) {
        this.date = date;
        this.location = location;
        this.time = time;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }

    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }
    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}
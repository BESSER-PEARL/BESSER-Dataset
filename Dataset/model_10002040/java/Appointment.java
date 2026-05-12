





import java.util.List;
import java.util.ArrayList;

public class Appointment  {

    private int room;
    private String date;
    private String time;
    private String attribute;
    private int doctoradi;
    private String no;





    private Doctor doctor;




    private Patient patient;


    public Appointment(
        int room,        String date,        String time,        String attribute,        int doctoradi,        String no    ) {
        this.room = room;
        this.date = date;
        this.time = time;
        this.attribute = attribute;
        this.doctoradi = doctoradi;
        this.no = no;
    }


    public int getRoom() {
        return room;
    }

    public void setRoom(int room) {
        this.room = room;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public int getDoctoradi() {
        return doctoradi;
    }

    public void setDoctoradi(int doctoradi) {
        this.doctoradi = doctoradi;
    }
    public String getNo() {
        return no;
    }

    public void setNo(String no) {
        this.no = no;
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
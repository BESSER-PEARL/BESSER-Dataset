




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class appointment  {

    private String p_name;
    private int A_no;
    private LocalDate time;
    private String d_name;
    private int p_id;





    private Doctor doctor;




    private Patient patient;


    public appointment(
        String p_name,        int A_no,        LocalDate time,        String d_name,        int p_id    ) {
        this.p_name = p_name;
        this.A_no = A_no;
        this.time = time;
        this.d_name = d_name;
        this.p_id = p_id;
    }


    public String getP_name() {
        return p_name;
    }

    public void setP_name(String p_name) {
        this.p_name = p_name;
    }
    public int getA_no() {
        return A_no;
    }

    public void setA_no(int A_no) {
        this.A_no = A_no;
    }
    public LocalDate getTime() {
        return time;
    }

    public void setTime(LocalDate time) {
        this.time = time;
    }
    public String getD_name() {
        return d_name;
    }

    public void setD_name(String d_name) {
        this.d_name = d_name;
    }
    public int getP_id() {
        return p_id;
    }

    public void setP_id(int p_id) {
        this.p_id = p_id;
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
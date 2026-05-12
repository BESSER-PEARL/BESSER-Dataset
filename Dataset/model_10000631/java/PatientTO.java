




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class PatientTO  {

    private String first_name;
    private String last_name;
    private String password;
    private int plan_id;
    private int state_id;
    private String email;
    private LocalDate date_of_birth;
    private int contact_no;
    private int patient_id;



    public PatientTO(
        String first_name,        String last_name,        String password,        int plan_id,        int state_id,        String email,        LocalDate date_of_birth,        int contact_no,        int patient_id    ) {
        this.first_name = first_name;
        this.last_name = last_name;
        this.password = password;
        this.plan_id = plan_id;
        this.state_id = state_id;
        this.email = email;
        this.date_of_birth = date_of_birth;
        this.contact_no = contact_no;
        this.patient_id = patient_id;
    }


    public String getFirst_name() {
        return first_name;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }
    public String getLast_name() {
        return last_name;
    }

    public void setLast_name(String last_name) {
        this.last_name = last_name;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public int getPlan_id() {
        return plan_id;
    }

    public void setPlan_id(int plan_id) {
        this.plan_id = plan_id;
    }
    public int getState_id() {
        return state_id;
    }

    public void setState_id(int state_id) {
        this.state_id = state_id;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public LocalDate getDate_of_birth() {
        return date_of_birth;
    }

    public void setDate_of_birth(LocalDate date_of_birth) {
        this.date_of_birth = date_of_birth;
    }
    public int getContact_no() {
        return contact_no;
    }

    public void setContact_no(int contact_no) {
        this.contact_no = contact_no;
    }
    public int getPatient_id() {
        return patient_id;
    }

    public void setPatient_id(int patient_id) {
        this.patient_id = patient_id;
    }


}






import java.util.List;
import java.util.ArrayList;

public class Health_Records  {

    private String healthhistory;





    private Patient patient;




    private Doctor doctor;


    public Health_Records(
        String healthhistory    ) {
        this.healthhistory = healthhistory;
    }


    public String getHealthhistory() {
        return healthhistory;
    }

    public void setHealthhistory(String healthhistory) {
        this.healthhistory = healthhistory;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }
    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }

}
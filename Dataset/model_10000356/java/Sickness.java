





import java.util.List;
import java.util.ArrayList;

public class Sickness  {

    private String recommendations;
    private String prescription;
    private String symptoms;





    private Patient patient;


    public Sickness(
        String recommendations,        String prescription,        String symptoms    ) {
        this.recommendations = recommendations;
        this.prescription = prescription;
        this.symptoms = symptoms;
    }


    public String getRecommendations() {
        return recommendations;
    }

    public void setRecommendations(String recommendations) {
        this.recommendations = recommendations;
    }
    public String getPrescription() {
        return prescription;
    }

    public void setPrescription(String prescription) {
        this.prescription = prescription;
    }
    public String getSymptoms() {
        return symptoms;
    }

    public void setSymptoms(String symptoms) {
        this.symptoms = symptoms;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}
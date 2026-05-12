





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String treatment;
    private String patientID;



    public Patient(
        String treatment,        String patientID    ) {
        this.treatment = treatment;
        this.patientID = patientID;
    }


    public String getTreatment() {
        return treatment;
    }

    public void setTreatment(String treatment) {
        this.treatment = treatment;
    }
    public String getPatientid() {
        return patientID;
    }

    public void setPatientid(String patientID) {
        this.patientID = patientID;
    }


}
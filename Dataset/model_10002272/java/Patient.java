





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String patientID;
    private String treatment;



    public Patient(
        String patientID,        String treatment    ) {
        this.patientID = patientID;
        this.treatment = treatment;
    }


    public String getPatientid() {
        return patientID;
    }

    public void setPatientid(String patientID) {
        this.patientID = patientID;
    }
    public String getTreatment() {
        return treatment;
    }

    public void setTreatment(String treatment) {
        this.treatment = treatment;
    }


}






import java.util.List;
import java.util.ArrayList;

public class patient  {

    private String disease;
    private String patient_name;
    private None patient_id;



    public patient(
        String disease,        String patient_name,        None patient_id    ) {
        this.disease = disease;
        this.patient_name = patient_name;
        this.patient_id = patient_id;
    }


    public String getDisease() {
        return disease;
    }

    public void setDisease(String disease) {
        this.disease = disease;
    }
    public String getPatient_name() {
        return patient_name;
    }

    public void setPatient_name(String patient_name) {
        this.patient_name = patient_name;
    }
    public None getPatient_id() {
        return patient_id;
    }

    public void setPatient_id(None patient_id) {
        this.patient_id = patient_id;
    }


}
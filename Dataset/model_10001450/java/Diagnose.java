





import java.util.List;
import java.util.ArrayList;

public class Diagnose  {

    private String symptomps;
    private int diagnoseID;
    private String medication;



    public Diagnose(
        String symptomps,        int diagnoseID,        String medication    ) {
        this.symptomps = symptomps;
        this.diagnoseID = diagnoseID;
        this.medication = medication;
    }


    public String getSymptomps() {
        return symptomps;
    }

    public void setSymptomps(String symptomps) {
        this.symptomps = symptomps;
    }
    public int getDiagnoseid() {
        return diagnoseID;
    }

    public void setDiagnoseid(int diagnoseID) {
        this.diagnoseID = diagnoseID;
    }
    public String getMedication() {
        return medication;
    }

    public void setMedication(String medication) {
        this.medication = medication;
    }


}
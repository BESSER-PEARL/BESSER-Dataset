





import java.util.List;
import java.util.ArrayList;

public class PatientDAO  {






    private PatientBO patientbo;




    private StateDAO1 statedao1;


    public PatientDAO(
    ) {
    }



    public PatientBO getPatientbo() {
        return patientbo;
    }

    public void setPatientbo(PatientBO patientbo) {
        this.patientbo = patientbo;
    }
    public StateDAO1 getStatedao1() {
        return statedao1;
    }

    public void setStatedao1(StateDAO1 statedao1) {
        this.statedao1 = statedao1;
    }

}
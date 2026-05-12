





import java.util.List;
import java.util.ArrayList;

public class PlanDAO  {






    private PatientDAO patientdao;


    public PlanDAO(
    ) {
    }



    public PatientDAO getPatientdao() {
        return patientdao;
    }

    public void setPatientdao(PatientDAO patientdao) {
        this.patientdao = patientdao;
    }

}
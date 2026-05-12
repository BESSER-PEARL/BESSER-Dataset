





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String Admit_date;
    private int Patient_id;
    private String Sickness;



    public Patient(
        String Admit_date,        int Patient_id,        String Sickness    ) {
        this.Admit_date = Admit_date;
        this.Patient_id = Patient_id;
        this.Sickness = Sickness;
    }


    public String getAdmit_date() {
        return Admit_date;
    }

    public void setAdmit_date(String Admit_date) {
        this.Admit_date = Admit_date;
    }
    public int getPatient_id() {
        return Patient_id;
    }

    public void setPatient_id(int Patient_id) {
        this.Patient_id = Patient_id;
    }
    public String getSickness() {
        return Sickness;
    }

    public void setSickness(String Sickness) {
        this.Sickness = Sickness;
    }


}
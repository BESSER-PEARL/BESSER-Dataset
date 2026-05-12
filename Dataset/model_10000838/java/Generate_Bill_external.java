





import java.util.List;
import java.util.ArrayList;

public class Generate_Bill_external  {






    private Receptionist_Actor receptionist_actor;




    private Patient_Actor patient_actor;




    private Accounts_Section_Actor accounts_section_actor;


    public Generate_Bill_external(
    ) {
    }



    public Receptionist_Actor getReceptionist_actor() {
        return receptionist_actor;
    }

    public void setReceptionist_actor(Receptionist_Actor receptionist_actor) {
        this.receptionist_actor = receptionist_actor;
    }
    public Patient_Actor getPatient_actor() {
        return patient_actor;
    }

    public void setPatient_actor(Patient_Actor patient_actor) {
        this.patient_actor = patient_actor;
    }
    public Accounts_Section_Actor getAccounts_section_actor() {
        return accounts_section_actor;
    }

    public void setAccounts_section_actor(Accounts_Section_Actor accounts_section_actor) {
        this.accounts_section_actor = accounts_section_actor;
    }

}
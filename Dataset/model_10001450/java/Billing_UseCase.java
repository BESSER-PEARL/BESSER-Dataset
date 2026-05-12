





import java.util.List;
import java.util.ArrayList;

public class Billing_UseCase  {






    private Nurse_Actor nurse_actor;




    private Patient_Actor patient_actor;


    public Billing_UseCase(
    ) {
    }



    public Nurse_Actor getNurse_actor() {
        return nurse_actor;
    }

    public void setNurse_actor(Nurse_Actor nurse_actor) {
        this.nurse_actor = nurse_actor;
    }
    public Patient_Actor getPatient_actor() {
        return patient_actor;
    }

    public void setPatient_actor(Patient_Actor patient_actor) {
        this.patient_actor = patient_actor;
    }

}
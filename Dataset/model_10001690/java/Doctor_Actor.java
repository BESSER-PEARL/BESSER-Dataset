





import java.util.List;
import java.util.ArrayList;

public class Doctor_Actor  {






    private Give_Prescription_external give_prescription_external;




    private Check_Patient_external check_patient_external;


    public Doctor_Actor(
    ) {
    }



    public Give_Prescription_external getGive_prescription_external() {
        return give_prescription_external;
    }

    public void setGive_prescription_external(Give_Prescription_external give_prescription_external) {
        this.give_prescription_external = give_prescription_external;
    }
    public Check_Patient_external getCheck_patient_external() {
        return check_patient_external;
    }

    public void setCheck_patient_external(Check_Patient_external check_patient_external) {
        this.check_patient_external = check_patient_external;
    }

}
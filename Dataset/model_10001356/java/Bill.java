





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String Patient_Name;
    private String Amount;
    private String Bill_No;





    private Patient patient;




    private Receptionist receptionist;


    public Bill(
        String Patient_Name,        String Amount,        String Bill_No    ) {
        this.Patient_Name = Patient_Name;
        this.Amount = Amount;
        this.Bill_No = Bill_No;
    }


    public String getPatient_name() {
        return Patient_Name;
    }

    public void setPatient_name(String Patient_Name) {
        this.Patient_Name = Patient_Name;
    }
    public String getAmount() {
        return Amount;
    }

    public void setAmount(String Amount) {
        this.Amount = Amount;
    }
    public String getBill_no() {
        return Bill_No;
    }

    public void setBill_no(String Bill_No) {
        this.Bill_No = Bill_No;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }
    public Receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(Receptionist receptionist) {
        this.receptionist = receptionist;
    }

}
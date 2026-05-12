





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String amount;
    private String bill_no;
    private String patient_name;





    private patient patient;




    private receptionist receptionist;


    public Bill(
        String amount,        String bill_no,        String patient_name    ) {
        this.amount = amount;
        this.bill_no = bill_no;
        this.patient_name = patient_name;
    }


    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }
    public String getBill_no() {
        return bill_no;
    }

    public void setBill_no(String bill_no) {
        this.bill_no = bill_no;
    }
    public String getPatient_name() {
        return patient_name;
    }

    public void setPatient_name(String patient_name) {
        this.patient_name = patient_name;
    }

    public patient getPatient() {
        return patient;
    }

    public void setPatient(patient patient) {
        this.patient = patient;
    }
    public receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(receptionist receptionist) {
        this.receptionist = receptionist;
    }

}
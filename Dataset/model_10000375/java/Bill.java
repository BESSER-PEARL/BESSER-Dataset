





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private int Patient_Id;
    private String Amount;
    private String BillNo;





    private Patient patient;




    private Receptionist receptionist;


    public Bill(
        int Patient_Id,        String Amount,        String BillNo    ) {
        this.Patient_Id = Patient_Id;
        this.Amount = Amount;
        this.BillNo = BillNo;
    }


    public int getPatient_id() {
        return Patient_Id;
    }

    public void setPatient_id(int Patient_Id) {
        this.Patient_Id = Patient_Id;
    }
    public String getAmount() {
        return Amount;
    }

    public void setAmount(String Amount) {
        this.Amount = Amount;
    }
    public String getBillno() {
        return BillNo;
    }

    public void setBillno(String BillNo) {
        this.BillNo = BillNo;
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
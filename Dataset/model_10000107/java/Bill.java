





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String BillNo;
    private int Patient_Id;
    private String Amount;





    private Receptionist receptionist;




    private Patient patient;


    public Bill(
        String BillNo,        int Patient_Id,        String Amount    ) {
        this.BillNo = BillNo;
        this.Patient_Id = Patient_Id;
        this.Amount = Amount;
    }


    public String getBillno() {
        return BillNo;
    }

    public void setBillno(String BillNo) {
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

    public Receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(Receptionist receptionist) {
        this.receptionist = receptionist;
    }
    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}
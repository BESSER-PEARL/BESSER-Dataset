





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String BillNo;
    private String Amount;
    private int Patient_Id;





    private Receptionist receptionist;




    private Patient patient;


    public Bill(
        String BillNo,        String Amount,        int Patient_Id    ) {
        this.BillNo = BillNo;
        this.Amount = Amount;
        this.Patient_Id = Patient_Id;
    }


    public String getBillno() {
        return BillNo;
    }

    public void setBillno(String BillNo) {
        this.BillNo = BillNo;
    }
    public String getAmount() {
        return Amount;
    }

    public void setAmount(String Amount) {
        this.Amount = Amount;
    }
    public int getPatient_id() {
        return Patient_Id;
    }

    public void setPatient_id(int Patient_Id) {
        this.Patient_Id = Patient_Id;
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
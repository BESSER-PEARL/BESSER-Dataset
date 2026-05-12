





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String PatientName;
    private int Amount;
    private String BillNo_;





    private Receptionist receptionist;


    public Bill(
        String PatientName,        int Amount,        String BillNo_    ) {
        this.PatientName = PatientName;
        this.Amount = Amount;
        this.BillNo_ = BillNo_;
    }


    public String getPatientname() {
        return PatientName;
    }

    public void setPatientname(String PatientName) {
        this.PatientName = PatientName;
    }
    public int getAmount() {
        return Amount;
    }

    public void setAmount(int Amount) {
        this.Amount = Amount;
    }
    public String getBillno_() {
        return BillNo_;
    }

    public void setBillno_(String BillNo_) {
        this.BillNo_ = BillNo_;
    }

    public Receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(Receptionist receptionist) {
        this.receptionist = receptionist;
    }

}
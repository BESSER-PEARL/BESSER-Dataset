





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String PatientName;
    private None Amount;
    private int BillId;





    private Patient patient;




    private ReceptionList receptionlist;


    public Bill(
        String PatientName,        None Amount,        int BillId    ) {
        this.PatientName = PatientName;
        this.Amount = Amount;
        this.BillId = BillId;
    }


    public String getPatientname() {
        return PatientName;
    }

    public void setPatientname(String PatientName) {
        this.PatientName = PatientName;
    }
    public None getAmount() {
        return Amount;
    }

    public void setAmount(None Amount) {
        this.Amount = Amount;
    }
    public int getBillid() {
        return BillId;
    }

    public void setBillid(int BillId) {
        this.BillId = BillId;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }
    public ReceptionList getReceptionlist() {
        return receptionlist;
    }

    public void setReceptionlist(ReceptionList receptionlist) {
        this.receptionlist = receptionlist;
    }

}
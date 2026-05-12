





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private int BillNo;
    private String patientName;
    private int amount;





    private Patient patient;


    public Bill(
        int BillNo,        String patientName,        int amount    ) {
        this.BillNo = BillNo;
        this.patientName = patientName;
        this.amount = amount;
    }


    public int getBillno() {
        return BillNo;
    }

    public void setBillno(int BillNo) {
        this.BillNo = BillNo;
    }
    public String getPatientname() {
        return patientName;
    }

    public void setPatientname(String patientName) {
        this.patientName = patientName;
    }
    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}
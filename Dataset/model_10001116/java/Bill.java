





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String Amount;
    private String BillNo;
    private String PatientName;





    private Receptionsit receptionsit;




    private Patient patient;


    public Bill(
        String Amount,        String BillNo,        String PatientName    ) {
        this.Amount = Amount;
        this.BillNo = BillNo;
        this.PatientName = PatientName;
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
    public String getPatientname() {
        return PatientName;
    }

    public void setPatientname(String PatientName) {
        this.PatientName = PatientName;
    }

    public Receptionsit getReceptionsit() {
        return receptionsit;
    }

    public void setReceptionsit(Receptionsit receptionsit) {
        this.receptionsit = receptionsit;
    }
    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}
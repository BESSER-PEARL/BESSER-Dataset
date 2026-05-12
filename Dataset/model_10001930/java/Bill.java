





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String BillNo;
    private String PatientName;
    private String Amt;





    private Patient patient;




    private Receptionist receptionist;


    public Bill(
        String BillNo,        String PatientName,        String Amt    ) {
        this.BillNo = BillNo;
        this.PatientName = PatientName;
        this.Amt = Amt;
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
    public String getAmt() {
        return Amt;
    }

    public void setAmt(String Amt) {
        this.Amt = Amt;
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
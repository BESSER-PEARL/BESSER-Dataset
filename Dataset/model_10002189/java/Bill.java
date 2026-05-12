





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String patientname;
    private float amount;
    private String billno;





    private Staff staff;




    private Patient patient;


    public Bill(
        String patientname,        float amount,        String billno    ) {
        this.patientname = patientname;
        this.amount = amount;
        this.billno = billno;
    }


    public String getPatientname() {
        return patientname;
    }

    public void setPatientname(String patientname) {
        this.patientname = patientname;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }
    public String getBillno() {
        return billno;
    }

    public void setBillno(String billno) {
        this.billno = billno;
    }

    public Staff getStaff() {
        return staff;
    }

    public void setStaff(Staff staff) {
        this.staff = staff;
    }
    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}
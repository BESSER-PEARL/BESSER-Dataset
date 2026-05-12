





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String billno;
    private String patientname;
    private float amount;





    private Patient patient;




    private Receptionist receptionist;


    public Bill(
        String billno,        String patientname,        float amount    ) {
        this.billno = billno;
        this.patientname = patientname;
        this.amount = amount;
    }


    public String getBillno() {
        return billno;
    }

    public void setBillno(String billno) {
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
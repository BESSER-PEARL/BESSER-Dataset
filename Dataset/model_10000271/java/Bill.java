





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String billno;
    private float amount;
    private String patientname;





    private Receptionist receptionist;




    private Patient patient;


    public Bill(
        String billno,        float amount,        String patientname    ) {
        this.billno = billno;
        this.amount = amount;
        this.patientname = patientname;
    }


    public String getBillno() {
        return billno;
    }

    public void setBillno(String billno) {
        this.billno = billno;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }
    public String getPatientname() {
        return patientname;
    }

    public void setPatientname(String patientname) {
        this.patientname = patientname;
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
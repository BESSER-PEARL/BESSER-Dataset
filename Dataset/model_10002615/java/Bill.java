





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String billno;
    private float amount;





    private Patient patient;


    public Bill(
        String billno,        float amount    ) {
        this.billno = billno;
        this.amount = amount;
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

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}
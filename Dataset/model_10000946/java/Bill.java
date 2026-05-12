





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private float amount;
    private String billno;
    private String patientname;





    private Receptionist receptionist;


    public Bill(
        float amount,        String billno,        String patientname    ) {
        this.amount = amount;
        this.billno = billno;
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

}
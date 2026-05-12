





import java.util.List;
import java.util.ArrayList;

public class loan  {

    private String patient_name;
    private String amount;





    private billing billing;


    public loan(
        String patient_name,        String amount    ) {
        this.patient_name = patient_name;
        this.amount = amount;
    }


    public String getPatient_name() {
        return patient_name;
    }

    public void setPatient_name(String patient_name) {
        this.patient_name = patient_name;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }

    public billing getBilling() {
        return billing;
    }

    public void setBilling(billing billing) {
        this.billing = billing;
    }

}
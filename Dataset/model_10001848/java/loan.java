





import java.util.List;
import java.util.ArrayList;

public class loan  {

    private String amount;
    private String patient_name;





    private Bill bill;


    public loan(
        String amount,        String patient_name    ) {
        this.amount = amount;
        this.patient_name = patient_name;
    }


    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }
    public String getPatient_name() {
        return patient_name;
    }

    public void setPatient_name(String patient_name) {
        this.patient_name = patient_name;
    }

    public Bill getBill() {
        return bill;
    }

    public void setBill(Bill bill) {
        this.bill = bill;
    }

}
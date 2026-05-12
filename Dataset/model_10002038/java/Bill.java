





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String PatientName;
    private String Amount;



    public Bill(
        String PatientName,        String Amount    ) {
        this.PatientName = PatientName;
        this.Amount = Amount;
    }


    public String getPatientname() {
        return PatientName;
    }

    public void setPatientname(String PatientName) {
        this.PatientName = PatientName;
    }
    public String getAmount() {
        return Amount;
    }

    public void setAmount(String Amount) {
        this.Amount = Amount;
    }


}
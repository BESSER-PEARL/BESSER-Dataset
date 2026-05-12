





import java.util.List;
import java.util.ArrayList;

public class Billing_Report  {

    private String testCharges;
    private String serviceCharges;





    private Receptionist receptionist;


    public Billing_Report(
        String testCharges,        String serviceCharges    ) {
        this.testCharges = testCharges;
        this.serviceCharges = serviceCharges;
    }


    public String getTestcharges() {
        return testCharges;
    }

    public void setTestcharges(String testCharges) {
        this.testCharges = testCharges;
    }
    public String getServicecharges() {
        return serviceCharges;
    }

    public void setServicecharges(String serviceCharges) {
        this.serviceCharges = serviceCharges;
    }

    public Receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(Receptionist receptionist) {
        this.receptionist = receptionist;
    }

}
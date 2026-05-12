





import java.util.List;
import java.util.ArrayList;

public class Appointment  {

    private String Ap_ID;
    private float Time;
    private String E_ID;
    private boolean Confirmation;





    private Customercare customercare;


    public Appointment(
        String Ap_ID,        float Time,        String E_ID,        boolean Confirmation    ) {
        this.Ap_ID = Ap_ID;
        this.Time = Time;
        this.E_ID = E_ID;
        this.Confirmation = Confirmation;
    }


    public String getAp_id() {
        return Ap_ID;
    }

    public void setAp_id(String Ap_ID) {
        this.Ap_ID = Ap_ID;
    }
    public float getTime() {
        return Time;
    }

    public void setTime(float Time) {
        this.Time = Time;
    }
    public String getE_id() {
        return E_ID;
    }

    public void setE_id(String E_ID) {
        this.E_ID = E_ID;
    }
    public boolean getConfirmation() {
        return Confirmation;
    }

    public void setConfirmation(boolean Confirmation) {
        this.Confirmation = Confirmation;
    }

    public Customercare getCustomercare() {
        return customercare;
    }

    public void setCustomercare(Customercare customercare) {
        this.customercare = customercare;
    }

}
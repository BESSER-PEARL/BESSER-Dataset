





import java.util.List;
import java.util.ArrayList;

public class Ward  {

    private int WardNo;
    private String Ward_Type;





    private Patient patient;


    public Ward(
        int WardNo,        String Ward_Type    ) {
        this.WardNo = WardNo;
        this.Ward_Type = Ward_Type;
    }


    public int getWardno() {
        return WardNo;
    }

    public void setWardno(int WardNo) {
        this.WardNo = WardNo;
    }
    public String getWard_type() {
        return Ward_Type;
    }

    public void setWard_type(String Ward_Type) {
        this.Ward_Type = Ward_Type;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Ward  {

    private String Location;
    private int wardNo;





    private Patient patient;


    public Ward(
        String Location,        int wardNo    ) {
        this.Location = Location;
        this.wardNo = wardNo;
    }


    public String getLocation() {
        return Location;
    }

    public void setLocation(String Location) {
        this.Location = Location;
    }
    public int getWardno() {
        return wardNo;
    }

    public void setWardno(int wardNo) {
        this.wardNo = wardNo;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}
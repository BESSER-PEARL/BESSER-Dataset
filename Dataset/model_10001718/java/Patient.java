





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int id;
    private String sickness;
    private String prescriptions;
    private String specialReqs;
    private String allergies;





    private Ward ward;


    public Patient(
        int id,        String sickness,        String prescriptions,        String specialReqs,        String allergies    ) {
        this.id = id;
        this.sickness = sickness;
        this.prescriptions = prescriptions;
        this.specialReqs = specialReqs;
        this.allergies = allergies;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getSickness() {
        return sickness;
    }

    public void setSickness(String sickness) {
        this.sickness = sickness;
    }
    public String getPrescriptions() {
        return prescriptions;
    }

    public void setPrescriptions(String prescriptions) {
        this.prescriptions = prescriptions;
    }
    public String getSpecialreqs() {
        return specialReqs;
    }

    public void setSpecialreqs(String specialReqs) {
        this.specialReqs = specialReqs;
    }
    public String getAllergies() {
        return allergies;
    }

    public void setAllergies(String allergies) {
        this.allergies = allergies;
    }

    public Ward getWard() {
        return ward;
    }

    public void setWard(Ward ward) {
        this.ward = ward;
    }

}
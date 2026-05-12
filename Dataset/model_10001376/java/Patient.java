





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String name;
    private String Prescription;
    private String Allergy;
    private String Sickness;



    public Patient(
        String name,        String Prescription,        String Allergy,        String Sickness    ) {
        this.name = name;
        this.Prescription = Prescription;
        this.Allergy = Allergy;
        this.Sickness = Sickness;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPrescription() {
        return Prescription;
    }

    public void setPrescription(String Prescription) {
        this.Prescription = Prescription;
    }
    public String getAllergy() {
        return Allergy;
    }

    public void setAllergy(String Allergy) {
        this.Allergy = Allergy;
    }
    public String getSickness() {
        return Sickness;
    }

    public void setSickness(String Sickness) {
        this.Sickness = Sickness;
    }


}
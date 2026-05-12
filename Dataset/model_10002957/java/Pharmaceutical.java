





import java.util.List;
import java.util.ArrayList;

public class Pharmaceutical  {

    private String method_of_administration;
    private String dosage;





    private List<Medication> medications;


    public Pharmaceutical(
        String method_of_administration,        String dosage    ) {
        this.method_of_administration = method_of_administration;
        this.dosage = dosage;
        this.medications = new ArrayList<>();
    }

    public Pharmaceutical(
        String method_of_administration,        String dosage        ArrayList<Medication> medications    ) {
        this.method_of_administration = method_of_administration;
        this.dosage = dosage;
        this.medications = medications;
    }

    public String getMethod_of_administration() {
        return method_of_administration;
    }

    public void setMethod_of_administration(String method_of_administration) {
        this.method_of_administration = method_of_administration;
    }
    public String getDosage() {
        return dosage;
    }

    public void setDosage(String dosage) {
        this.dosage = dosage;
    }

    public List<Medication> getMedications() {
        return medications;
    }

    public void addMedication(Medication medication) {
        this.medications.add(medication);
    }

}






import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String MedicalTest;
    private float Height;
    private String Surgeries;
    private String Medicine;
    private float weight;
    private String DiagnosisList;
    private String Allergies;





    private List<Diagnosis> diagnosiss;


    public Patient(
        String MedicalTest,        float Height,        String Surgeries,        String Medicine,        float weight,        String DiagnosisList,        String Allergies    ) {
        this.MedicalTest = MedicalTest;
        this.Height = Height;
        this.Surgeries = Surgeries;
        this.Medicine = Medicine;
        this.weight = weight;
        this.DiagnosisList = DiagnosisList;
        this.Allergies = Allergies;
        this.diagnosiss = new ArrayList<>();
    }

    public Patient(
        String MedicalTest,        float Height,        String Surgeries,        String Medicine,        float weight,        String DiagnosisList,        String Allergies        ArrayList<Diagnosis> diagnosiss    ) {
        this.MedicalTest = MedicalTest;
        this.Height = Height;
        this.Surgeries = Surgeries;
        this.Medicine = Medicine;
        this.weight = weight;
        this.DiagnosisList = DiagnosisList;
        this.Allergies = Allergies;
        this.diagnosiss = diagnosiss;
    }

    public String getMedicaltest() {
        return MedicalTest;
    }

    public void setMedicaltest(String MedicalTest) {
        this.MedicalTest = MedicalTest;
    }
    public float getHeight() {
        return Height;
    }

    public void setHeight(float Height) {
        this.Height = Height;
    }
    public String getSurgeries() {
        return Surgeries;
    }

    public void setSurgeries(String Surgeries) {
        this.Surgeries = Surgeries;
    }
    public String getMedicine() {
        return Medicine;
    }

    public void setMedicine(String Medicine) {
        this.Medicine = Medicine;
    }
    public float getWeight() {
        return weight;
    }

    public void setWeight(float weight) {
        this.weight = weight;
    }
    public String getDiagnosislist() {
        return DiagnosisList;
    }

    public void setDiagnosislist(String DiagnosisList) {
        this.DiagnosisList = DiagnosisList;
    }
    public String getAllergies() {
        return Allergies;
    }

    public void setAllergies(String Allergies) {
        this.Allergies = Allergies;
    }

    public List<Diagnosis> getDiagnosiss() {
        return diagnosiss;
    }

    public void addDiagnosis(Diagnosis diagnosis) {
        this.diagnosiss.add(diagnosis);
    }

}
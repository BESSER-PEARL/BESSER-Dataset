





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private float weight;
    private String Surgeries;
    private float Height;
    private String MedicalTest;
    private String Medicine;
    private String DiagnosisList;
    private String Allergies;





    private List<Diagnosis> diagnosiss;


    public Patient(
        float weight,        String Surgeries,        float Height,        String MedicalTest,        String Medicine,        String DiagnosisList,        String Allergies    ) {
        this.weight = weight;
        this.Surgeries = Surgeries;
        this.Height = Height;
        this.MedicalTest = MedicalTest;
        this.Medicine = Medicine;
        this.DiagnosisList = DiagnosisList;
        this.Allergies = Allergies;
        this.diagnosiss = new ArrayList<>();
    }

    public Patient(
        float weight,        String Surgeries,        float Height,        String MedicalTest,        String Medicine,        String DiagnosisList,        String Allergies        ArrayList<Diagnosis> diagnosiss    ) {
        this.weight = weight;
        this.Surgeries = Surgeries;
        this.Height = Height;
        this.MedicalTest = MedicalTest;
        this.Medicine = Medicine;
        this.DiagnosisList = DiagnosisList;
        this.Allergies = Allergies;
        this.diagnosiss = diagnosiss;
    }

    public float getWeight() {
        return weight;
    }

    public void setWeight(float weight) {
        this.weight = weight;
    }
    public String getSurgeries() {
        return Surgeries;
    }

    public void setSurgeries(String Surgeries) {
        this.Surgeries = Surgeries;
    }
    public float getHeight() {
        return Height;
    }

    public void setHeight(float Height) {
        this.Height = Height;
    }
    public String getMedicaltest() {
        return MedicalTest;
    }

    public void setMedicaltest(String MedicalTest) {
        this.MedicalTest = MedicalTest;
    }
    public String getMedicine() {
        return Medicine;
    }

    public void setMedicine(String Medicine) {
        this.Medicine = Medicine;
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
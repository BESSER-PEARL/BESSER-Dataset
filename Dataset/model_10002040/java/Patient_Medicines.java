





import java.util.List;
import java.util.ArrayList;

public class Patient_Medicines  {

    private String patientno;
    private int no;
    private String medicines;
    private int quantities;





    private Patient patient;




    private List<Patient_Prescription> patient_prescriptions;




    private List<Medicine> medicines;


    public Patient_Medicines(
        String patientno,        int no,        String medicines,        int quantities    ) {
        this.patientno = patientno;
        this.no = no;
        this.medicines = medicines;
        this.quantities = quantities;
        this.patient_prescriptions = new ArrayList<>();
        this.medicines = new ArrayList<>();
    }

    public Patient_Medicines(
        String patientno,        int no,        String medicines,        int quantities        ArrayList<Patient_Prescription> patient_prescriptions,        ArrayList<Medicine> medicines    ) {
        this.patientno = patientno;
        this.no = no;
        this.medicines = medicines;
        this.quantities = quantities;
        this.patient_prescriptions = patient_prescriptions;
        this.medicines = medicines;
    }

    public String getPatientno() {
        return patientno;
    }

    public void setPatientno(String patientno) {
        this.patientno = patientno;
    }
    public int getNo() {
        return no;
    }

    public void setNo(int no) {
        this.no = no;
    }
    public String getMedicines() {
        return medicines;
    }

    public void setMedicines(String medicines) {
        this.medicines = medicines;
    }
    public int getQuantities() {
        return quantities;
    }

    public void setQuantities(int quantities) {
        this.quantities = quantities;
    }

    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }
    public List<Patient_Prescription> getPatient_prescriptions() {
        return patient_prescriptions;
    }

    public void addPatient_prescription(Patient_prescription patient_prescription) {
        this.patient_prescriptions.add(patient_prescription);
    }
    public List<Medicine> getMedicines() {
        return medicines;
    }

    public void addMedicine(Medicine medicine) {
        this.medicines.add(medicine);
    }

}
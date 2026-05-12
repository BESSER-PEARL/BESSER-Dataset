





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String billno;
    private String patientname;
    private float amount;





    private List<Patient> patients;




    private List<Receptionist> receptionists;


    public Bill(
        String billno,        String patientname,        float amount    ) {
        this.billno = billno;
        this.patientname = patientname;
        this.amount = amount;
        this.patients = new ArrayList<>();
        this.receptionists = new ArrayList<>();
    }

    public Bill(
        String billno,        String patientname,        float amount        ArrayList<Patient> patients,        ArrayList<Receptionist> receptionists    ) {
        this.billno = billno;
        this.patientname = patientname;
        this.amount = amount;
        this.patients = patients;
        this.receptionists = receptionists;
    }

    public String getBillno() {
        return billno;
    }

    public void setBillno(String billno) {
        this.billno = billno;
    }
    public String getPatientname() {
        return patientname;
    }

    public void setPatientname(String patientname) {
        this.patientname = patientname;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }

    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }
    public List<Receptionist> getReceptionists() {
        return receptionists;
    }

    public void addReceptionist(Receptionist receptionist) {
        this.receptionists.add(receptionist);
    }

}
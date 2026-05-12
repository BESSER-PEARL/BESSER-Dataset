





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {






    private List<Patient> patients;




    private List<Bill> bills;


    public Receptionist(
    ) {
        this.patients = new ArrayList<>();
        this.bills = new ArrayList<>();
    }

    public Receptionist(
        ArrayList<Patient> patients,        ArrayList<Bill> bills    ) {
        this.patients = patients;
        this.bills = bills;
    }


    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }
    public List<Bill> getBills() {
        return bills;
    }

    public void addBill(Bill bill) {
        this.bills.add(bill);
    }

}
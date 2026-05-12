





import java.util.List;
import java.util.ArrayList;

public class pharmacy  {

    private None price;
    private String medicines;





    private List<patient> patients;


    public pharmacy(
        None price,        String medicines    ) {
        this.price = price;
        this.medicines = medicines;
        this.patients = new ArrayList<>();
    }

    public pharmacy(
        None price,        String medicines        ArrayList<patient> patients    ) {
        this.price = price;
        this.medicines = medicines;
        this.patients = patients;
    }

    public None getPrice() {
        return price;
    }

    public void setPrice(None price) {
        this.price = price;
    }
    public String getMedicines() {
        return medicines;
    }

    public void setMedicines(String medicines) {
        this.medicines = medicines;
    }

    public List<patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}
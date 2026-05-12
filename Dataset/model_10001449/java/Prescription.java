





import java.util.List;
import java.util.ArrayList;

public class Prescription  {

    private String medicines;
    private String tests;





    private List<Doctor> doctors;


    public Prescription(
        String medicines,        String tests    ) {
        this.medicines = medicines;
        this.tests = tests;
        this.doctors = new ArrayList<>();
    }

    public Prescription(
        String medicines,        String tests        ArrayList<Doctor> doctors    ) {
        this.medicines = medicines;
        this.tests = tests;
        this.doctors = doctors;
    }

    public String getMedicines() {
        return medicines;
    }

    public void setMedicines(String medicines) {
        this.medicines = medicines;
    }
    public String getTests() {
        return tests;
    }

    public void setTests(String tests) {
        this.tests = tests;
    }

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}
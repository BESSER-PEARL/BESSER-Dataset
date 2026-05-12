





import java.util.List;
import java.util.ArrayList;

public class Nurse  {

    private int id;
    private String name;
    private int doctorid;





    private List<Doctor> doctors;


    public Nurse(
        int id,        String name,        int doctorid    ) {
        this.id = id;
        this.name = name;
        this.doctorid = doctorid;
        this.doctors = new ArrayList<>();
    }

    public Nurse(
        int id,        String name,        int doctorid        ArrayList<Doctor> doctors    ) {
        this.id = id;
        this.name = name;
        this.doctorid = doctorid;
        this.doctors = doctors;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getDoctorid() {
        return doctorid;
    }

    public void setDoctorid(int doctorid) {
        this.doctorid = doctorid;
    }

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}
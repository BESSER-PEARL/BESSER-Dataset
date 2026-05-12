





import java.util.List;
import java.util.ArrayList;

public class Nurse  {

    private int doctorid;
    private String name;
    private int id;





    private List<Doctor> doctors;


    public Nurse(
        int doctorid,        String name,        int id    ) {
        this.doctorid = doctorid;
        this.name = name;
        this.id = id;
        this.doctors = new ArrayList<>();
    }

    public Nurse(
        int doctorid,        String name,        int id        ArrayList<Doctor> doctors    ) {
        this.doctorid = doctorid;
        this.name = name;
        this.id = id;
        this.doctors = doctors;
    }

    public int getDoctorid() {
        return doctorid;
    }

    public void setDoctorid(int doctorid) {
        this.doctorid = doctorid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}






import java.util.List;
import java.util.ArrayList;

public class Nurse  {

    private int id;
    private int doctorid;
    private String name;





    private List<Doctor> doctors;


    public Nurse(
        int id,        int doctorid,        String name    ) {
        this.id = id;
        this.doctorid = doctorid;
        this.name = name;
        this.doctors = new ArrayList<>();
    }

    public Nurse(
        int id,        int doctorid,        String name        ArrayList<Doctor> doctors    ) {
        this.id = id;
        this.doctorid = doctorid;
        this.name = name;
        this.doctors = doctors;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}
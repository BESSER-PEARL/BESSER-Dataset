





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private String name;
    private int doctorid;
    private int id;





    private List<Doctor> doctors;


    public Department(
        String name,        int doctorid,        int id    ) {
        this.name = name;
        this.doctorid = doctorid;
        this.id = id;
        this.doctors = new ArrayList<>();
    }

    public Department(
        String name,        int doctorid,        int id        ArrayList<Doctor> doctors    ) {
        this.name = name;
        this.doctorid = doctorid;
        this.id = id;
        this.doctors = doctors;
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






import java.util.List;
import java.util.ArrayList;

public class Department  {

    private int doctorid;
    private int id;
    private String name;





    private List<Doctor> doctors;


    public Department(
        int doctorid,        int id,        String name    ) {
        this.doctorid = doctorid;
        this.id = id;
        this.name = name;
        this.doctors = new ArrayList<>();
    }

    public Department(
        int doctorid,        int id,        String name        ArrayList<Doctor> doctors    ) {
        this.doctorid = doctorid;
        this.id = id;
        this.name = name;
        this.doctors = doctors;
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
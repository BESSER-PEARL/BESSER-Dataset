





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private String name;
    private int id;
    private int doctorid;





    private List<Doctor> doctors;


    public Department(
        String name,        int id,        int doctorid    ) {
        this.name = name;
        this.id = id;
        this.doctorid = doctorid;
        this.doctors = new ArrayList<>();
    }

    public Department(
        String name,        int id,        int doctorid        ArrayList<Doctor> doctors    ) {
        this.name = name;
        this.id = id;
        this.doctorid = doctorid;
        this.doctors = doctors;
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
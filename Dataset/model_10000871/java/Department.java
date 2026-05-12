





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private int id;
    private String name;





    private List<Doctor> doctors;


    public Department(
        int id,        String name    ) {
        this.id = id;
        this.name = name;
        this.doctors = new ArrayList<>();
    }

    public Department(
        int id,        String name        ArrayList<Doctor> doctors    ) {
        this.id = id;
        this.name = name;
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

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}
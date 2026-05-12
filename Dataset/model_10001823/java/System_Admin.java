





import java.util.List;
import java.util.ArrayList;

public class System_Admin  {

    private String name;
    private int id;
    private int adminid;





    private List<Doctor> doctors;


    public System_Admin(
        String name,        int id,        int adminid    ) {
        this.name = name;
        this.id = id;
        this.adminid = adminid;
        this.doctors = new ArrayList<>();
    }

    public System_Admin(
        String name,        int id,        int adminid        ArrayList<Doctor> doctors    ) {
        this.name = name;
        this.id = id;
        this.adminid = adminid;
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
    public int getAdminid() {
        return adminid;
    }

    public void setAdminid(int adminid) {
        this.adminid = adminid;
    }

    public List<Doctor> getDoctors() {
        return doctors;
    }

    public void addDoctor(Doctor doctor) {
        this.doctors.add(doctor);
    }

}
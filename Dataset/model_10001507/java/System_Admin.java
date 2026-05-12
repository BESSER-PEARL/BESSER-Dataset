





import java.util.List;
import java.util.ArrayList;

public class System_Admin  {

    private int adminid;
    private int id;
    private String name;





    private List<Doctor> doctors;


    public System_Admin(
        int adminid,        int id,        String name    ) {
        this.adminid = adminid;
        this.id = id;
        this.name = name;
        this.doctors = new ArrayList<>();
    }

    public System_Admin(
        int adminid,        int id,        String name        ArrayList<Doctor> doctors    ) {
        this.adminid = adminid;
        this.id = id;
        this.name = name;
        this.doctors = doctors;
    }

    public int getAdminid() {
        return adminid;
    }

    public void setAdminid(int adminid) {
        this.adminid = adminid;
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
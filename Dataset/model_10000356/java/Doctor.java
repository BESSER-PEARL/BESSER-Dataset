





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String name;
    private int id;
    private String speciality;





    private Staff staff;


    public Doctor(
        String name,        int id,        String speciality    ) {
        this.name = name;
        this.id = id;
        this.speciality = speciality;
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
    public String getSpeciality() {
        return speciality;
    }

    public void setSpeciality(String speciality) {
        this.speciality = speciality;
    }

    public Staff getStaff() {
        return staff;
    }

    public void setStaff(Staff staff) {
        this.staff = staff;
    }

}
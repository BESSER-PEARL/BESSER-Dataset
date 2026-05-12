





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private String Name;
    private int Doctor_ID;
    private int ID;





    private Doctor doctor;


    public Department(
        String Name,        int Doctor_ID,        int ID    ) {
        this.Name = Name;
        this.Doctor_ID = Doctor_ID;
        this.ID = ID;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getDoctor_id() {
        return Doctor_ID;
    }

    public void setDoctor_id(int Doctor_ID) {
        this.Doctor_ID = Doctor_ID;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }

    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }

}
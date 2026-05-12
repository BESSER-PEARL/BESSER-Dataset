





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String Specialization;
    private String Dept;
    private int Doctor_id;



    public Doctor(
        String Specialization,        String Dept,        int Doctor_id    ) {
        this.Specialization = Specialization;
        this.Dept = Dept;
        this.Doctor_id = Doctor_id;
    }


    public String getSpecialization() {
        return Specialization;
    }

    public void setSpecialization(String Specialization) {
        this.Specialization = Specialization;
    }
    public String getDept() {
        return Dept;
    }

    public void setDept(String Dept) {
        this.Dept = Dept;
    }
    public int getDoctor_id() {
        return Doctor_id;
    }

    public void setDoctor_id(int Doctor_id) {
        this.Doctor_id = Doctor_id;
    }


}
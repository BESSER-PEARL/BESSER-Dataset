





import java.util.List;
import java.util.ArrayList;

public class DoctorDatabase  {

    private String doctorName;
    private String Specialization;





    private Receptionist receptionist;


    public DoctorDatabase(
        String doctorName,        String Specialization    ) {
        this.doctorName = doctorName;
        this.Specialization = Specialization;
    }


    public String getDoctorname() {
        return doctorName;
    }

    public void setDoctorname(String doctorName) {
        this.doctorName = doctorName;
    }
    public String getSpecialization() {
        return Specialization;
    }

    public void setSpecialization(String Specialization) {
        this.Specialization = Specialization;
    }

    public Receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(Receptionist receptionist) {
        this.receptionist = receptionist;
    }

}
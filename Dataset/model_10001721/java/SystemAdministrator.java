





import java.util.List;
import java.util.ArrayList;

public class SystemAdministrator  {

    private String Doctors;
    private String Patients;



    public SystemAdministrator(
        String Doctors,        String Patients    ) {
        this.Doctors = Doctors;
        this.Patients = Patients;
    }


    public String getDoctors() {
        return Doctors;
    }

    public void setDoctors(String Doctors) {
        this.Doctors = Doctors;
    }
    public String getPatients() {
        return Patients;
    }

    public void setPatients(String Patients) {
        this.Patients = Patients;
    }


}
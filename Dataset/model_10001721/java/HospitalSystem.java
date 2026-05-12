





import java.util.List;
import java.util.ArrayList;

public class HospitalSystem  {

    private None admin;
    private String Patients;
    private String Doctors;





    private SystemAdministrator systemadministrator;


    public HospitalSystem(
        None admin,        String Patients,        String Doctors    ) {
        this.admin = admin;
        this.Patients = Patients;
        this.Doctors = Doctors;
    }


    public None getAdmin() {
        return admin;
    }

    public void setAdmin(None admin) {
        this.admin = admin;
    }
    public String getPatients() {
        return Patients;
    }

    public void setPatients(String Patients) {
        this.Patients = Patients;
    }
    public String getDoctors() {
        return Doctors;
    }

    public void setDoctors(String Doctors) {
        this.Doctors = Doctors;
    }

    public SystemAdministrator getSystemadministrator() {
        return systemadministrator;
    }

    public void setSystemadministrator(SystemAdministrator systemadministrator) {
        this.systemadministrator = systemadministrator;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Appointment  {

    private String Patient;
    private String Doctor;
    private String Time;





    private Patients patients;




    private Receptionist receptionist;


    public Appointment(
        String Patient,        String Doctor,        String Time    ) {
        this.Patient = Patient;
        this.Doctor = Doctor;
        this.Time = Time;
    }


    public String getPatient() {
        return Patient;
    }

    public void setPatient(String Patient) {
        this.Patient = Patient;
    }
    public String getDoctor() {
        return Doctor;
    }

    public void setDoctor(String Doctor) {
        this.Doctor = Doctor;
    }
    public String getTime() {
        return Time;
    }

    public void setTime(String Time) {
        this.Time = Time;
    }

    public Patients getPatients() {
        return patients;
    }

    public void setPatients(Patients patients) {
        this.patients = patients;
    }
    public Receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(Receptionist receptionist) {
        this.receptionist = receptionist;
    }

}
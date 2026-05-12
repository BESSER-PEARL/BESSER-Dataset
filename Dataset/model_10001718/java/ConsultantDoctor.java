





import java.util.List;
import java.util.ArrayList;

public class ConsultantDoctor  {






    private Team team;




    private List<Patient> patients;


    public ConsultantDoctor(
    ) {
        this.patients = new ArrayList<>();
    }

    public ConsultantDoctor(
        ArrayList<Patient> patients    ) {
        this.patients = patients;
    }


    public Team getTeam() {
        return team;
    }

    public void setTeam(Team team) {
        this.team = team;
    }
    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}
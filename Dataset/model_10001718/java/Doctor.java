





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String locations;
    private String specialty;





    private List<Team> teams;




    private List<Patient> patients;


    public Doctor(
        String locations,        String specialty    ) {
        this.locations = locations;
        this.specialty = specialty;
        this.teams = new ArrayList<>();
        this.patients = new ArrayList<>();
    }

    public Doctor(
        String locations,        String specialty        ArrayList<Team> teams,        ArrayList<Patient> patients    ) {
        this.locations = locations;
        this.specialty = specialty;
        this.teams = teams;
        this.patients = patients;
    }

    public String getLocations() {
        return locations;
    }

    public void setLocations(String locations) {
        this.locations = locations;
    }
    public String getSpecialty() {
        return specialty;
    }

    public void setSpecialty(String specialty) {
        this.specialty = specialty;
    }

    public List<Team> getTeams() {
        return teams;
    }

    public void addTeam(Team team) {
        this.teams.add(team);
    }
    public List<Patient> getPatients() {
        return patients;
    }

    public void addPatient(Patient patient) {
        this.patients.add(patient);
    }

}
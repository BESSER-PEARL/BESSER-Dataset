





import java.util.List;
import java.util.ArrayList;

public class System  {

    private float Update;
    private boolean Status;





    private List<MicroPhone> microphones;




    private List<Sensor> sensors;




    private HouseHolds households;




    private Home_Security_System home_security_system;




    private HomeTheatre hometheatre;


    public System(
        float Update,        boolean Status    ) {
        this.Update = Update;
        this.Status = Status;
        this.microphones = new ArrayList<>();
        this.sensors = new ArrayList<>();
    }

    public System(
        float Update,        boolean Status        ArrayList<MicroPhone> microphones,        ArrayList<Sensor> sensors    ) {
        this.Update = Update;
        this.Status = Status;
        this.microphones = microphones;
        this.sensors = sensors;
    }

    public float getUpdate() {
        return Update;
    }

    public void setUpdate(float Update) {
        this.Update = Update;
    }
    public boolean getStatus() {
        return Status;
    }

    public void setStatus(boolean Status) {
        this.Status = Status;
    }

    public List<MicroPhone> getMicrophones() {
        return microphones;
    }

    public void addMicrophone(Microphone microphone) {
        this.microphones.add(microphone);
    }
    public List<Sensor> getSensors() {
        return sensors;
    }

    public void addSensor(Sensor sensor) {
        this.sensors.add(sensor);
    }
    public HouseHolds getHouseholds() {
        return households;
    }

    public void setHouseholds(HouseHolds households) {
        this.households = households;
    }
    public Home_Security_System getHome_security_system() {
        return home_security_system;
    }

    public void setHome_security_system(Home_Security_System home_security_system) {
        this.home_security_system = home_security_system;
    }
    public HomeTheatre getHometheatre() {
        return hometheatre;
    }

    public void setHometheatre(HomeTheatre hometheatre) {
        this.hometheatre = hometheatre;
    }

}
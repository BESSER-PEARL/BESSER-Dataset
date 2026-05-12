





import java.util.List;
import java.util.ArrayList;

public class System  {

    private float Update;
    private boolean Status;





    private List<MicroPhone> microphones;




    private Microcontroller microcontroller;




    private HouseHolds households;




    private HomeTheatre hometheatre;


    public System(
        float Update,        boolean Status    ) {
        this.Update = Update;
        this.Status = Status;
        this.microphones = new ArrayList<>();
    }

    public System(
        float Update,        boolean Status        ArrayList<MicroPhone> microphones    ) {
        this.Update = Update;
        this.Status = Status;
        this.microphones = microphones;
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
    public Microcontroller getMicrocontroller() {
        return microcontroller;
    }

    public void setMicrocontroller(Microcontroller microcontroller) {
        this.microcontroller = microcontroller;
    }
    public HouseHolds getHouseholds() {
        return households;
    }

    public void setHouseholds(HouseHolds households) {
        this.households = households;
    }
    public HomeTheatre getHometheatre() {
        return hometheatre;
    }

    public void setHometheatre(HomeTheatre hometheatre) {
        this.hometheatre = hometheatre;
    }

}
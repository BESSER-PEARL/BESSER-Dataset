





import java.util.List;
import java.util.ArrayList;

public class System  {

    private boolean Status;
    private float Update;





    private List<MicroPhone> microphones;




    private HouseHolds households;




    private HomeTheatre hometheatre;


    public System(
        boolean Status,        float Update    ) {
        this.Status = Status;
        this.Update = Update;
        this.microphones = new ArrayList<>();
    }

    public System(
        boolean Status,        float Update        ArrayList<MicroPhone> microphones    ) {
        this.Status = Status;
        this.Update = Update;
        this.microphones = microphones;
    }

    public boolean getStatus() {
        return Status;
    }

    public void setStatus(boolean Status) {
        this.Status = Status;
    }
    public float getUpdate() {
        return Update;
    }

    public void setUpdate(float Update) {
        this.Update = Update;
    }

    public List<MicroPhone> getMicrophones() {
        return microphones;
    }

    public void addMicrophone(Microphone microphone) {
        this.microphones.add(microphone);
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
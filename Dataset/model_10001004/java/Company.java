





import java.util.List;
import java.util.ArrayList;

public class Company  {






    private List<Pilot> pilots;


    public Company(
    ) {
        this.pilots = new ArrayList<>();
    }

    public Company(
        ArrayList<Pilot> pilots    ) {
        this.pilots = pilots;
    }


    public List<Pilot> getPilots() {
        return pilots;
    }

    public void addPilot(Pilot pilot) {
        this.pilots.add(pilot);
    }

}
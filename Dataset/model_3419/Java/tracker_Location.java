





import java.util.List;
import java.util.ArrayList;

public class tracker_Location  {

    private String name;





    private tracker_Sighting tracker_sighting;




    private tracker_Premises tracker_premises;


    public tracker_Location(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tracker_Sighting getTracker_sighting() {
        return tracker_sighting;
    }

    public void setTracker_sighting(tracker_Sighting tracker_sighting) {
        this.tracker_sighting = tracker_sighting;
    }
    public tracker_Premises getTracker_premises() {
        return tracker_premises;
    }

    public void setTracker_premises(tracker_Premises tracker_premises) {
        this.tracker_premises = tracker_premises;
    }

}
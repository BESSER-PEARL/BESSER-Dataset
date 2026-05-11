





import java.util.List;
import java.util.ArrayList;

public class tracker_UnAppliedTags  {






    private tracker_Premises tracker_premises;




    private List<tracker_AnimalId> tracker_animalids;


    public tracker_UnAppliedTags(
    ) {
        this.tracker_animalids = new ArrayList<>();
    }

    public tracker_UnAppliedTags(
        ArrayList<tracker_AnimalId> tracker_animalids    ) {
        this.tracker_animalids = tracker_animalids;
    }


    public tracker_Premises getTracker_premises() {
        return tracker_premises;
    }

    public void setTracker_premises(tracker_Premises tracker_premises) {
        this.tracker_premises = tracker_premises;
    }
    public List<tracker_AnimalId> getTracker_animalids() {
        return tracker_animalids;
    }

    public void addTracker_animalid(Tracker_animalid tracker_animalid) {
        this.tracker_animalids.add(tracker_animalid);
    }

}
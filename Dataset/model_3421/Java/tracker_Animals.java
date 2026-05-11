





import java.util.List;
import java.util.ArrayList;

public class tracker_Animals  {






    private List<tracker_Animal> tracker_animals;




    private tracker_Premises tracker_premises;


    public tracker_Animals(
    ) {
        this.tracker_animals = new ArrayList<>();
    }

    public tracker_Animals(
        ArrayList<tracker_Animal> tracker_animals    ) {
        this.tracker_animals = tracker_animals;
    }


    public List<tracker_Animal> getTracker_animals() {
        return tracker_animals;
    }

    public void addTracker_animal(Tracker_animal tracker_animal) {
        this.tracker_animals.add(tracker_animal);
    }
    public tracker_Premises getTracker_premises() {
        return tracker_premises;
    }

    public void setTracker_premises(tracker_Premises tracker_premises) {
        this.tracker_premises = tracker_premises;
    }

}






import java.util.List;
import java.util.ArrayList;

public class tracker_Tag  {

    private boolean usainNumberUsed;
    private String id;





    private tracker_Animal tracker_animal;


    public tracker_Tag(
        boolean usainNumberUsed,        String id    ) {
        this.usainNumberUsed = usainNumberUsed;
        this.id = id;
    }


    public boolean getUsainnumberused() {
        return usainNumberUsed;
    }

    public void setUsainnumberused(boolean usainNumberUsed) {
        this.usainNumberUsed = usainNumberUsed;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public tracker_Animal getTracker_animal() {
        return tracker_animal;
    }

    public void setTracker_animal(tracker_Animal tracker_animal) {
        this.tracker_animal = tracker_animal;
    }

}
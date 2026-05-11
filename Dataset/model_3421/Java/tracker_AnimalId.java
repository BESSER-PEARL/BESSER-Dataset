





import java.util.List;
import java.util.ArrayList;

public class tracker_AnimalId  {

    private String idNumber;
    private boolean usainNumberUsed;





    private tracker_Animal tracker_animal;


    public tracker_AnimalId(
        String idNumber,        boolean usainNumberUsed    ) {
        this.idNumber = idNumber;
        this.usainNumberUsed = usainNumberUsed;
    }


    public String getIdnumber() {
        return idNumber;
    }

    public void setIdnumber(String idNumber) {
        this.idNumber = idNumber;
    }
    public boolean getUsainnumberused() {
        return usainNumberUsed;
    }

    public void setUsainnumberused(boolean usainNumberUsed) {
        this.usainNumberUsed = usainNumberUsed;
    }

    public tracker_Animal getTracker_animal() {
        return tracker_animal;
    }

    public void setTracker_animal(tracker_Animal tracker_animal) {
        this.tracker_animal = tracker_animal;
    }

}
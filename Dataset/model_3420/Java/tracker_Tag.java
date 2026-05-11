





import java.util.List;
import java.util.ArrayList;

public class tracker_Tag  {

    private String idNumber;
    private boolean usainNumberUsed;





    private tracker_Animal tracker_animal;




    private tracker_Premises tracker_premises;


    public tracker_Tag(
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
    public tracker_Premises getTracker_premises() {
        return tracker_premises;
    }

    public void setTracker_premises(tracker_Premises tracker_premises) {
        this.tracker_premises = tracker_premises;
    }

}
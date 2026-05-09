





import java.util.List;
import java.util.ArrayList;

public class esmodel_events_MergeEvent extends Event {

    private int totalTime;
    private int numberOfConflicts;



    public esmodel_events_MergeEvent(
        int totalTime,        int numberOfConflicts    ) {
        super(
        );
        this.totalTime = totalTime;
        this.numberOfConflicts = numberOfConflicts;
    }


    public int getTotaltime() {
        return totalTime;
    }

    public void setTotaltime(int totalTime) {
        this.totalTime = totalTime;
    }
    public int getNumberofconflicts() {
        return numberOfConflicts;
    }

    public void setNumberofconflicts(int numberOfConflicts) {
        this.numberOfConflicts = numberOfConflicts;
    }


}
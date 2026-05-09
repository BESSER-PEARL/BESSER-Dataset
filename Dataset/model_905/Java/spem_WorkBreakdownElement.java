





import java.util.List;
import java.util.ArrayList;

public class spem_WorkBreakdownElement extends BreakdownElement {

    private boolean isOngoing;
    private boolean isEventDriven;
    private boolean isRepeatable;





    private spem_WorkSequence spem_worksequence;




    private List<spem_WorkSequence> spem_worksequences;




    private spem_WorkSequence spem_worksequence;




    private List<spem_WorkSequence> spem_worksequences;


    public spem_WorkBreakdownElement(
        boolean isOngoing,        boolean isEventDriven,        boolean isRepeatable    ) {
        super(
        );
        this.isOngoing = isOngoing;
        this.isEventDriven = isEventDriven;
        this.isRepeatable = isRepeatable;
        this.spem_worksequences = new ArrayList<>();
        this.spem_worksequences = new ArrayList<>();
    }

    public spem_WorkBreakdownElement(
        boolean isOngoing,        boolean isEventDriven,        boolean isRepeatable        ArrayList<spem_WorkSequence> spem_worksequences,        ArrayList<spem_WorkSequence> spem_worksequences    ) {
        this.isOngoing = isOngoing;
        this.isEventDriven = isEventDriven;
        this.isRepeatable = isRepeatable;
        this.spem_worksequences = spem_worksequences;
        this.spem_worksequences = spem_worksequences;
    }

    public boolean getIsongoing() {
        return isOngoing;
    }

    public void setIsongoing(boolean isOngoing) {
        this.isOngoing = isOngoing;
    }
    public boolean getIseventdriven() {
        return isEventDriven;
    }

    public void setIseventdriven(boolean isEventDriven) {
        this.isEventDriven = isEventDriven;
    }
    public boolean getIsrepeatable() {
        return isRepeatable;
    }

    public void setIsrepeatable(boolean isRepeatable) {
        this.isRepeatable = isRepeatable;
    }

    public spem_WorkSequence getSpem_worksequence() {
        return spem_worksequence;
    }

    public void setSpem_worksequence(spem_WorkSequence spem_worksequence) {
        this.spem_worksequence = spem_worksequence;
    }
    public List<spem_WorkSequence> getSpem_worksequences() {
        return spem_worksequences;
    }

    public void addSpem_worksequence(Spem_worksequence spem_worksequence) {
        this.spem_worksequences.add(spem_worksequence);
    }
    public spem_WorkSequence getSpem_worksequence() {
        return spem_worksequence;
    }

    public void setSpem_worksequence(spem_WorkSequence spem_worksequence) {
        this.spem_worksequence = spem_worksequence;
    }
    public List<spem_WorkSequence> getSpem_worksequences() {
        return spem_worksequences;
    }

    public void addSpem_worksequence(Spem_worksequence spem_worksequence) {
        this.spem_worksequences.add(spem_worksequence);
    }

}
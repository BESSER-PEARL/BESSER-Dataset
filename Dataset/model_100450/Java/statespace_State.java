





import java.util.List;
import java.util.ArrayList;

public class statespace_State extends Storage {

    private int index;
    private String objectKeys;
    private int hashCode;
    private int objectCount;
    private boolean open;
    private String location;
    private boolean pruned;
    private boolean goal;
    private int derivedFrom;





    private statespace_StateSpace statespace_statespace;




    private statespace_StateSpace statespace_statespace;




    private statespace_StateSpace statespace_statespace;




    private statespace_StateSpace statespace_statespace;




    private statespace_Transition statespace_transition;




    private List<statespace_Transition> statespace_transitions;




    private statespace_Transition statespace_transition;




    private List<statespace_Transition> statespace_transitions;


    public statespace_State(
        int index,        String objectKeys,        int hashCode,        int objectCount,        boolean open,        String location,        boolean pruned,        boolean goal,        int derivedFrom    ) {
        super(
        );
        this.index = index;
        this.objectKeys = objectKeys;
        this.hashCode = hashCode;
        this.objectCount = objectCount;
        this.open = open;
        this.location = location;
        this.pruned = pruned;
        this.goal = goal;
        this.derivedFrom = derivedFrom;
        this.statespace_transitions = new ArrayList<>();
        this.statespace_transitions = new ArrayList<>();
    }

    public statespace_State(
        int index,        String objectKeys,        int hashCode,        int objectCount,        boolean open,        String location,        boolean pruned,        boolean goal,        int derivedFrom        ArrayList<statespace_Transition> statespace_transitions,        ArrayList<statespace_Transition> statespace_transitions    ) {
        this.index = index;
        this.objectKeys = objectKeys;
        this.hashCode = hashCode;
        this.objectCount = objectCount;
        this.open = open;
        this.location = location;
        this.pruned = pruned;
        this.goal = goal;
        this.derivedFrom = derivedFrom;
        this.statespace_transitions = statespace_transitions;
        this.statespace_transitions = statespace_transitions;
    }

    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }
    public String getObjectkeys() {
        return objectKeys;
    }

    public void setObjectkeys(String objectKeys) {
        this.objectKeys = objectKeys;
    }
    public int getHashcode() {
        return hashCode;
    }

    public void setHashcode(int hashCode) {
        this.hashCode = hashCode;
    }
    public int getObjectcount() {
        return objectCount;
    }

    public void setObjectcount(int objectCount) {
        this.objectCount = objectCount;
    }
    public boolean getOpen() {
        return open;
    }

    public void setOpen(boolean open) {
        this.open = open;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public boolean getPruned() {
        return pruned;
    }

    public void setPruned(boolean pruned) {
        this.pruned = pruned;
    }
    public boolean getGoal() {
        return goal;
    }

    public void setGoal(boolean goal) {
        this.goal = goal;
    }
    public int getDerivedfrom() {
        return derivedFrom;
    }

    public void setDerivedfrom(int derivedFrom) {
        this.derivedFrom = derivedFrom;
    }

    public statespace_StateSpace getStatespace_statespace() {
        return statespace_statespace;
    }

    public void setStatespace_statespace(statespace_StateSpace statespace_statespace) {
        this.statespace_statespace = statespace_statespace;
    }
    public statespace_StateSpace getStatespace_statespace() {
        return statespace_statespace;
    }

    public void setStatespace_statespace(statespace_StateSpace statespace_statespace) {
        this.statespace_statespace = statespace_statespace;
    }
    public statespace_StateSpace getStatespace_statespace() {
        return statespace_statespace;
    }

    public void setStatespace_statespace(statespace_StateSpace statespace_statespace) {
        this.statespace_statespace = statespace_statespace;
    }
    public statespace_StateSpace getStatespace_statespace() {
        return statespace_statespace;
    }

    public void setStatespace_statespace(statespace_StateSpace statespace_statespace) {
        this.statespace_statespace = statespace_statespace;
    }
    public statespace_Transition getStatespace_transition() {
        return statespace_transition;
    }

    public void setStatespace_transition(statespace_Transition statespace_transition) {
        this.statespace_transition = statespace_transition;
    }
    public List<statespace_Transition> getStatespace_transitions() {
        return statespace_transitions;
    }

    public void addStatespace_transition(Statespace_transition statespace_transition) {
        this.statespace_transitions.add(statespace_transition);
    }
    public statespace_Transition getStatespace_transition() {
        return statespace_transition;
    }

    public void setStatespace_transition(statespace_Transition statespace_transition) {
        this.statespace_transition = statespace_transition;
    }
    public List<statespace_Transition> getStatespace_transitions() {
        return statespace_transitions;
    }

    public void addStatespace_transition(Statespace_transition statespace_transition) {
        this.statespace_transitions.add(statespace_transition);
    }

}
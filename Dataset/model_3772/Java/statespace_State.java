





import java.util.List;
import java.util.ArrayList;

public class statespace_State extends Storage {

    private boolean pruned;
    private boolean open;
    private int hashCode;
    private String objectKeys;
    private int objectCount;
    private int index;
    private boolean goal;
    private String location;
    private int derivedFrom;





    private statespace_StateSpace statespace_statespace;




    private List<statespace_Transition> statespace_transitions;




    private statespace_StateSpace statespace_statespace;




    private statespace_Transition statespace_transition;




    private statespace_StateSpace statespace_statespace;




    private statespace_Transition statespace_transition;




    private statespace_StateSpace statespace_statespace;




    private List<statespace_Transition> statespace_transitions;


    public statespace_State(
        boolean pruned,        boolean open,        int hashCode,        String objectKeys,        int objectCount,        int index,        boolean goal,        String location,        int derivedFrom    ) {
        super(
        );
        this.pruned = pruned;
        this.open = open;
        this.hashCode = hashCode;
        this.objectKeys = objectKeys;
        this.objectCount = objectCount;
        this.index = index;
        this.goal = goal;
        this.location = location;
        this.derivedFrom = derivedFrom;
        this.statespace_transitions = new ArrayList<>();
        this.statespace_transitions = new ArrayList<>();
    }

    public statespace_State(
        boolean pruned,        boolean open,        int hashCode,        String objectKeys,        int objectCount,        int index,        boolean goal,        String location,        int derivedFrom        ArrayList<statespace_Transition> statespace_transitions,        ArrayList<statespace_Transition> statespace_transitions    ) {
        this.pruned = pruned;
        this.open = open;
        this.hashCode = hashCode;
        this.objectKeys = objectKeys;
        this.objectCount = objectCount;
        this.index = index;
        this.goal = goal;
        this.location = location;
        this.derivedFrom = derivedFrom;
        this.statespace_transitions = statespace_transitions;
        this.statespace_transitions = statespace_transitions;
    }

    public boolean getPruned() {
        return pruned;
    }

    public void setPruned(boolean pruned) {
        this.pruned = pruned;
    }
    public boolean getOpen() {
        return open;
    }

    public void setOpen(boolean open) {
        this.open = open;
    }
    public int getHashcode() {
        return hashCode;
    }

    public void setHashcode(int hashCode) {
        this.hashCode = hashCode;
    }
    public String getObjectkeys() {
        return objectKeys;
    }

    public void setObjectkeys(String objectKeys) {
        this.objectKeys = objectKeys;
    }
    public int getObjectcount() {
        return objectCount;
    }

    public void setObjectcount(int objectCount) {
        this.objectCount = objectCount;
    }
    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }
    public boolean getGoal() {
        return goal;
    }

    public void setGoal(boolean goal) {
        this.goal = goal;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
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
    public List<statespace_Transition> getStatespace_transitions() {
        return statespace_transitions;
    }

    public void addStatespace_transition(Statespace_transition statespace_transition) {
        this.statespace_transitions.add(statespace_transition);
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
    public statespace_StateSpace getStatespace_statespace() {
        return statespace_statespace;
    }

    public void setStatespace_statespace(statespace_StateSpace statespace_statespace) {
        this.statespace_statespace = statespace_statespace;
    }
    public List<statespace_Transition> getStatespace_transitions() {
        return statespace_transitions;
    }

    public void addStatespace_transition(Statespace_transition statespace_transition) {
        this.statespace_transitions.add(statespace_transition);
    }

}
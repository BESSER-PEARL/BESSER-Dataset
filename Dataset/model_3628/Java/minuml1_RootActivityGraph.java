





import java.util.List;
import java.util.ArrayList;

public class minuml1_RootActivityGraph  {

    private String name;





    private List<minuml1_Transition> minuml1_transitions;




    private List<minuml1_Partition> minuml1_partitions;




    private minuml1_State minuml1_state;


    public minuml1_RootActivityGraph(
        String name    ) {
        this.name = name;
        this.minuml1_transitions = new ArrayList<>();
        this.minuml1_partitions = new ArrayList<>();
    }

    public minuml1_RootActivityGraph(
        String name        ArrayList<minuml1_Transition> minuml1_transitions,        ArrayList<minuml1_Partition> minuml1_partitions    ) {
        this.name = name;
        this.minuml1_transitions = minuml1_transitions;
        this.minuml1_partitions = minuml1_partitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<minuml1_Transition> getMinuml1_transitions() {
        return minuml1_transitions;
    }

    public void addMinuml1_transition(Minuml1_transition minuml1_transition) {
        this.minuml1_transitions.add(minuml1_transition);
    }
    public List<minuml1_Partition> getMinuml1_partitions() {
        return minuml1_partitions;
    }

    public void addMinuml1_partition(Minuml1_partition minuml1_partition) {
        this.minuml1_partitions.add(minuml1_partition);
    }
    public minuml1_State getMinuml1_state() {
        return minuml1_state;
    }

    public void setMinuml1_state(minuml1_State minuml1_state) {
        this.minuml1_state = minuml1_state;
    }

}
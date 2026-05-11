





import java.util.List;
import java.util.ArrayList;

public class thingML_Session extends Region, AnnotatedElement, State {

    private int maxInstances;





    private List<thingML_State> thingml_states;




    private List<thingML_ParallelRegion> thingml_parallelregions;




    private thingML_State thingml_state;


    public thingML_Session(
        int maxInstances    ) {
        super(
        );
        this.maxInstances = maxInstances;
        this.thingml_states = new ArrayList<>();
        this.thingml_parallelregions = new ArrayList<>();
    }

    public thingML_Session(
        int maxInstances        ArrayList<thingML_State> thingml_states,        ArrayList<thingML_ParallelRegion> thingml_parallelregions    ) {
        this.maxInstances = maxInstances;
        this.thingml_states = thingml_states;
        this.thingml_parallelregions = thingml_parallelregions;
    }

    public int getMaxinstances() {
        return maxInstances;
    }

    public void setMaxinstances(int maxInstances) {
        this.maxInstances = maxInstances;
    }

    public List<thingML_State> getThingml_states() {
        return thingml_states;
    }

    public void addThingml_state(Thingml_state thingml_state) {
        this.thingml_states.add(thingml_state);
    }
    public List<thingML_ParallelRegion> getThingml_parallelregions() {
        return thingml_parallelregions;
    }

    public void addThingml_parallelregion(Thingml_parallelregion thingml_parallelregion) {
        this.thingml_parallelregions.add(thingml_parallelregion);
    }
    public thingML_State getThingml_state() {
        return thingml_state;
    }

    public void setThingml_state(thingML_State thingml_state) {
        this.thingml_state = thingml_state;
    }

}
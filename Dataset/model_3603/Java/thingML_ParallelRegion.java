





import java.util.List;
import java.util.ArrayList;

public class thingML_ParallelRegion extends Region, AnnotatedElement {

    private String name;
    private boolean history;





    private thingML_CompositeState thingml_compositestate;




    private thingML_State thingml_state;




    private List<thingML_State> thingml_states;


    public thingML_ParallelRegion(
        String name,        boolean history    ) {
        super(
        );
        this.name = name;
        this.history = history;
        this.thingml_states = new ArrayList<>();
    }

    public thingML_ParallelRegion(
        String name,        boolean history        ArrayList<thingML_State> thingml_states    ) {
        this.name = name;
        this.history = history;
        this.thingml_states = thingml_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getHistory() {
        return history;
    }

    public void setHistory(boolean history) {
        this.history = history;
    }

    public thingML_CompositeState getThingml_compositestate() {
        return thingml_compositestate;
    }

    public void setThingml_compositestate(thingML_CompositeState thingml_compositestate) {
        this.thingml_compositestate = thingml_compositestate;
    }
    public thingML_State getThingml_state() {
        return thingml_state;
    }

    public void setThingml_state(thingML_State thingml_state) {
        this.thingml_state = thingml_state;
    }
    public List<thingML_State> getThingml_states() {
        return thingml_states;
    }

    public void addThingml_state(Thingml_state thingml_state) {
        this.thingml_states.add(thingml_state);
    }

}
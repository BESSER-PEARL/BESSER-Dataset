





import java.util.List;
import java.util.ArrayList;

public class thingml_Region extends AnnotatedElement {

    private boolean history;





    private List<thingml_State> thingml_states;




    private thingml_State thingml_state;


    public thingml_Region(
        boolean history    ) {
        super(
        );
        this.history = history;
        this.thingml_states = new ArrayList<>();
    }

    public thingml_Region(
        boolean history        ArrayList<thingml_State> thingml_states    ) {
        this.history = history;
        this.thingml_states = thingml_states;
    }

    public boolean getHistory() {
        return history;
    }

    public void setHistory(boolean history) {
        this.history = history;
    }

    public List<thingml_State> getThingml_states() {
        return thingml_states;
    }

    public void addThingml_state(Thingml_state thingml_state) {
        this.thingml_states.add(thingml_state);
    }
    public thingml_State getThingml_state() {
        return thingml_state;
    }

    public void setThingml_state(thingml_State thingml_state) {
        this.thingml_state = thingml_state;
    }

}
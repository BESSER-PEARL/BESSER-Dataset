





import java.util.List;
import java.util.ArrayList;

public class thingML_StateContainer extends NamedElement, AnnotatedElement {

    private boolean history;





    private thingML_State thingml_state;




    private List<thingML_State> thingml_states;


    public thingML_StateContainer(
        boolean history    ) {
        super(
        );
        this.history = history;
        this.thingml_states = new ArrayList<>();
    }

    public thingML_StateContainer(
        boolean history        ArrayList<thingML_State> thingml_states    ) {
        this.history = history;
        this.thingml_states = thingml_states;
    }

    public boolean getHistory() {
        return history;
    }

    public void setHistory(boolean history) {
        this.history = history;
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
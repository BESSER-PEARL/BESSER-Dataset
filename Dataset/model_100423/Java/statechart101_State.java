





import java.util.List;
import java.util.ArrayList;

public class statechart101_State extends NamedElement {

    private String label;
    private String type;
    private String activity;





    private statechart101_State statechart101_state;




    private List<statechart101_State> statechart101_states;


    public statechart101_State(
        String label,        String type,        String activity    ) {
        super(
        );
        this.label = label;
        this.type = type;
        this.activity = activity;
        this.statechart101_states = new ArrayList<>();
    }

    public statechart101_State(
        String label,        String type,        String activity        ArrayList<statechart101_State> statechart101_states    ) {
        this.label = label;
        this.type = type;
        this.activity = activity;
        this.statechart101_states = statechart101_states;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }

    public statechart101_State getStatechart101_state() {
        return statechart101_state;
    }

    public void setStatechart101_state(statechart101_State statechart101_state) {
        this.statechart101_state = statechart101_state;
    }
    public List<statechart101_State> getStatechart101_states() {
        return statechart101_states;
    }

    public void addStatechart101_state(Statechart101_state statechart101_state) {
        this.statechart101_states.add(statechart101_state);
    }

}
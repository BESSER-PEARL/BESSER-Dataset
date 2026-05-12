





import java.util.List;
import java.util.ArrayList;

public class statechart02_State  {

    private String activity;
    private String name;
    private String label;
    private String type;





    private statechart02_State statechart02_state;




    private List<statechart02_State> statechart02_states;


    public statechart02_State(
        String activity,        String name,        String label,        String type    ) {
        this.activity = activity;
        this.name = name;
        this.label = label;
        this.type = type;
        this.statechart02_states = new ArrayList<>();
    }

    public statechart02_State(
        String activity,        String name,        String label,        String type        ArrayList<statechart02_State> statechart02_states    ) {
        this.activity = activity;
        this.name = name;
        this.label = label;
        this.type = type;
        this.statechart02_states = statechart02_states;
    }

    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

    public statechart02_State getStatechart02_state() {
        return statechart02_state;
    }

    public void setStatechart02_state(statechart02_State statechart02_state) {
        this.statechart02_state = statechart02_state;
    }
    public List<statechart02_State> getStatechart02_states() {
        return statechart02_states;
    }

    public void addStatechart02_state(Statechart02_state statechart02_state) {
        this.statechart02_states.add(statechart02_state);
    }

}
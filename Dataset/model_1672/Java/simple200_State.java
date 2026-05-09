





import java.util.List;
import java.util.ArrayList;

public class simple200_State extends NamedElement {

    private String label;
    private String activity;
    private String type;





    private simple200_State simple200_state;




    private List<simple200_State> simple200_states;


    public simple200_State(
        String label,        String activity,        String type    ) {
        super(
        );
        this.label = label;
        this.activity = activity;
        this.type = type;
        this.simple200_states = new ArrayList<>();
    }

    public simple200_State(
        String label,        String activity,        String type        ArrayList<simple200_State> simple200_states    ) {
        this.label = label;
        this.activity = activity;
        this.type = type;
        this.simple200_states = simple200_states;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getActivity() {
        return activity;
    }

    public void setActivity(String activity) {
        this.activity = activity;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public simple200_State getSimple200_state() {
        return simple200_state;
    }

    public void setSimple200_state(simple200_State simple200_state) {
        this.simple200_state = simple200_state;
    }
    public List<simple200_State> getSimple200_states() {
        return simple200_states;
    }

    public void addSimple200_state(Simple200_state simple200_state) {
        this.simple200_states.add(simple200_state);
    }

}
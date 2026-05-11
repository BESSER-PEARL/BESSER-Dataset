





import java.util.List;
import java.util.ArrayList;

public class cstat1_AbstractState  {

    private String id;
    private String type;





    private cstat1_Transition cstat1_transition;




    private cstat1_Transition cstat1_transition;




    private List<cstat1_Transition> cstat1_transitions;


    public cstat1_AbstractState(
        String id,        String type    ) {
        this.id = id;
        this.type = type;
        this.cstat1_transitions = new ArrayList<>();
    }

    public cstat1_AbstractState(
        String id,        String type        ArrayList<cstat1_Transition> cstat1_transitions    ) {
        this.id = id;
        this.type = type;
        this.cstat1_transitions = cstat1_transitions;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public cstat1_Transition getCstat1_transition() {
        return cstat1_transition;
    }

    public void setCstat1_transition(cstat1_Transition cstat1_transition) {
        this.cstat1_transition = cstat1_transition;
    }
    public cstat1_Transition getCstat1_transition() {
        return cstat1_transition;
    }

    public void setCstat1_transition(cstat1_Transition cstat1_transition) {
        this.cstat1_transition = cstat1_transition;
    }
    public List<cstat1_Transition> getCstat1_transitions() {
        return cstat1_transitions;
    }

    public void addCstat1_transition(Cstat1_transition cstat1_transition) {
        this.cstat1_transitions.add(cstat1_transition);
    }

}
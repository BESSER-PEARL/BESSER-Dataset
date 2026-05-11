





import java.util.List;
import java.util.ArrayList;

public class scxml_TransitionTarget extends Node {

    private String id;





    private scxml_Transition scxml_transition;


    public scxml_TransitionTarget(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public scxml_Transition getScxml_transition() {
        return scxml_transition;
    }

    public void setScxml_transition(scxml_Transition scxml_transition) {
        this.scxml_transition = scxml_transition;
    }

}
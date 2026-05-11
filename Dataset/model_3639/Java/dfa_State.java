





import java.util.List;
import java.util.ArrayList;

public class dfa_State extends NamedElement {

    private String description;





    private dfa_Transition dfa_transition;


    public dfa_State(
        String description    ) {
        super(
        );
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public dfa_Transition getDfa_transition() {
        return dfa_transition;
    }

    public void setDfa_transition(dfa_Transition dfa_transition) {
        this.dfa_transition = dfa_transition;
    }

}
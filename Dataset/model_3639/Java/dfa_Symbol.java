





import java.util.List;
import java.util.ArrayList;

public class dfa_Symbol  {

    private String literal;
    private String direction;
    private String description;





    private dfa_Transition dfa_transition;


    public dfa_Symbol(
        String literal,        String direction,        String description    ) {
        this.literal = literal;
        this.direction = direction;
        this.description = description;
    }


    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
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
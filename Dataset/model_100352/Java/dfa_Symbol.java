





import java.util.List;
import java.util.ArrayList;

public class dfa_Symbol  {

    private String description;
    private String direction;
    private String literal;





    private dfa_Language dfa_language;




    private dfa_Transition dfa_transition;


    public dfa_Symbol(
        String description,        String direction,        String literal    ) {
        this.description = description;
        this.direction = direction;
        this.literal = literal;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }

    public dfa_Language getDfa_language() {
        return dfa_language;
    }

    public void setDfa_language(dfa_Language dfa_language) {
        this.dfa_language = dfa_language;
    }
    public dfa_Transition getDfa_transition() {
        return dfa_transition;
    }

    public void setDfa_transition(dfa_Transition dfa_transition) {
        this.dfa_transition = dfa_transition;
    }

}
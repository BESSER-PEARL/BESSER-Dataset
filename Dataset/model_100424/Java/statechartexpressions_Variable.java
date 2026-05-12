





import java.util.List;
import java.util.ArrayList;

public class statechartexpressions_Variable  {

    private String identifier;





    private statechartexpressions_VariableReference statechartexpressions_variablereference;


    public statechartexpressions_Variable(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public statechartexpressions_VariableReference getStatechartexpressions_variablereference() {
        return statechartexpressions_variablereference;
    }

    public void setStatechartexpressions_variablereference(statechartexpressions_VariableReference statechartexpressions_variablereference) {
        this.statechartexpressions_variablereference = statechartexpressions_variablereference;
    }

}
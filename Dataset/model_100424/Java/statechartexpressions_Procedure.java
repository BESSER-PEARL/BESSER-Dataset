





import java.util.List;
import java.util.ArrayList;

public class statechartexpressions_Procedure  {

    private String identifier;





    private statechartexpressions_ProcedureCall statechartexpressions_procedurecall;


    public statechartexpressions_Procedure(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public statechartexpressions_ProcedureCall getStatechartexpressions_procedurecall() {
        return statechartexpressions_procedurecall;
    }

    public void setStatechartexpressions_procedurecall(statechartexpressions_ProcedureCall statechartexpressions_procedurecall) {
        this.statechartexpressions_procedurecall = statechartexpressions_procedurecall;
    }

}
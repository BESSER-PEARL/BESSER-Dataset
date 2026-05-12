





import java.util.List;
import java.util.ArrayList;

public class sparql_AdditionalValueLogicalNE extends LocatedElement {






    private sparql_ConditionalAndExpression sparql_conditionalandexpression;




    private sparql_RelationalExpression sparql_relationalexpression;


    public sparql_AdditionalValueLogicalNE(
    ) {
        super(
        );
    }



    public sparql_ConditionalAndExpression getSparql_conditionalandexpression() {
        return sparql_conditionalandexpression;
    }

    public void setSparql_conditionalandexpression(sparql_ConditionalAndExpression sparql_conditionalandexpression) {
        this.sparql_conditionalandexpression = sparql_conditionalandexpression;
    }
    public sparql_RelationalExpression getSparql_relationalexpression() {
        return sparql_relationalexpression;
    }

    public void setSparql_relationalexpression(sparql_RelationalExpression sparql_relationalexpression) {
        this.sparql_relationalexpression = sparql_relationalexpression;
    }

}
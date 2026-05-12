





import java.util.List;
import java.util.ArrayList;

public class sparql_NumericExpression extends LocatedElement {






    private sparql_RelationalExpression sparql_relationalexpression;




    private sparql_AdditiveExpression sparql_additiveexpression;


    public sparql_NumericExpression(
    ) {
        super(
        );
    }



    public sparql_RelationalExpression getSparql_relationalexpression() {
        return sparql_relationalexpression;
    }

    public void setSparql_relationalexpression(sparql_RelationalExpression sparql_relationalexpression) {
        this.sparql_relationalexpression = sparql_relationalexpression;
    }
    public sparql_AdditiveExpression getSparql_additiveexpression() {
        return sparql_additiveexpression;
    }

    public void setSparql_additiveexpression(sparql_AdditiveExpression sparql_additiveexpression) {
        this.sparql_additiveexpression = sparql_additiveexpression;
    }

}
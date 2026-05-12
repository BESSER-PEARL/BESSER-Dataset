





import java.util.List;
import java.util.ArrayList;

public class sparql_BrackettedExpression extends PrimaryExpression, Constraint {






    private sparql_OrderConditionLeftNE sparql_orderconditionleftne;




    private sparql_Expression sparql_expression;


    public sparql_BrackettedExpression(
    ) {
        super(
        );
    }



    public sparql_OrderConditionLeftNE getSparql_orderconditionleftne() {
        return sparql_orderconditionleftne;
    }

    public void setSparql_orderconditionleftne(sparql_OrderConditionLeftNE sparql_orderconditionleftne) {
        this.sparql_orderconditionleftne = sparql_orderconditionleftne;
    }
    public sparql_Expression getSparql_expression() {
        return sparql_expression;
    }

    public void setSparql_expression(sparql_Expression sparql_expression) {
        this.sparql_expression = sparql_expression;
    }

}
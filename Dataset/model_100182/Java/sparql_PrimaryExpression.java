





import java.util.List;
import java.util.ArrayList;

public class sparql_PrimaryExpression extends UnaryExpression {






    private sparql_MinusPrimaryExpressionNE sparql_minusprimaryexpressionne;




    private sparql_NotPrimaryExpressionNE sparql_notprimaryexpressionne;


    public sparql_PrimaryExpression(
    ) {
        super(
        );
    }



    public sparql_MinusPrimaryExpressionNE getSparql_minusprimaryexpressionne() {
        return sparql_minusprimaryexpressionne;
    }

    public void setSparql_minusprimaryexpressionne(sparql_MinusPrimaryExpressionNE sparql_minusprimaryexpressionne) {
        this.sparql_minusprimaryexpressionne = sparql_minusprimaryexpressionne;
    }
    public sparql_NotPrimaryExpressionNE getSparql_notprimaryexpressionne() {
        return sparql_notprimaryexpressionne;
    }

    public void setSparql_notprimaryexpressionne(sparql_NotPrimaryExpressionNE sparql_notprimaryexpressionne) {
        this.sparql_notprimaryexpressionne = sparql_notprimaryexpressionne;
    }

}
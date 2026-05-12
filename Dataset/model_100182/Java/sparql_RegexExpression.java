





import java.util.List;
import java.util.ArrayList;

public class sparql_RegexExpression extends BuiltInCall {






    private List<sparql_AdditionalExpressionNE> sparql_additionalexpressionnes;




    private sparql_Expression sparql_expression;


    public sparql_RegexExpression(
    ) {
        super(
        );
        this.sparql_additionalexpressionnes = new ArrayList<>();
    }

    public sparql_RegexExpression(
        ArrayList<sparql_AdditionalExpressionNE> sparql_additionalexpressionnes    ) {
        this.sparql_additionalexpressionnes = sparql_additionalexpressionnes;
    }


    public List<sparql_AdditionalExpressionNE> getSparql_additionalexpressionnes() {
        return sparql_additionalexpressionnes;
    }

    public void addSparql_additionalexpressionne(Sparql_additionalexpressionne sparql_additionalexpressionne) {
        this.sparql_additionalexpressionnes.add(sparql_additionalexpressionne);
    }
    public sparql_Expression getSparql_expression() {
        return sparql_expression;
    }

    public void setSparql_expression(sparql_Expression sparql_expression) {
        this.sparql_expression = sparql_expression;
    }

}
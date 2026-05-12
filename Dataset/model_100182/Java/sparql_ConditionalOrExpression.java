





import java.util.List;
import java.util.ArrayList;

public class sparql_ConditionalOrExpression extends LocatedElement {






    private sparql_AdditionalExpressionNE sparql_additionalexpressionne;




    private sparql_Expression sparql_expression;




    private List<sparql_AdditionalConditionalAndExpressionNE> sparql_additionalconditionalandexpressionnes;


    public sparql_ConditionalOrExpression(
    ) {
        super(
        );
        this.sparql_additionalconditionalandexpressionnes = new ArrayList<>();
    }

    public sparql_ConditionalOrExpression(
        ArrayList<sparql_AdditionalConditionalAndExpressionNE> sparql_additionalconditionalandexpressionnes    ) {
        this.sparql_additionalconditionalandexpressionnes = sparql_additionalconditionalandexpressionnes;
    }


    public sparql_AdditionalExpressionNE getSparql_additionalexpressionne() {
        return sparql_additionalexpressionne;
    }

    public void setSparql_additionalexpressionne(sparql_AdditionalExpressionNE sparql_additionalexpressionne) {
        this.sparql_additionalexpressionne = sparql_additionalexpressionne;
    }
    public sparql_Expression getSparql_expression() {
        return sparql_expression;
    }

    public void setSparql_expression(sparql_Expression sparql_expression) {
        this.sparql_expression = sparql_expression;
    }
    public List<sparql_AdditionalConditionalAndExpressionNE> getSparql_additionalconditionalandexpressionnes() {
        return sparql_additionalconditionalandexpressionnes;
    }

    public void addSparql_additionalconditionalandexpressionne(Sparql_additionalconditionalandexpressionne sparql_additionalconditionalandexpressionne) {
        this.sparql_additionalconditionalandexpressionnes.add(sparql_additionalconditionalandexpressionne);
    }

}
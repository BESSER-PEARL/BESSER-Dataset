





import java.util.List;
import java.util.ArrayList;

public class sparql_ConditionalAndExpression extends LocatedElement {






    private sparql_ValueLogical sparql_valuelogical;




    private sparql_ConditionalOrExpression sparql_conditionalorexpression;




    private sparql_AdditionalConditionalAndExpressionNE sparql_additionalconditionalandexpressionne;


    public sparql_ConditionalAndExpression(
    ) {
        super(
        );
    }



    public sparql_ValueLogical getSparql_valuelogical() {
        return sparql_valuelogical;
    }

    public void setSparql_valuelogical(sparql_ValueLogical sparql_valuelogical) {
        this.sparql_valuelogical = sparql_valuelogical;
    }
    public sparql_ConditionalOrExpression getSparql_conditionalorexpression() {
        return sparql_conditionalorexpression;
    }

    public void setSparql_conditionalorexpression(sparql_ConditionalOrExpression sparql_conditionalorexpression) {
        this.sparql_conditionalorexpression = sparql_conditionalorexpression;
    }
    public sparql_AdditionalConditionalAndExpressionNE getSparql_additionalconditionalandexpressionne() {
        return sparql_additionalconditionalandexpressionne;
    }

    public void setSparql_additionalconditionalandexpressionne(sparql_AdditionalConditionalAndExpressionNE sparql_additionalconditionalandexpressionne) {
        this.sparql_additionalconditionalandexpressionne = sparql_additionalconditionalandexpressionne;
    }

}
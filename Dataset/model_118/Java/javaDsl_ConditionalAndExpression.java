





import java.util.List;
import java.util.ArrayList;

public class javaDsl_ConditionalAndExpression  {

    private String operators;





    private List<javaDsl_InclusiveOrExpression> javadsl_inclusiveorexpressions;




    private javaDsl_ConditionalOrExpression javadsl_conditionalorexpression;


    public javaDsl_ConditionalAndExpression(
        String operators    ) {
        this.operators = operators;
        this.javadsl_inclusiveorexpressions = new ArrayList<>();
    }

    public javaDsl_ConditionalAndExpression(
        String operators        ArrayList<javaDsl_InclusiveOrExpression> javadsl_inclusiveorexpressions    ) {
        this.operators = operators;
        this.javadsl_inclusiveorexpressions = javadsl_inclusiveorexpressions;
    }

    public String getOperators() {
        return operators;
    }

    public void setOperators(String operators) {
        this.operators = operators;
    }

    public List<javaDsl_InclusiveOrExpression> getJavadsl_inclusiveorexpressions() {
        return javadsl_inclusiveorexpressions;
    }

    public void addJavadsl_inclusiveorexpression(Javadsl_inclusiveorexpression javadsl_inclusiveorexpression) {
        this.javadsl_inclusiveorexpressions.add(javadsl_inclusiveorexpression);
    }
    public javaDsl_ConditionalOrExpression getJavadsl_conditionalorexpression() {
        return javadsl_conditionalorexpression;
    }

    public void setJavadsl_conditionalorexpression(javaDsl_ConditionalOrExpression javadsl_conditionalorexpression) {
        this.javadsl_conditionalorexpression = javadsl_conditionalorexpression;
    }

}
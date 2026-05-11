





import java.util.List;
import java.util.ArrayList;

public class alf_ConditionalOrExpression  {






    private List<alf_ConditionalAndExpression> alf_conditionalandexpressions;




    private alf_ConditionalTestExpression alf_conditionaltestexpression;


    public alf_ConditionalOrExpression(
    ) {
        this.alf_conditionalandexpressions = new ArrayList<>();
    }

    public alf_ConditionalOrExpression(
        ArrayList<alf_ConditionalAndExpression> alf_conditionalandexpressions    ) {
        this.alf_conditionalandexpressions = alf_conditionalandexpressions;
    }


    public List<alf_ConditionalAndExpression> getAlf_conditionalandexpressions() {
        return alf_conditionalandexpressions;
    }

    public void addAlf_conditionalandexpression(Alf_conditionalandexpression alf_conditionalandexpression) {
        this.alf_conditionalandexpressions.add(alf_conditionalandexpression);
    }
    public alf_ConditionalTestExpression getAlf_conditionaltestexpression() {
        return alf_conditionaltestexpression;
    }

    public void setAlf_conditionaltestexpression(alf_ConditionalTestExpression alf_conditionaltestexpression) {
        this.alf_conditionaltestexpression = alf_conditionaltestexpression;
    }

}






import java.util.List;
import java.util.ArrayList;

public class diagram_filter_VariableFilter extends Filter {

    private String semanticConditionExpression;





    private List<filter_FilterVariable> filter_filtervariables;


    public diagram_filter_VariableFilter(
        String semanticConditionExpression    ) {
        super(
        );
        this.semanticConditionExpression = semanticConditionExpression;
        this.filter_filtervariables = new ArrayList<>();
    }

    public diagram_filter_VariableFilter(
        String semanticConditionExpression        ArrayList<filter_FilterVariable> filter_filtervariables    ) {
        this.semanticConditionExpression = semanticConditionExpression;
        this.filter_filtervariables = filter_filtervariables;
    }

    public String getSemanticconditionexpression() {
        return semanticConditionExpression;
    }

    public void setSemanticconditionexpression(String semanticConditionExpression) {
        this.semanticConditionExpression = semanticConditionExpression;
    }

    public List<filter_FilterVariable> getFilter_filtervariables() {
        return filter_filtervariables;
    }

    public void addFilter_filtervariable(Filter_filtervariable filter_filtervariable) {
        this.filter_filtervariables.add(filter_filtervariable);
    }

}
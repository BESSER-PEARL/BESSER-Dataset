





import java.util.List;
import java.util.ArrayList;

public class diagram_filter_VariableFilter extends Filter {

    private String semanticConditionExpression;



    public diagram_filter_VariableFilter(
        String semanticConditionExpression    ) {
        super(
        );
        this.semanticConditionExpression = semanticConditionExpression;
    }


    public String getSemanticconditionexpression() {
        return semanticConditionExpression;
    }

    public void setSemanticconditionexpression(String semanticConditionExpression) {
        this.semanticConditionExpression = semanticConditionExpression;
    }


}






import java.util.List;
import java.util.ArrayList;

public class sequence_template_TConditionalExecutionStyle extends TTransformer {

    private String predicateExpression;



    public sequence_template_TConditionalExecutionStyle(
        String predicateExpression    ) {
        super(
        );
        this.predicateExpression = predicateExpression;
    }


    public String getPredicateexpression() {
        return predicateExpression;
    }

    public void setPredicateexpression(String predicateExpression) {
        this.predicateExpression = predicateExpression;
    }


}
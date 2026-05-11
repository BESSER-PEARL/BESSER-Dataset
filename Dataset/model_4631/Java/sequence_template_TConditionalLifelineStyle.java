





import java.util.List;
import java.util.ArrayList;

public class sequence_template_TConditionalLifelineStyle extends TTransformer {

    private String predicateExpression;



    public sequence_template_TConditionalLifelineStyle(
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
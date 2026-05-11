





import java.util.List;
import java.util.ArrayList;

public class expression_PredicateComparisonOperator extends Predicate {

    private String operator;



    public expression_PredicateComparisonOperator(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }


}
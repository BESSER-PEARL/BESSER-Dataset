





import java.util.List;
import java.util.ArrayList;

public class expression_PredicateBooleanOperator extends Predicate {

    private String operator;





    private List<expression_Predicate> expression_predicates;


    public expression_PredicateBooleanOperator(
        String operator    ) {
        super(
        );
        this.operator = operator;
        this.expression_predicates = new ArrayList<>();
    }

    public expression_PredicateBooleanOperator(
        String operator        ArrayList<expression_Predicate> expression_predicates    ) {
        this.operator = operator;
        this.expression_predicates = expression_predicates;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public List<expression_Predicate> getExpression_predicates() {
        return expression_predicates;
    }

    public void addExpression_predicate(Expression_predicate expression_predicate) {
        this.expression_predicates.add(expression_predicate);
    }

}
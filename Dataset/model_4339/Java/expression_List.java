





import java.util.List;
import java.util.ArrayList;

public class expression_List extends Term {






    private List<expression_Term> expression_terms;


    public expression_List(
    ) {
        super(
        );
        this.expression_terms = new ArrayList<>();
    }

    public expression_List(
        ArrayList<expression_Term> expression_terms    ) {
        this.expression_terms = expression_terms;
    }


    public List<expression_Term> getExpression_terms() {
        return expression_terms;
    }

    public void addExpression_term(Expression_term expression_term) {
        this.expression_terms.add(expression_term);
    }

}
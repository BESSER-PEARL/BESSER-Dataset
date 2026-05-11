





import java.util.List;
import java.util.ArrayList;

public class expression_Variable extends Expression {






    private expression_PredicateIsEmpty expression_predicateisempty;




    private expression_PredicateIsNull expression_predicateisnull;


    public expression_Variable(
    ) {
        super(
        );
    }



    public expression_PredicateIsEmpty getExpression_predicateisempty() {
        return expression_predicateisempty;
    }

    public void setExpression_predicateisempty(expression_PredicateIsEmpty expression_predicateisempty) {
        this.expression_predicateisempty = expression_predicateisempty;
    }
    public expression_PredicateIsNull getExpression_predicateisnull() {
        return expression_predicateisnull;
    }

    public void setExpression_predicateisnull(expression_PredicateIsNull expression_predicateisnull) {
        this.expression_predicateisnull = expression_predicateisnull;
    }

}
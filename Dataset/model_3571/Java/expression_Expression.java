





import java.util.List;
import java.util.ArrayList;

public class expression_Expression extends SyntaxElement {






    private expression_CollectionExpression expression_collectionexpression;




    private expression_OperationCall expression_operationcall;


    public expression_Expression(
    ) {
        super(
        );
    }



    public expression_CollectionExpression getExpression_collectionexpression() {
        return expression_collectionexpression;
    }

    public void setExpression_collectionexpression(expression_CollectionExpression expression_collectionexpression) {
        this.expression_collectionexpression = expression_collectionexpression;
    }
    public expression_OperationCall getExpression_operationcall() {
        return expression_operationcall;
    }

    public void setExpression_operationcall(expression_OperationCall expression_operationcall) {
        this.expression_operationcall = expression_operationcall;
    }

}
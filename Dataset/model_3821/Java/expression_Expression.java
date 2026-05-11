





import java.util.List;
import java.util.ArrayList;

public class expression_Expression  {

    private float calculatedValue;





    private expression_UnaryExpression expression_unaryexpression;




    private expression_BinaryExpression expression_binaryexpression;




    private expression_BinaryExpression expression_binaryexpression;


    public expression_Expression(
        float calculatedValue    ) {
        this.calculatedValue = calculatedValue;
    }


    public float getCalculatedvalue() {
        return calculatedValue;
    }

    public void setCalculatedvalue(float calculatedValue) {
        this.calculatedValue = calculatedValue;
    }

    public expression_UnaryExpression getExpression_unaryexpression() {
        return expression_unaryexpression;
    }

    public void setExpression_unaryexpression(expression_UnaryExpression expression_unaryexpression) {
        this.expression_unaryexpression = expression_unaryexpression;
    }
    public expression_BinaryExpression getExpression_binaryexpression() {
        return expression_binaryexpression;
    }

    public void setExpression_binaryexpression(expression_BinaryExpression expression_binaryexpression) {
        this.expression_binaryexpression = expression_binaryexpression;
    }
    public expression_BinaryExpression getExpression_binaryexpression() {
        return expression_binaryexpression;
    }

    public void setExpression_binaryexpression(expression_BinaryExpression expression_binaryexpression) {
        this.expression_binaryexpression = expression_binaryexpression;
    }

}
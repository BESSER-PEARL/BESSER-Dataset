





import java.util.List;
import java.util.ArrayList;

public class cSharp_UnaryExpression  {

    private String expUnaryOperator;





    private cSharp_UnaryExpression csharp_unaryexpression;




    private cSharp_Expression csharp_expression;


    public cSharp_UnaryExpression(
        String expUnaryOperator    ) {
        this.expUnaryOperator = expUnaryOperator;
    }


    public String getExpunaryoperator() {
        return expUnaryOperator;
    }

    public void setExpunaryoperator(String expUnaryOperator) {
        this.expUnaryOperator = expUnaryOperator;
    }

    public cSharp_UnaryExpression getCsharp_unaryexpression() {
        return csharp_unaryexpression;
    }

    public void setCsharp_unaryexpression(cSharp_UnaryExpression csharp_unaryexpression) {
        this.csharp_unaryexpression = csharp_unaryexpression;
    }
    public cSharp_Expression getCsharp_expression() {
        return csharp_expression;
    }

    public void setCsharp_expression(cSharp_Expression csharp_expression) {
        this.csharp_expression = csharp_expression;
    }

}
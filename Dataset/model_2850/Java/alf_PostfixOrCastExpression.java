





import java.util.List;
import java.util.ArrayList;

public class alf_PostfixOrCastExpression extends UnaryExpression, CastCompletion {






    private alf_NameOrPrimaryExpression alf_nameorprimaryexpression;




    private alf_PostfixExpressionCompletion alf_postfixexpressioncompletion;


    public alf_PostfixOrCastExpression(
    ) {
        super(
        );
    }



    public alf_NameOrPrimaryExpression getAlf_nameorprimaryexpression() {
        return alf_nameorprimaryexpression;
    }

    public void setAlf_nameorprimaryexpression(alf_NameOrPrimaryExpression alf_nameorprimaryexpression) {
        this.alf_nameorprimaryexpression = alf_nameorprimaryexpression;
    }
    public alf_PostfixExpressionCompletion getAlf_postfixexpressioncompletion() {
        return alf_postfixexpressioncompletion;
    }

    public void setAlf_postfixexpressioncompletion(alf_PostfixExpressionCompletion alf_postfixexpressioncompletion) {
        this.alf_postfixexpressioncompletion = alf_postfixexpressioncompletion;
    }

}
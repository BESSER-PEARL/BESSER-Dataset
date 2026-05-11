





import java.util.List;
import java.util.ArrayList;

public class alf_NonNamePostfixOrCastExpression extends NonNameUnaryExpression {

    private boolean any;





    private alf_PostfixExpressionCompletion alf_postfixexpressioncompletion;




    private alf_NonNameExpression alf_nonnameexpression;




    private alf_BaseExpression alf_baseexpression;




    private alf_PostfixOrCastExpression alf_postfixorcastexpression;




    private alf_PostfixExpressionCompletion alf_postfixexpressioncompletion;




    private alf_QualifiedNameWithoutBinding alf_qualifiednamewithoutbinding;




    private alf_NameToExpressionCompletion alf_nametoexpressioncompletion;


    public alf_NonNamePostfixOrCastExpression(
        boolean any    ) {
        super(
        );
        this.any = any;
    }


    public boolean getAny() {
        return any;
    }

    public void setAny(boolean any) {
        this.any = any;
    }

    public alf_PostfixExpressionCompletion getAlf_postfixexpressioncompletion() {
        return alf_postfixexpressioncompletion;
    }

    public void setAlf_postfixexpressioncompletion(alf_PostfixExpressionCompletion alf_postfixexpressioncompletion) {
        this.alf_postfixexpressioncompletion = alf_postfixexpressioncompletion;
    }
    public alf_NonNameExpression getAlf_nonnameexpression() {
        return alf_nonnameexpression;
    }

    public void setAlf_nonnameexpression(alf_NonNameExpression alf_nonnameexpression) {
        this.alf_nonnameexpression = alf_nonnameexpression;
    }
    public alf_BaseExpression getAlf_baseexpression() {
        return alf_baseexpression;
    }

    public void setAlf_baseexpression(alf_BaseExpression alf_baseexpression) {
        this.alf_baseexpression = alf_baseexpression;
    }
    public alf_PostfixOrCastExpression getAlf_postfixorcastexpression() {
        return alf_postfixorcastexpression;
    }

    public void setAlf_postfixorcastexpression(alf_PostfixOrCastExpression alf_postfixorcastexpression) {
        this.alf_postfixorcastexpression = alf_postfixorcastexpression;
    }
    public alf_PostfixExpressionCompletion getAlf_postfixexpressioncompletion() {
        return alf_postfixexpressioncompletion;
    }

    public void setAlf_postfixexpressioncompletion(alf_PostfixExpressionCompletion alf_postfixexpressioncompletion) {
        this.alf_postfixexpressioncompletion = alf_postfixexpressioncompletion;
    }
    public alf_QualifiedNameWithoutBinding getAlf_qualifiednamewithoutbinding() {
        return alf_qualifiednamewithoutbinding;
    }

    public void setAlf_qualifiednamewithoutbinding(alf_QualifiedNameWithoutBinding alf_qualifiednamewithoutbinding) {
        this.alf_qualifiednamewithoutbinding = alf_qualifiednamewithoutbinding;
    }
    public alf_NameToExpressionCompletion getAlf_nametoexpressioncompletion() {
        return alf_nametoexpressioncompletion;
    }

    public void setAlf_nametoexpressioncompletion(alf_NameToExpressionCompletion alf_nametoexpressioncompletion) {
        this.alf_nametoexpressioncompletion = alf_nametoexpressioncompletion;
    }

}
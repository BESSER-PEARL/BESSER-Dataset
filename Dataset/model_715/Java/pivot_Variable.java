





import java.util.List;
import java.util.ArrayList;

public class pivot_Variable extends VariableDeclaration {

    private String isImplicit;





    private pivot_ExpressionInOCL pivot_expressioninocl;




    private pivot_OCLExpression pivot_oclexpression;




    private pivot_ExpressionInOCL pivot_expressioninocl;




    private pivot_LetExp pivot_letexp;




    private pivot_ExpressionInOCL pivot_expressioninocl;


    public pivot_Variable(
        String isImplicit    ) {
        super(
        );
        this.isImplicit = isImplicit;
    }


    public String getIsimplicit() {
        return isImplicit;
    }

    public void setIsimplicit(String isImplicit) {
        this.isImplicit = isImplicit;
    }

    public pivot_ExpressionInOCL getPivot_expressioninocl() {
        return pivot_expressioninocl;
    }

    public void setPivot_expressioninocl(pivot_ExpressionInOCL pivot_expressioninocl) {
        this.pivot_expressioninocl = pivot_expressioninocl;
    }
    public pivot_OCLExpression getPivot_oclexpression() {
        return pivot_oclexpression;
    }

    public void setPivot_oclexpression(pivot_OCLExpression pivot_oclexpression) {
        this.pivot_oclexpression = pivot_oclexpression;
    }
    public pivot_ExpressionInOCL getPivot_expressioninocl() {
        return pivot_expressioninocl;
    }

    public void setPivot_expressioninocl(pivot_ExpressionInOCL pivot_expressioninocl) {
        this.pivot_expressioninocl = pivot_expressioninocl;
    }
    public pivot_LetExp getPivot_letexp() {
        return pivot_letexp;
    }

    public void setPivot_letexp(pivot_LetExp pivot_letexp) {
        this.pivot_letexp = pivot_letexp;
    }
    public pivot_ExpressionInOCL getPivot_expressioninocl() {
        return pivot_expressioninocl;
    }

    public void setPivot_expressioninocl(pivot_ExpressionInOCL pivot_expressioninocl) {
        this.pivot_expressioninocl = pivot_expressioninocl;
    }

}
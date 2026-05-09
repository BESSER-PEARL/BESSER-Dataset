





import java.util.List;
import java.util.ArrayList;

public class pivot_Variable extends VariableDeclaration {

    private String implicit;





    private pivot_Parameter pivot_parameter;




    private pivot_IterateExp pivot_iterateexp;




    private pivot_ExpressionInOCL pivot_expressioninocl;




    private pivot_ExpressionInOCL pivot_expressioninocl;




    private pivot_ExpressionInOCL pivot_expressioninocl;




    private pivot_LetExp pivot_letexp;




    private pivot_LoopExp pivot_loopexp;


    public pivot_Variable(
        String implicit    ) {
        super(
        );
        this.implicit = implicit;
    }


    public String getImplicit() {
        return implicit;
    }

    public void setImplicit(String implicit) {
        this.implicit = implicit;
    }

    public pivot_Parameter getPivot_parameter() {
        return pivot_parameter;
    }

    public void setPivot_parameter(pivot_Parameter pivot_parameter) {
        this.pivot_parameter = pivot_parameter;
    }
    public pivot_IterateExp getPivot_iterateexp() {
        return pivot_iterateexp;
    }

    public void setPivot_iterateexp(pivot_IterateExp pivot_iterateexp) {
        this.pivot_iterateexp = pivot_iterateexp;
    }
    public pivot_ExpressionInOCL getPivot_expressioninocl() {
        return pivot_expressioninocl;
    }

    public void setPivot_expressioninocl(pivot_ExpressionInOCL pivot_expressioninocl) {
        this.pivot_expressioninocl = pivot_expressioninocl;
    }
    public pivot_ExpressionInOCL getPivot_expressioninocl() {
        return pivot_expressioninocl;
    }

    public void setPivot_expressioninocl(pivot_ExpressionInOCL pivot_expressioninocl) {
        this.pivot_expressioninocl = pivot_expressioninocl;
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
    public pivot_LoopExp getPivot_loopexp() {
        return pivot_loopexp;
    }

    public void setPivot_loopexp(pivot_LoopExp pivot_loopexp) {
        this.pivot_loopexp = pivot_loopexp;
    }

}
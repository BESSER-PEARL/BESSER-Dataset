





import java.util.List;
import java.util.ArrayList;

public class pivot_LetExp extends OCLExpression {






    private pivot_OCLExpression pivot_oclexpression;




    private pivot_Variable pivot_variable;


    public pivot_LetExp(
    ) {
        super(
        );
    }



    public pivot_OCLExpression getPivot_oclexpression() {
        return pivot_oclexpression;
    }

    public void setPivot_oclexpression(pivot_OCLExpression pivot_oclexpression) {
        this.pivot_oclexpression = pivot_oclexpression;
    }
    public pivot_Variable getPivot_variable() {
        return pivot_variable;
    }

    public void setPivot_variable(pivot_Variable pivot_variable) {
        this.pivot_variable = pivot_variable;
    }

}
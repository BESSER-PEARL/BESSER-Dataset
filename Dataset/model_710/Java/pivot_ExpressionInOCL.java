





import java.util.List;
import java.util.ArrayList;

public class pivot_ExpressionInOCL extends OpaqueExpression {






    private List<pivot_Variable> pivot_variables;




    private pivot_OCLExpression pivot_oclexpression;




    private pivot_Variable pivot_variable;




    private pivot_Variable pivot_variable;




    private pivot_OCLExpression pivot_oclexpression;


    public pivot_ExpressionInOCL(
    ) {
        super(
        );
        this.pivot_variables = new ArrayList<>();
    }

    public pivot_ExpressionInOCL(
        ArrayList<pivot_Variable> pivot_variables    ) {
        this.pivot_variables = pivot_variables;
    }


    public List<pivot_Variable> getPivot_variables() {
        return pivot_variables;
    }

    public void addPivot_variable(Pivot_variable pivot_variable) {
        this.pivot_variables.add(pivot_variable);
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
    public pivot_Variable getPivot_variable() {
        return pivot_variable;
    }

    public void setPivot_variable(pivot_Variable pivot_variable) {
        this.pivot_variable = pivot_variable;
    }
    public pivot_OCLExpression getPivot_oclexpression() {
        return pivot_oclexpression;
    }

    public void setPivot_oclexpression(pivot_OCLExpression pivot_oclexpression) {
        this.pivot_oclexpression = pivot_oclexpression;
    }

}






import java.util.List;
import java.util.ArrayList;

public class pivot_LoopExp extends CallExp {






    private pivot_OCLExpression pivot_oclexpression;




    private List<pivot_Variable> pivot_variables;


    public pivot_LoopExp(
    ) {
        super(
        );
        this.pivot_variables = new ArrayList<>();
    }

    public pivot_LoopExp(
        ArrayList<pivot_Variable> pivot_variables    ) {
        this.pivot_variables = pivot_variables;
    }


    public pivot_OCLExpression getPivot_oclexpression() {
        return pivot_oclexpression;
    }

    public void setPivot_oclexpression(pivot_OCLExpression pivot_oclexpression) {
        this.pivot_oclexpression = pivot_oclexpression;
    }
    public List<pivot_Variable> getPivot_variables() {
        return pivot_variables;
    }

    public void addPivot_variable(Pivot_variable pivot_variable) {
        this.pivot_variables.add(pivot_variable);
    }

}






import java.util.List;
import java.util.ArrayList;

public class JTLMM_essentialocl_LoopExp extends essentialocl_CallExp, essentialocl_OclExpression {






    private List<Variable> variables;




    private OclExpression oclexpression;


    public JTLMM_essentialocl_LoopExp(
    ) {
        super(
        );
        this.variables = new ArrayList<>();
    }

    public JTLMM_essentialocl_LoopExp(
        ArrayList<Variable> variables    ) {
        this.variables = variables;
    }


    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }
    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}
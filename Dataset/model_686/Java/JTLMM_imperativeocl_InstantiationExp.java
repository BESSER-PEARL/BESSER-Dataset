





import java.util.List;
import java.util.ArrayList;

public class JTLMM_imperativeocl_InstantiationExp extends ImperativeExpression {






    private List<OclExpression> oclexpressions;




    private Class class;




    private Variable variable;


    public JTLMM_imperativeocl_InstantiationExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public JTLMM_imperativeocl_InstantiationExp(
        ArrayList<OclExpression> oclexpressions    ) {
        this.oclexpressions = oclexpressions;
    }


    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }
    public Class getClass() {
        return class;
    }

    public void setClass(Class class) {
        this.class = class;
    }
    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }

}
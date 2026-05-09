





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_InstantiationExp extends ImperativeExpression {






    private Variable variable;




    private Class class;




    private List<OclExpression> oclexpressions;


    public ImperativeOCL_InstantiationExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public ImperativeOCL_InstantiationExp(
        ArrayList<OclExpression> oclexpressions    ) {
        this.oclexpressions = oclexpressions;
    }


    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }
    public Class getClass() {
        return class;
    }

    public void setClass(Class class) {
        this.class = class;
    }
    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }

}
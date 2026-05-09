





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_InstantiationExp extends ImperativeExpression {






    private Class class;




    private Variable variable;




    private List<OclExpression> oclexpressions;




    private Operation operation;


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
    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }
    public Operation getOperation() {
        return operation;
    }

    public void setOperation(Operation operation) {
        this.operation = operation;
    }

}
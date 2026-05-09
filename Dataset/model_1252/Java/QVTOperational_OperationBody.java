





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_OperationBody extends Element {






    private ImperativeOperation imperativeoperation;




    private List<OclExpression> oclexpressions;




    private List<Variable> variables;


    public QVTOperational_OperationBody(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
        this.variables = new ArrayList<>();
    }

    public QVTOperational_OperationBody(
        ArrayList<OclExpression> oclexpressions,        ArrayList<Variable> variables    ) {
        this.oclexpressions = oclexpressions;
        this.variables = variables;
    }


    public ImperativeOperation getImperativeoperation() {
        return imperativeoperation;
    }

    public void setImperativeoperation(ImperativeOperation imperativeoperation) {
        this.imperativeoperation = imperativeoperation;
    }
    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }
    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }

}
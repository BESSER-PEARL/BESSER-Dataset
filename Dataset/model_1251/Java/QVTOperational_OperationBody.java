





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_OperationBody extends Element {






    private List<OclExpression> oclexpressions;




    private ImperativeOperation imperativeoperation;


    public QVTOperational_OperationBody(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public QVTOperational_OperationBody(
        ArrayList<OclExpression> oclexpressions    ) {
        this.oclexpressions = oclexpressions;
    }


    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }
    public ImperativeOperation getImperativeoperation() {
        return imperativeoperation;
    }

    public void setImperativeoperation(ImperativeOperation imperativeoperation) {
        this.imperativeoperation = imperativeoperation;
    }

}
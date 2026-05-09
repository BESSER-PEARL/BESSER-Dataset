





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_OperationBody extends Element {






    private ImperativeOperation imperativeoperation;




    private List<qvtoperational_OCLExpression> qvtoperational_oclexpressions;


    public qvtoperational_OperationBody(
    ) {
        super(
        );
        this.qvtoperational_oclexpressions = new ArrayList<>();
    }

    public qvtoperational_OperationBody(
        ArrayList<qvtoperational_OCLExpression> qvtoperational_oclexpressions    ) {
        this.qvtoperational_oclexpressions = qvtoperational_oclexpressions;
    }


    public ImperativeOperation getImperativeoperation() {
        return imperativeoperation;
    }

    public void setImperativeoperation(ImperativeOperation imperativeoperation) {
        this.imperativeoperation = imperativeoperation;
    }
    public List<qvtoperational_OCLExpression> getQvtoperational_oclexpressions() {
        return qvtoperational_oclexpressions;
    }

    public void addQvtoperational_oclexpression(Qvtoperational_oclexpression qvtoperational_oclexpression) {
        this.qvtoperational_oclexpressions.add(qvtoperational_oclexpression);
    }

}
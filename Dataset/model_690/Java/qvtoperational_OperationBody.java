





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_OperationBody extends Element {






    private List<OclExpression> oclexpressions;


    public qvtoperational_OperationBody(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public qvtoperational_OperationBody(
        ArrayList<OclExpression> oclexpressions    ) {
        this.oclexpressions = oclexpressions;
    }


    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }

}
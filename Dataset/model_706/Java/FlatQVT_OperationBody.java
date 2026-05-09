





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_OperationBody extends Element {






    private List<OclExpression> oclexpressions;


    public FlatQVT_OperationBody(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public FlatQVT_OperationBody(
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
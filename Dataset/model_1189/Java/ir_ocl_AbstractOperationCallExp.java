





import java.util.List;
import java.util.ArrayList;

public class ir_ocl_AbstractOperationCallExp extends CallExp {






    private List<OclExpression> oclexpressions;


    public ir_ocl_AbstractOperationCallExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public ir_ocl_AbstractOperationCallExp(
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
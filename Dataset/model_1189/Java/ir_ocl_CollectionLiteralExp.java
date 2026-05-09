





import java.util.List;
import java.util.ArrayList;

public class ir_ocl_CollectionLiteralExp extends LiteralExp {






    private List<OclExpression> oclexpressions;


    public ir_ocl_CollectionLiteralExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public ir_ocl_CollectionLiteralExp(
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
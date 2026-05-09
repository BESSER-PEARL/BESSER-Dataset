





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_ListLiteralExp extends LiteralExp {






    private List<OclExpression> oclexpressions;


    public ImperativeOCL_ListLiteralExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public ImperativeOCL_ListLiteralExp(
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
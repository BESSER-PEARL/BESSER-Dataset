





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_ListLiteralExp extends LiteralExp {






    private List<OclExpression> oclexpressions;


    public FlatQVT_ListLiteralExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public FlatQVT_ListLiteralExp(
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
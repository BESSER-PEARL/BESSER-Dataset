





import java.util.List;
import java.util.ArrayList;

public class JTL_imperativeocl_AnonymousTupleLiteralPart extends Element {






    private List<OclExpression> oclexpressions;


    public JTL_imperativeocl_AnonymousTupleLiteralPart(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public JTL_imperativeocl_AnonymousTupleLiteralPart(
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
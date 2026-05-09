





import java.util.List;
import java.util.ArrayList;

public class imperativeocl_BlockExp extends ImperativeExpression {






    private List<OclExpression> oclexpressions;


    public imperativeocl_BlockExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public imperativeocl_BlockExp(
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
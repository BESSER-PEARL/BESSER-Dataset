





import java.util.List;
import java.util.ArrayList;

public class atlstatic_ATL_SimpleOutPatternElement extends OutPatternElement {






    private List<OclExpression> oclexpressions;


    public atlstatic_ATL_SimpleOutPatternElement(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public atlstatic_ATL_SimpleOutPatternElement(
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
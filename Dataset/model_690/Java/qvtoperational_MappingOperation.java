





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_MappingOperation extends Operation, NamedElement, ImperativeOperation {






    private List<OclExpression> oclexpressions;


    public qvtoperational_MappingOperation(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public qvtoperational_MappingOperation(
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
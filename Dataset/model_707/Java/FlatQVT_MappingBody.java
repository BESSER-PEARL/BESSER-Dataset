





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_MappingBody extends OperationBody {






    private List<OclExpression> oclexpressions;




    private List<OclExpression> oclexpressions;


    public FlatQVT_MappingBody(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
        this.oclexpressions = new ArrayList<>();
    }

    public FlatQVT_MappingBody(
        ArrayList<OclExpression> oclexpressions,        ArrayList<OclExpression> oclexpressions    ) {
        this.oclexpressions = oclexpressions;
        this.oclexpressions = oclexpressions;
    }


    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }
    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }

}
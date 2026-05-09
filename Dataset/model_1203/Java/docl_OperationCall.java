





import java.util.List;
import java.util.ArrayList;

public class docl_OperationCall extends OclExpression {






    private List<docl_OclExpression> docl_oclexpressions;


    public docl_OperationCall(
    ) {
        super(
        );
        this.docl_oclexpressions = new ArrayList<>();
    }

    public docl_OperationCall(
        ArrayList<docl_OclExpression> docl_oclexpressions    ) {
        this.docl_oclexpressions = docl_oclexpressions;
    }


    public List<docl_OclExpression> getDocl_oclexpressions() {
        return docl_oclexpressions;
    }

    public void addDocl_oclexpression(Docl_oclexpression docl_oclexpression) {
        this.docl_oclexpressions.add(docl_oclexpression);
    }

}
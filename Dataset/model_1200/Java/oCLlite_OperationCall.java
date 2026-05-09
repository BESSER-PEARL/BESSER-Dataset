





import java.util.List;
import java.util.ArrayList;

public class oCLlite_OperationCall extends OclLExpression {






    private List<oCLlite_OclLExpression> ocllite_ocllexpressions;


    public oCLlite_OperationCall(
    ) {
        super(
        );
        this.ocllite_ocllexpressions = new ArrayList<>();
    }

    public oCLlite_OperationCall(
        ArrayList<oCLlite_OclLExpression> ocllite_ocllexpressions    ) {
        this.ocllite_ocllexpressions = ocllite_ocllexpressions;
    }


    public List<oCLlite_OclLExpression> getOcllite_ocllexpressions() {
        return ocllite_ocllexpressions;
    }

    public void addOcllite_ocllexpression(Ocllite_ocllexpression ocllite_ocllexpression) {
        this.ocllite_ocllexpressions.add(ocllite_ocllexpression);
    }

}
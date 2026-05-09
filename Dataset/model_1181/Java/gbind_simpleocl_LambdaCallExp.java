





import java.util.List;
import java.util.ArrayList;

public class gbind_simpleocl_LambdaCallExp extends VariableExp {






    private List<OclExpression> oclexpressions;


    public gbind_simpleocl_LambdaCallExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public gbind_simpleocl_LambdaCallExp(
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
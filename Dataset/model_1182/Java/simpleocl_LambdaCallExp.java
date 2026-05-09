





import java.util.List;
import java.util.ArrayList;

public class simpleocl_LambdaCallExp extends VariableExp {






    private List<simpleocl_OclExpression> simpleocl_oclexpressions;


    public simpleocl_LambdaCallExp(
    ) {
        super(
        );
        this.simpleocl_oclexpressions = new ArrayList<>();
    }

    public simpleocl_LambdaCallExp(
        ArrayList<simpleocl_OclExpression> simpleocl_oclexpressions    ) {
        this.simpleocl_oclexpressions = simpleocl_oclexpressions;
    }


    public List<simpleocl_OclExpression> getSimpleocl_oclexpressions() {
        return simpleocl_oclexpressions;
    }

    public void addSimpleocl_oclexpression(Simpleocl_oclexpression simpleocl_oclexpression) {
        this.simpleocl_oclexpressions.add(simpleocl_oclexpression);
    }

}
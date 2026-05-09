





import java.util.List;
import java.util.ArrayList;

public class EmigOcl_LambdaCallExp extends VariableExp {






    private List<EmigOcl_OclExpression> emigocl_oclexpressions;


    public EmigOcl_LambdaCallExp(
    ) {
        super(
        );
        this.emigocl_oclexpressions = new ArrayList<>();
    }

    public EmigOcl_LambdaCallExp(
        ArrayList<EmigOcl_OclExpression> emigocl_oclexpressions    ) {
        this.emigocl_oclexpressions = emigocl_oclexpressions;
    }


    public List<EmigOcl_OclExpression> getEmigocl_oclexpressions() {
        return emigocl_oclexpressions;
    }

    public void addEmigocl_oclexpression(Emigocl_oclexpression emigocl_oclexpression) {
        this.emigocl_oclexpressions.add(emigocl_oclexpression);
    }

}
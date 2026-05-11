





import java.util.List;
import java.util.ArrayList;

public class operators_OperationCallExp extends OclExpression {

    private String name;





    private operators_OclExpression operators_oclexpression;




    private List<operators_OclExpression> operators_oclexpressions;


    public operators_OperationCallExp(
        String name    ) {
        super(
        );
        this.name = name;
        this.operators_oclexpressions = new ArrayList<>();
    }

    public operators_OperationCallExp(
        String name        ArrayList<operators_OclExpression> operators_oclexpressions    ) {
        this.name = name;
        this.operators_oclexpressions = operators_oclexpressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public operators_OclExpression getOperators_oclexpression() {
        return operators_oclexpression;
    }

    public void setOperators_oclexpression(operators_OclExpression operators_oclexpression) {
        this.operators_oclexpression = operators_oclexpression;
    }
    public List<operators_OclExpression> getOperators_oclexpressions() {
        return operators_oclexpressions;
    }

    public void addOperators_oclexpression(Operators_oclexpression operators_oclexpression) {
        this.operators_oclexpressions.add(operators_oclexpression);
    }

}
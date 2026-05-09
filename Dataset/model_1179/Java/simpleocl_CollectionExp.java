





import java.util.List;
import java.util.ArrayList;

public class simpleocl_CollectionExp extends OclExpression {






    private List<simpleocl_OclExpression> simpleocl_oclexpressions;




    private simpleocl_OclExpression simpleocl_oclexpression;


    public simpleocl_CollectionExp(
    ) {
        super(
        );
        this.simpleocl_oclexpressions = new ArrayList<>();
    }

    public simpleocl_CollectionExp(
        ArrayList<simpleocl_OclExpression> simpleocl_oclexpressions    ) {
        this.simpleocl_oclexpressions = simpleocl_oclexpressions;
    }


    public List<simpleocl_OclExpression> getSimpleocl_oclexpressions() {
        return simpleocl_oclexpressions;
    }

    public void addSimpleocl_oclexpression(Simpleocl_oclexpression simpleocl_oclexpression) {
        this.simpleocl_oclexpressions.add(simpleocl_oclexpression);
    }
    public simpleocl_OclExpression getSimpleocl_oclexpression() {
        return simpleocl_oclexpression;
    }

    public void setSimpleocl_oclexpression(simpleocl_OclExpression simpleocl_oclexpression) {
        this.simpleocl_oclexpression = simpleocl_oclexpression;
    }

}
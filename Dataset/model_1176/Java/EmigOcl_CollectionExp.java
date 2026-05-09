





import java.util.List;
import java.util.ArrayList;

public class EmigOcl_CollectionExp extends OclExpression {






    private List<EmigOcl_OclExpression> emigocl_oclexpressions;




    private EmigOcl_OclExpression emigocl_oclexpression;


    public EmigOcl_CollectionExp(
    ) {
        super(
        );
        this.emigocl_oclexpressions = new ArrayList<>();
    }

    public EmigOcl_CollectionExp(
        ArrayList<EmigOcl_OclExpression> emigocl_oclexpressions    ) {
        this.emigocl_oclexpressions = emigocl_oclexpressions;
    }


    public List<EmigOcl_OclExpression> getEmigocl_oclexpressions() {
        return emigocl_oclexpressions;
    }

    public void addEmigocl_oclexpression(Emigocl_oclexpression emigocl_oclexpression) {
        this.emigocl_oclexpressions.add(emigocl_oclexpression);
    }
    public EmigOcl_OclExpression getEmigocl_oclexpression() {
        return emigocl_oclexpression;
    }

    public void setEmigocl_oclexpression(EmigOcl_OclExpression emigocl_oclexpression) {
        this.emigocl_oclexpression = emigocl_oclexpression;
    }

}
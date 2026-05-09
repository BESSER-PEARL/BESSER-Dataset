





import java.util.List;
import java.util.ArrayList;

public class Janus_essentialocl_OperationCallExp extends FeaturePropertyCall {






    private Relation relation;




    private List<OclExpression> oclexpressions;


    public Janus_essentialocl_OperationCallExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public Janus_essentialocl_OperationCallExp(
        ArrayList<OclExpression> oclexpressions    ) {
        this.oclexpressions = oclexpressions;
    }


    public Relation getRelation() {
        return relation;
    }

    public void setRelation(Relation relation) {
        this.relation = relation;
    }
    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }

}
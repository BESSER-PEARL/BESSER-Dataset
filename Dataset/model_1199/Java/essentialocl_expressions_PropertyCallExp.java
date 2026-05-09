





import java.util.List;
import java.util.ArrayList;

public class essentialocl_expressions_PropertyCallExp extends FeatureCallExp {






    private List<OclExpression> oclexpressions;




    private expressions_essentialocl_Property expressions_essentialocl_property;


    public essentialocl_expressions_PropertyCallExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public essentialocl_expressions_PropertyCallExp(
        ArrayList<OclExpression> oclexpressions    ) {
        this.oclexpressions = oclexpressions;
    }


    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }
    public expressions_essentialocl_Property getExpressions_essentialocl_property() {
        return expressions_essentialocl_property;
    }

    public void setExpressions_essentialocl_property(expressions_essentialocl_Property expressions_essentialocl_property) {
        this.expressions_essentialocl_property = expressions_essentialocl_property;
    }

}
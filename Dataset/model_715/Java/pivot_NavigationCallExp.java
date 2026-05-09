





import java.util.List;
import java.util.ArrayList;

public class pivot_NavigationCallExp extends FeatureCallExp {






    private List<pivot_OCLExpression> pivot_oclexpressions;




    private pivot_Property pivot_property;


    public pivot_NavigationCallExp(
    ) {
        super(
        );
        this.pivot_oclexpressions = new ArrayList<>();
    }

    public pivot_NavigationCallExp(
        ArrayList<pivot_OCLExpression> pivot_oclexpressions    ) {
        this.pivot_oclexpressions = pivot_oclexpressions;
    }


    public List<pivot_OCLExpression> getPivot_oclexpressions() {
        return pivot_oclexpressions;
    }

    public void addPivot_oclexpression(Pivot_oclexpression pivot_oclexpression) {
        this.pivot_oclexpressions.add(pivot_oclexpression);
    }
    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
    }

}
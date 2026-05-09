





import java.util.List;
import java.util.ArrayList;

public class ocl_expressions_NavigationCallExp extends FeatureCallExp {






    private List<OCLExpression> oclexpressions;


    public ocl_expressions_NavigationCallExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public ocl_expressions_NavigationCallExp(
        ArrayList<OCLExpression> oclexpressions    ) {
        this.oclexpressions = oclexpressions;
    }


    public List<OCLExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }

}
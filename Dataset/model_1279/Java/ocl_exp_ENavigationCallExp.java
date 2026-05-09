





import java.util.List;
import java.util.ArrayList;

public class ocl_exp_ENavigationCallExp extends EFeatureCallExp {






    private List<EOclExpression> eoclexpressions;


    public ocl_exp_ENavigationCallExp(
    ) {
        super(
        );
        this.eoclexpressions = new ArrayList<>();
    }

    public ocl_exp_ENavigationCallExp(
        ArrayList<EOclExpression> eoclexpressions    ) {
        this.eoclexpressions = eoclexpressions;
    }


    public List<EOclExpression> getEoclexpressions() {
        return eoclexpressions;
    }

    public void addEoclexpression(Eoclexpression eoclexpression) {
        this.eoclexpressions.add(eoclexpression);
    }

}
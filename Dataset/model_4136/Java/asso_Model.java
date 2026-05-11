





import java.util.List;
import java.util.ArrayList;

public class asso_Model  {






    private List<asso_EvalExpression> asso_evalexpressions;


    public asso_Model(
    ) {
        this.asso_evalexpressions = new ArrayList<>();
    }

    public asso_Model(
        ArrayList<asso_EvalExpression> asso_evalexpressions    ) {
        this.asso_evalexpressions = asso_evalexpressions;
    }


    public List<asso_EvalExpression> getAsso_evalexpressions() {
        return asso_evalexpressions;
    }

    public void addAsso_evalexpression(Asso_evalexpression asso_evalexpression) {
        this.asso_evalexpressions.add(asso_evalexpression);
    }

}
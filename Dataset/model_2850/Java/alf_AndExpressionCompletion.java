





import java.util.List;
import java.util.ArrayList;

public class alf_AndExpressionCompletion  {






    private List<alf_EqualityExpression> alf_equalityexpressions;


    public alf_AndExpressionCompletion(
    ) {
        this.alf_equalityexpressions = new ArrayList<>();
    }

    public alf_AndExpressionCompletion(
        ArrayList<alf_EqualityExpression> alf_equalityexpressions    ) {
        this.alf_equalityexpressions = alf_equalityexpressions;
    }


    public List<alf_EqualityExpression> getAlf_equalityexpressions() {
        return alf_equalityexpressions;
    }

    public void addAlf_equalityexpression(Alf_equalityexpression alf_equalityexpression) {
        this.alf_equalityexpressions.add(alf_equalityexpression);
    }

}
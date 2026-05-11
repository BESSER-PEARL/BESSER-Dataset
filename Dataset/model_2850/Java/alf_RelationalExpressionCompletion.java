





import java.util.List;
import java.util.ArrayList;

public class alf_RelationalExpressionCompletion  {

    private String relationalOperator;





    private alf_RelationalExpression alf_relationalexpression;


    public alf_RelationalExpressionCompletion(
        String relationalOperator    ) {
        this.relationalOperator = relationalOperator;
    }


    public String getRelationaloperator() {
        return relationalOperator;
    }

    public void setRelationaloperator(String relationalOperator) {
        this.relationalOperator = relationalOperator;
    }

    public alf_RelationalExpression getAlf_relationalexpression() {
        return alf_relationalexpression;
    }

    public void setAlf_relationalexpression(alf_RelationalExpression alf_relationalexpression) {
        this.alf_relationalexpression = alf_relationalexpression;
    }

}
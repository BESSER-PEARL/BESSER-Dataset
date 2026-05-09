





import java.util.List;
import java.util.ArrayList;

public class gpfl_CondStmt extends GExpression {






    private List<gpfl_GExpression> gpfl_gexpressions;




    private gpfl_GExpression gpfl_gexpression;


    public gpfl_CondStmt(
    ) {
        super(
        );
        this.gpfl_gexpressions = new ArrayList<>();
    }

    public gpfl_CondStmt(
        ArrayList<gpfl_GExpression> gpfl_gexpressions    ) {
        this.gpfl_gexpressions = gpfl_gexpressions;
    }


    public List<gpfl_GExpression> getGpfl_gexpressions() {
        return gpfl_gexpressions;
    }

    public void addGpfl_gexpression(Gpfl_gexpression gpfl_gexpression) {
        this.gpfl_gexpressions.add(gpfl_gexpression);
    }
    public gpfl_GExpression getGpfl_gexpression() {
        return gpfl_gexpression;
    }

    public void setGpfl_gexpression(gpfl_GExpression gpfl_gexpression) {
        this.gpfl_gexpression = gpfl_gexpression;
    }

}
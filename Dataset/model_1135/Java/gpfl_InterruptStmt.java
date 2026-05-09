





import java.util.List;
import java.util.ArrayList;

public class gpfl_InterruptStmt extends GExpression {

    private int timeout;





    private gpfl_GExpression gpfl_gexpression;




    private List<gpfl_GExpression> gpfl_gexpressions;


    public gpfl_InterruptStmt(
        int timeout    ) {
        super(
        );
        this.timeout = timeout;
        this.gpfl_gexpressions = new ArrayList<>();
    }

    public gpfl_InterruptStmt(
        int timeout        ArrayList<gpfl_GExpression> gpfl_gexpressions    ) {
        this.timeout = timeout;
        this.gpfl_gexpressions = gpfl_gexpressions;
    }

    public int getTimeout() {
        return timeout;
    }

    public void setTimeout(int timeout) {
        this.timeout = timeout;
    }

    public gpfl_GExpression getGpfl_gexpression() {
        return gpfl_gexpression;
    }

    public void setGpfl_gexpression(gpfl_GExpression gpfl_gexpression) {
        this.gpfl_gexpression = gpfl_gexpression;
    }
    public List<gpfl_GExpression> getGpfl_gexpressions() {
        return gpfl_gexpressions;
    }

    public void addGpfl_gexpression(Gpfl_gexpression gpfl_gexpression) {
        this.gpfl_gexpressions.add(gpfl_gexpression);
    }

}






import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsViewExpressionField extends RdbmsViewField {

    private String expression;





    private List<rdbms_RdbmsExpression> rdbms_rdbmsexpressions;


    public rdbms_RdbmsViewExpressionField(
        String expression    ) {
        super(
        );
        this.expression = expression;
        this.rdbms_rdbmsexpressions = new ArrayList<>();
    }

    public rdbms_RdbmsViewExpressionField(
        String expression        ArrayList<rdbms_RdbmsExpression> rdbms_rdbmsexpressions    ) {
        this.expression = expression;
        this.rdbms_rdbmsexpressions = rdbms_rdbmsexpressions;
    }

    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public List<rdbms_RdbmsExpression> getRdbms_rdbmsexpressions() {
        return rdbms_rdbmsexpressions;
    }

    public void addRdbms_rdbmsexpression(Rdbms_rdbmsexpression rdbms_rdbmsexpression) {
        this.rdbms_rdbmsexpressions.add(rdbms_rdbmsexpression);
    }

}
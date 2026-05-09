





import java.util.List;
import java.util.ArrayList;

public class ACG_ReportStat extends Statement {

    private String severity;





    private Expression expression;


    public ACG_ReportStat(
        String severity    ) {
        super(
        );
        this.severity = severity;
    }


    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}
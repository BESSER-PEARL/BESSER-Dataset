





import java.util.List;
import java.util.ArrayList;

public class JTL_imperativeocl_AssertExp extends ImperativeExpression {

    private String severity;





    private OclExpression oclexpression;


    public JTL_imperativeocl_AssertExp(
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

    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}
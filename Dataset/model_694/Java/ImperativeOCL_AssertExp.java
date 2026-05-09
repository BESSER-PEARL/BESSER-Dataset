





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_AssertExp extends ImperativeExpression {

    private String severity;





    private OclExpression oclexpression;


    public ImperativeOCL_AssertExp(
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
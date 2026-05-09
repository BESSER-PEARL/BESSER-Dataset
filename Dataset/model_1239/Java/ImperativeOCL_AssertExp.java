





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_AssertExp extends ImperativeExpression {

    private String severity;





    private LogExp logexp;


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

    public LogExp getLogexp() {
        return logexp;
    }

    public void setLogexp(LogExp logexp) {
        this.logexp = logexp;
    }

}
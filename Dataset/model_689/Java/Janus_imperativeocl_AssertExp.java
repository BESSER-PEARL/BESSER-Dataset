





import java.util.List;
import java.util.ArrayList;

public class Janus_imperativeocl_AssertExp extends ImperativeExpression {

    private String severity;



    public Janus_imperativeocl_AssertExp(
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


}
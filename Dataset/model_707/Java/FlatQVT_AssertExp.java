





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_AssertExp extends ImperativeExpression {

    private String severity;



    public FlatQVT_AssertExp(
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
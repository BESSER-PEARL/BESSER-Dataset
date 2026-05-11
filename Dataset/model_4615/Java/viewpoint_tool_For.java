





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_For extends ContainerModelOperation {

    private String iteratorName;
    private String expression;



    public viewpoint_tool_For(
        String iteratorName,        String expression    ) {
        super(
        );
        this.iteratorName = iteratorName;
        this.expression = expression;
    }


    public String getIteratorname() {
        return iteratorName;
    }

    public void setIteratorname(String iteratorName) {
        this.iteratorName = iteratorName;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }


}
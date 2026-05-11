





import java.util.List;
import java.util.ArrayList;

public class diagraph_DLabeledElement extends DGraphElement {

    private String expression;
    private String labls;



    public diagraph_DLabeledElement(
        String expression,        String labls    ) {
        super(
        );
        this.expression = expression;
        this.labls = labls;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getLabls() {
        return labls;
    }

    public void setLabls(String labls) {
        this.labls = labls;
    }


}
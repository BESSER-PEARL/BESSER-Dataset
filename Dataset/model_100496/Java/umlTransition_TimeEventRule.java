





import java.util.List;
import java.util.ArrayList;

public class umlTransition_TimeEventRule extends EventRule {

    private String expr;



    public umlTransition_TimeEventRule(
        String expr    ) {
        super(
        );
        this.expr = expr;
    }


    public String getExpr() {
        return expr;
    }

    public void setExpr(String expr) {
        this.expr = expr;
    }


}
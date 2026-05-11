





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_core_Location extends core_TAElement, Position {

    private String committed;
    private String urgent;





    private expressions_Expression expressions_expression;


    public timedAutomata_core_Location(
        String committed,        String urgent    ) {
        super(
        );
        this.committed = committed;
        this.urgent = urgent;
    }


    public String getCommitted() {
        return committed;
    }

    public void setCommitted(String committed) {
        this.committed = committed;
    }
    public String getUrgent() {
        return urgent;
    }

    public void setUrgent(String urgent) {
        this.urgent = urgent;
    }

    public expressions_Expression getExpressions_expression() {
        return expressions_expression;
    }

    public void setExpressions_expression(expressions_Expression expressions_expression) {
        this.expressions_expression = expressions_expression;
    }

}






import java.util.List;
import java.util.ArrayList;

public class statemachine_Transition  {

    private int priority;
    private int id;
    private String expression;





    private statemachine_Node statemachine_node;




    private statemachine_Node statemachine_node;


    public statemachine_Transition(
        int priority,        int id,        String expression    ) {
        this.priority = priority;
        this.id = id;
        this.expression = expression;
    }


    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public statemachine_Node getStatemachine_node() {
        return statemachine_node;
    }

    public void setStatemachine_node(statemachine_Node statemachine_node) {
        this.statemachine_node = statemachine_node;
    }
    public statemachine_Node getStatemachine_node() {
        return statemachine_node;
    }

    public void setStatemachine_node(statemachine_Node statemachine_node) {
        this.statemachine_node = statemachine_node;
    }

}
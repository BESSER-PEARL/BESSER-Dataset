





import java.util.List;
import java.util.ArrayList;

public class behaviour_FunctionCall extends Expression {

    private String funcName;





    private List<behaviour_Expression> behaviour_expressions;


    public behaviour_FunctionCall(
        String funcName    ) {
        super(
        );
        this.funcName = funcName;
        this.behaviour_expressions = new ArrayList<>();
    }

    public behaviour_FunctionCall(
        String funcName        ArrayList<behaviour_Expression> behaviour_expressions    ) {
        this.funcName = funcName;
        this.behaviour_expressions = behaviour_expressions;
    }

    public String getFuncname() {
        return funcName;
    }

    public void setFuncname(String funcName) {
        this.funcName = funcName;
    }

    public List<behaviour_Expression> getBehaviour_expressions() {
        return behaviour_expressions;
    }

    public void addBehaviour_expression(Behaviour_expression behaviour_expression) {
        this.behaviour_expressions.add(behaviour_expression);
    }

}
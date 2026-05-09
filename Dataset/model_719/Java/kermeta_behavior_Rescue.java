





import java.util.List;
import java.util.ArrayList;

public class kermeta_behavior_Rescue extends Object {

    private String exceptionName;





    private List<behavior_Expression> behavior_expressions;


    public kermeta_behavior_Rescue(
        String exceptionName    ) {
        super(
        );
        this.exceptionName = exceptionName;
        this.behavior_expressions = new ArrayList<>();
    }

    public kermeta_behavior_Rescue(
        String exceptionName        ArrayList<behavior_Expression> behavior_expressions    ) {
        this.exceptionName = exceptionName;
        this.behavior_expressions = behavior_expressions;
    }

    public String getExceptionname() {
        return exceptionName;
    }

    public void setExceptionname(String exceptionName) {
        this.exceptionName = exceptionName;
    }

    public List<behavior_Expression> getBehavior_expressions() {
        return behavior_expressions;
    }

    public void addBehavior_expression(Behavior_expression behavior_expression) {
        this.behavior_expressions.add(behavior_expression);
    }

}
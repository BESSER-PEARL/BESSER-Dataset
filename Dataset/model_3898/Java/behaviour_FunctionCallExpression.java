





import java.util.List;
import java.util.ArrayList;

public class behaviour_FunctionCallExpression extends Expression {






    private List<behaviour_VariableClass> behaviour_variableclasss;


    public behaviour_FunctionCallExpression(
    ) {
        super(
        );
        this.behaviour_variableclasss = new ArrayList<>();
    }

    public behaviour_FunctionCallExpression(
        ArrayList<behaviour_VariableClass> behaviour_variableclasss    ) {
        this.behaviour_variableclasss = behaviour_variableclasss;
    }


    public List<behaviour_VariableClass> getBehaviour_variableclasss() {
        return behaviour_variableclasss;
    }

    public void addBehaviour_variableclass(Behaviour_variableclass behaviour_variableclass) {
        this.behaviour_variableclasss.add(behaviour_variableclass);
    }

}






import java.util.List;
import java.util.ArrayList;

public class behaviour_Move extends PrimitiveActivity {






    private List<behaviour_Expression> behaviour_expressions;


    public behaviour_Move(
    ) {
        super(
        );
        this.behaviour_expressions = new ArrayList<>();
    }

    public behaviour_Move(
        ArrayList<behaviour_Expression> behaviour_expressions    ) {
        this.behaviour_expressions = behaviour_expressions;
    }


    public List<behaviour_Expression> getBehaviour_expressions() {
        return behaviour_expressions;
    }

    public void addBehaviour_expression(Behaviour_expression behaviour_expression) {
        this.behaviour_expressions.add(behaviour_expression);
    }

}
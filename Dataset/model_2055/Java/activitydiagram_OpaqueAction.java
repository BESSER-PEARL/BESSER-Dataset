





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_OpaqueAction extends Action {






    private List<activitydiagram_Expression> activitydiagram_expressions;


    public activitydiagram_OpaqueAction(
    ) {
        super(
        );
        this.activitydiagram_expressions = new ArrayList<>();
    }

    public activitydiagram_OpaqueAction(
        ArrayList<activitydiagram_Expression> activitydiagram_expressions    ) {
        this.activitydiagram_expressions = activitydiagram_expressions;
    }


    public List<activitydiagram_Expression> getActivitydiagram_expressions() {
        return activitydiagram_expressions;
    }

    public void addActivitydiagram_expression(Activitydiagram_expression activitydiagram_expression) {
        this.activitydiagram_expressions.add(activitydiagram_expression);
    }

}
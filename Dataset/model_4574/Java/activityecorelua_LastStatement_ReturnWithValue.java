





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_LastStatement_ReturnWithValue extends LastStatement_Return {






    private List<activityecorelua_Expression> activityecorelua_expressions;


    public activityecorelua_LastStatement_ReturnWithValue(
    ) {
        super(
        );
        this.activityecorelua_expressions = new ArrayList<>();
    }

    public activityecorelua_LastStatement_ReturnWithValue(
        ArrayList<activityecorelua_Expression> activityecorelua_expressions    ) {
        this.activityecorelua_expressions = activityecorelua_expressions;
    }


    public List<activityecorelua_Expression> getActivityecorelua_expressions() {
        return activityecorelua_expressions;
    }

    public void addActivityecorelua_expression(Activityecorelua_expression activityecorelua_expression) {
        this.activityecorelua_expressions.add(activityecorelua_expression);
    }

}
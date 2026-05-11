





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_Statement_Local_Variable_Declaration extends Statement {

    private String variableNames;





    private List<activityecorelua_Expression> activityecorelua_expressions;


    public activityecorelua_Statement_Local_Variable_Declaration(
        String variableNames    ) {
        super(
        );
        this.variableNames = variableNames;
        this.activityecorelua_expressions = new ArrayList<>();
    }

    public activityecorelua_Statement_Local_Variable_Declaration(
        String variableNames        ArrayList<activityecorelua_Expression> activityecorelua_expressions    ) {
        this.variableNames = variableNames;
        this.activityecorelua_expressions = activityecorelua_expressions;
    }

    public String getVariablenames() {
        return variableNames;
    }

    public void setVariablenames(String variableNames) {
        this.variableNames = variableNames;
    }

    public List<activityecorelua_Expression> getActivityecorelua_expressions() {
        return activityecorelua_expressions;
    }

    public void addActivityecorelua_expression(Activityecorelua_expression activityecorelua_expression) {
        this.activityecorelua_expressions.add(activityecorelua_expression);
    }

}
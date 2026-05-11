





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_Statement_For_Generic extends Statement {

    private String names;





    private List<activityecorelua_Expression> activityecorelua_expressions;


    public activityecorelua_Statement_For_Generic(
        String names    ) {
        super(
        );
        this.names = names;
        this.activityecorelua_expressions = new ArrayList<>();
    }

    public activityecorelua_Statement_For_Generic(
        String names        ArrayList<activityecorelua_Expression> activityecorelua_expressions    ) {
        this.names = names;
        this.activityecorelua_expressions = activityecorelua_expressions;
    }

    public String getNames() {
        return names;
    }

    public void setNames(String names) {
        this.names = names;
    }

    public List<activityecorelua_Expression> getActivityecorelua_expressions() {
        return activityecorelua_expressions;
    }

    public void addActivityecorelua_expression(Activityecorelua_expression activityecorelua_expression) {
        this.activityecorelua_expressions.add(activityecorelua_expression);
    }

}
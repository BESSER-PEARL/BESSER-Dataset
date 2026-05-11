





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_TableView extends View {

    private String style;





    private applauseDsl_ScalarExpression applausedsl_scalarexpression;




    private applauseDsl_ScalarExpression applausedsl_scalarexpression;




    private List<applauseDsl_Parameter> applausedsl_parameters;


    public applauseDsl_TableView(
        String style    ) {
        super(
        );
        this.style = style;
        this.applausedsl_parameters = new ArrayList<>();
    }

    public applauseDsl_TableView(
        String style        ArrayList<applauseDsl_Parameter> applausedsl_parameters    ) {
        this.style = style;
        this.applausedsl_parameters = applausedsl_parameters;
    }

    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }

    public applauseDsl_ScalarExpression getApplausedsl_scalarexpression() {
        return applausedsl_scalarexpression;
    }

    public void setApplausedsl_scalarexpression(applauseDsl_ScalarExpression applausedsl_scalarexpression) {
        this.applausedsl_scalarexpression = applausedsl_scalarexpression;
    }
    public applauseDsl_ScalarExpression getApplausedsl_scalarexpression() {
        return applausedsl_scalarexpression;
    }

    public void setApplausedsl_scalarexpression(applauseDsl_ScalarExpression applausedsl_scalarexpression) {
        this.applausedsl_scalarexpression = applausedsl_scalarexpression;
    }
    public List<applauseDsl_Parameter> getApplausedsl_parameters() {
        return applausedsl_parameters;
    }

    public void addApplausedsl_parameter(Applausedsl_parameter applausedsl_parameter) {
        this.applausedsl_parameters.add(applausedsl_parameter);
    }

}
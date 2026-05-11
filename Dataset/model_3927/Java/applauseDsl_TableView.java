





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_TableView extends View {

    private String style;





    private applauseDsl_ScalarExpression applausedsl_scalarexpression;




    private List<applauseDsl_Parameter> applausedsl_parameters;




    private applauseDsl_ScalarExpression applausedsl_scalarexpression;




    private List<applauseDsl_Section> applausedsl_sections;


    public applauseDsl_TableView(
        String style    ) {
        super(
        );
        this.style = style;
        this.applausedsl_parameters = new ArrayList<>();
        this.applausedsl_sections = new ArrayList<>();
    }

    public applauseDsl_TableView(
        String style        ArrayList<applauseDsl_Parameter> applausedsl_parameters,        ArrayList<applauseDsl_Section> applausedsl_sections    ) {
        this.style = style;
        this.applausedsl_parameters = applausedsl_parameters;
        this.applausedsl_sections = applausedsl_sections;
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
    public List<applauseDsl_Parameter> getApplausedsl_parameters() {
        return applausedsl_parameters;
    }

    public void addApplausedsl_parameter(Applausedsl_parameter applausedsl_parameter) {
        this.applausedsl_parameters.add(applausedsl_parameter);
    }
    public applauseDsl_ScalarExpression getApplausedsl_scalarexpression() {
        return applausedsl_scalarexpression;
    }

    public void setApplausedsl_scalarexpression(applauseDsl_ScalarExpression applausedsl_scalarexpression) {
        this.applausedsl_scalarexpression = applausedsl_scalarexpression;
    }
    public List<applauseDsl_Section> getApplausedsl_sections() {
        return applausedsl_sections;
    }

    public void addApplausedsl_section(Applausedsl_section applausedsl_section) {
        this.applausedsl_sections.add(applausedsl_section);
    }

}
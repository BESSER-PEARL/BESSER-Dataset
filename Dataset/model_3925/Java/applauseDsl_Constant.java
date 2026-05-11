





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_Constant extends VariableDeclaration {

    private String language;





    private List<applauseDsl_ScalarExpression> applausedsl_scalarexpressions;


    public applauseDsl_Constant(
        String language    ) {
        super(
        );
        this.language = language;
        this.applausedsl_scalarexpressions = new ArrayList<>();
    }

    public applauseDsl_Constant(
        String language        ArrayList<applauseDsl_ScalarExpression> applausedsl_scalarexpressions    ) {
        this.language = language;
        this.applausedsl_scalarexpressions = applausedsl_scalarexpressions;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public List<applauseDsl_ScalarExpression> getApplausedsl_scalarexpressions() {
        return applausedsl_scalarexpressions;
    }

    public void addApplausedsl_scalarexpression(Applausedsl_scalarexpression applausedsl_scalarexpression) {
        this.applausedsl_scalarexpressions.add(applausedsl_scalarexpression);
    }

}
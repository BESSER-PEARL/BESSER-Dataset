





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_View extends ModelElement {

    private String name;





    private List<applauseDsl_VariableDeclaration> applausedsl_variabledeclarations;


    public applauseDsl_View(
        String name    ) {
        super(
        );
        this.name = name;
        this.applausedsl_variabledeclarations = new ArrayList<>();
    }

    public applauseDsl_View(
        String name        ArrayList<applauseDsl_VariableDeclaration> applausedsl_variabledeclarations    ) {
        this.name = name;
        this.applausedsl_variabledeclarations = applausedsl_variabledeclarations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<applauseDsl_VariableDeclaration> getApplausedsl_variabledeclarations() {
        return applausedsl_variabledeclarations;
    }

    public void addApplausedsl_variabledeclaration(Applausedsl_variabledeclaration applausedsl_variabledeclaration) {
        this.applausedsl_variabledeclarations.add(applausedsl_variabledeclaration);
    }

}






import java.util.List;
import java.util.ArrayList;

public class core_saflet_SafletContext extends ThreadSensitive {

    private String exceptions;
    private String sessionVariables;





    private List<saflet_core_Variable> saflet_core_variables;


    public core_saflet_SafletContext(
        String exceptions,        String sessionVariables    ) {
        super(
        );
        this.exceptions = exceptions;
        this.sessionVariables = sessionVariables;
        this.saflet_core_variables = new ArrayList<>();
    }

    public core_saflet_SafletContext(
        String exceptions,        String sessionVariables        ArrayList<saflet_core_Variable> saflet_core_variables    ) {
        this.exceptions = exceptions;
        this.sessionVariables = sessionVariables;
        this.saflet_core_variables = saflet_core_variables;
    }

    public String getExceptions() {
        return exceptions;
    }

    public void setExceptions(String exceptions) {
        this.exceptions = exceptions;
    }
    public String getSessionvariables() {
        return sessionVariables;
    }

    public void setSessionvariables(String sessionVariables) {
        this.sessionVariables = sessionVariables;
    }

    public List<saflet_core_Variable> getSaflet_core_variables() {
        return saflet_core_variables;
    }

    public void addSaflet_core_variable(Saflet_core_variable saflet_core_variable) {
        this.saflet_core_variables.add(saflet_core_variable);
    }

}
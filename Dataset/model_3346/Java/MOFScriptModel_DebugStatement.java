





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_DebugStatement extends MOFScriptStatement {

    private String vars;
    private String specification;



    public MOFScriptModel_DebugStatement(
        String vars,        String specification    ) {
        super(
        );
        this.vars = vars;
        this.specification = specification;
    }


    public String getVars() {
        return vars;
    }

    public void setVars(String vars) {
        this.vars = vars;
    }
    public String getSpecification() {
        return specification;
    }

    public void setSpecification(String specification) {
        this.specification = specification;
    }


}
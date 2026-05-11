





import java.util.List;
import java.util.ArrayList;

public class go_AtribVar  {

    private String type;
    private String vars;





    private go_DecVar go_decvar;


    public go_AtribVar(
        String type,        String vars    ) {
        this.type = type;
        this.vars = vars;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getVars() {
        return vars;
    }

    public void setVars(String vars) {
        this.vars = vars;
    }

    public go_DecVar getGo_decvar() {
        return go_decvar;
    }

    public void setGo_decvar(go_DecVar go_decvar) {
        this.go_decvar = go_decvar;
    }

}
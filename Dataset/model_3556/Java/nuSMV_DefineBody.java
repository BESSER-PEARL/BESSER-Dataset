





import java.util.List;
import java.util.ArrayList;

public class nuSMV_DefineBody  {

    private boolean semicolon;
    private String var;





    private nuSMV_DefineDeclaration nusmv_definedeclaration;


    public nuSMV_DefineBody(
        boolean semicolon,        String var    ) {
        this.semicolon = semicolon;
        this.var = var;
    }


    public boolean getSemicolon() {
        return semicolon;
    }

    public void setSemicolon(boolean semicolon) {
        this.semicolon = semicolon;
    }
    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }

    public nuSMV_DefineDeclaration getNusmv_definedeclaration() {
        return nusmv_definedeclaration;
    }

    public void setNusmv_definedeclaration(nuSMV_DefineDeclaration nusmv_definedeclaration) {
        this.nusmv_definedeclaration = nusmv_definedeclaration;
    }

}
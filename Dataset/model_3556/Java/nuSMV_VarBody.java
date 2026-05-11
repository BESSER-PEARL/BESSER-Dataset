





import java.util.List;
import java.util.ArrayList;

public class nuSMV_VarBody  {

    private boolean semicolon;
    private String name;





    private nuSMV_IVariableDeclaration nusmv_ivariabledeclaration;




    private nuSMV_FrozenVariableDeclaration nusmv_frozenvariabledeclaration;




    private nuSMV_VariableDeclaration nusmv_variabledeclaration;


    public nuSMV_VarBody(
        boolean semicolon,        String name    ) {
        this.semicolon = semicolon;
        this.name = name;
    }


    public boolean getSemicolon() {
        return semicolon;
    }

    public void setSemicolon(boolean semicolon) {
        this.semicolon = semicolon;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public nuSMV_IVariableDeclaration getNusmv_ivariabledeclaration() {
        return nusmv_ivariabledeclaration;
    }

    public void setNusmv_ivariabledeclaration(nuSMV_IVariableDeclaration nusmv_ivariabledeclaration) {
        this.nusmv_ivariabledeclaration = nusmv_ivariabledeclaration;
    }
    public nuSMV_FrozenVariableDeclaration getNusmv_frozenvariabledeclaration() {
        return nusmv_frozenvariabledeclaration;
    }

    public void setNusmv_frozenvariabledeclaration(nuSMV_FrozenVariableDeclaration nusmv_frozenvariabledeclaration) {
        this.nusmv_frozenvariabledeclaration = nusmv_frozenvariabledeclaration;
    }
    public nuSMV_VariableDeclaration getNusmv_variabledeclaration() {
        return nusmv_variabledeclaration;
    }

    public void setNusmv_variabledeclaration(nuSMV_VariableDeclaration nusmv_variabledeclaration) {
        this.nusmv_variabledeclaration = nusmv_variabledeclaration;
    }

}
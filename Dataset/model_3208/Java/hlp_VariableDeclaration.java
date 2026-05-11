





import java.util.List;
import java.util.ArrayList;

public class hlp_VariableDeclaration  {






    private hlp_Variable hlp_variable;




    private hlp_VariableDeclarationScope hlp_variabledeclarationscope;


    public hlp_VariableDeclaration(
    ) {
    }



    public hlp_Variable getHlp_variable() {
        return hlp_variable;
    }

    public void setHlp_variable(hlp_Variable hlp_variable) {
        this.hlp_variable = hlp_variable;
    }
    public hlp_VariableDeclarationScope getHlp_variabledeclarationscope() {
        return hlp_variabledeclarationscope;
    }

    public void setHlp_variabledeclarationscope(hlp_VariableDeclarationScope hlp_variabledeclarationscope) {
        this.hlp_variabledeclarationscope = hlp_variabledeclarationscope;
    }

}






import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppVariableDeclaration extends CppNamedElement {

    private String vartype;
    private boolean isArray;



    public Metamodelo_Cpp_CppVariableDeclaration(
        String vartype,        boolean isArray    ) {
        super(
        );
        this.vartype = vartype;
        this.isArray = isArray;
    }


    public String getVartype() {
        return vartype;
    }

    public void setVartype(String vartype) {
        this.vartype = vartype;
    }
    public boolean getIsarray() {
        return isArray;
    }

    public void setIsarray(boolean isArray) {
        this.isArray = isArray;
    }


}
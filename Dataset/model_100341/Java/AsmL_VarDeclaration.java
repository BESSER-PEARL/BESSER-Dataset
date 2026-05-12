





import java.util.List;
import java.util.ArrayList;

public class AsmL_VarDeclaration extends VarOrCase, AsmLElement, VarOrMethod {

    private String isConstant;
    private String name;
    private String isDeclaration;
    private String isLocal;



    public AsmL_VarDeclaration(
        String isConstant,        String name,        String isDeclaration,        String isLocal    ) {
        super(
        );
        this.isConstant = isConstant;
        this.name = name;
        this.isDeclaration = isDeclaration;
        this.isLocal = isLocal;
    }


    public String getIsconstant() {
        return isConstant;
    }

    public void setIsconstant(String isConstant) {
        this.isConstant = isConstant;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIsdeclaration() {
        return isDeclaration;
    }

    public void setIsdeclaration(String isDeclaration) {
        this.isDeclaration = isDeclaration;
    }
    public String getIslocal() {
        return isLocal;
    }

    public void setIslocal(String isLocal) {
        this.isLocal = isLocal;
    }


}






import java.util.List;
import java.util.ArrayList;

public class gbind_simpleocl_VariableDeclaration extends LocatedElement {

    private String varName;





    private OclType ocltype;


    public gbind_simpleocl_VariableDeclaration(
        String varName    ) {
        super(
        );
        this.varName = varName;
    }


    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }

    public OclType getOcltype() {
        return ocltype;
    }

    public void setOcltype(OclType ocltype) {
        this.ocltype = ocltype;
    }

}






import java.util.List;
import java.util.ArrayList;

public class OCL_VariableDeclaration extends LocatedElement {

    private String varName;
    private String id;





    private OclType ocltype;




    private LetExp letexp;


    public OCL_VariableDeclaration(
        String varName,        String id    ) {
        super(
        );
        this.varName = varName;
        this.id = id;
    }


    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public OclType getOcltype() {
        return ocltype;
    }

    public void setOcltype(OclType ocltype) {
        this.ocltype = ocltype;
    }
    public LetExp getLetexp() {
        return letexp;
    }

    public void setLetexp(LetExp letexp) {
        this.letexp = letexp;
    }

}
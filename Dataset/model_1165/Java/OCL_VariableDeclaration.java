





import java.util.List;
import java.util.ArrayList;

public class OCL_VariableDeclaration extends LocatedElement {

    private String id;
    private String varName;





    private IterateExp iterateexp;




    private LetExp letexp;




    private List<VariableExp> variableexps;




    private OclType ocltype;


    public OCL_VariableDeclaration(
        String id,        String varName    ) {
        super(
        );
        this.id = id;
        this.varName = varName;
        this.variableexps = new ArrayList<>();
    }

    public OCL_VariableDeclaration(
        String id,        String varName        ArrayList<VariableExp> variableexps    ) {
        this.id = id;
        this.varName = varName;
        this.variableexps = variableexps;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }

    public IterateExp getIterateexp() {
        return iterateexp;
    }

    public void setIterateexp(IterateExp iterateexp) {
        this.iterateexp = iterateexp;
    }
    public LetExp getLetexp() {
        return letexp;
    }

    public void setLetexp(LetExp letexp) {
        this.letexp = letexp;
    }
    public List<VariableExp> getVariableexps() {
        return variableexps;
    }

    public void addVariableexp(Variableexp variableexp) {
        this.variableexps.add(variableexp);
    }
    public OclType getOcltype() {
        return ocltype;
    }

    public void setOcltype(OclType ocltype) {
        this.ocltype = ocltype;
    }

}
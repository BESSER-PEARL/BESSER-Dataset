





import java.util.List;
import java.util.ArrayList;

public class JDTAST_SingleVariableDeclaration extends VariableDeclaration {

    private String varargs;





    private JDTAST_CatchClause jdtast_catchclause;




    private List<JDTAST_ExtendedModifier> jdtast_extendedmodifiers;




    private JDTAST_Type jdtast_type;


    public JDTAST_SingleVariableDeclaration(
        String varargs    ) {
        super(
        );
        this.varargs = varargs;
        this.jdtast_extendedmodifiers = new ArrayList<>();
    }

    public JDTAST_SingleVariableDeclaration(
        String varargs        ArrayList<JDTAST_ExtendedModifier> jdtast_extendedmodifiers    ) {
        this.varargs = varargs;
        this.jdtast_extendedmodifiers = jdtast_extendedmodifiers;
    }

    public String getVarargs() {
        return varargs;
    }

    public void setVarargs(String varargs) {
        this.varargs = varargs;
    }

    public JDTAST_CatchClause getJdtast_catchclause() {
        return jdtast_catchclause;
    }

    public void setJdtast_catchclause(JDTAST_CatchClause jdtast_catchclause) {
        this.jdtast_catchclause = jdtast_catchclause;
    }
    public List<JDTAST_ExtendedModifier> getJdtast_extendedmodifiers() {
        return jdtast_extendedmodifiers;
    }

    public void addJdtast_extendedmodifier(Jdtast_extendedmodifier jdtast_extendedmodifier) {
        this.jdtast_extendedmodifiers.add(jdtast_extendedmodifier);
    }
    public JDTAST_Type getJdtast_type() {
        return jdtast_type;
    }

    public void setJdtast_type(JDTAST_Type jdtast_type) {
        this.jdtast_type = jdtast_type;
    }

}
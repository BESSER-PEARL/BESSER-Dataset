





import java.util.List;
import java.util.ArrayList;

public class atlext_OCL_VariableDeclaration extends OCL_TypedElement, ATL_LocatedElement {

    private String varName;
    private String id;





    private LetExp letexp;




    private OclExpression oclexpression;


    public atlext_OCL_VariableDeclaration(
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

    public LetExp getLetexp() {
        return letexp;
    }

    public void setLetexp(LetExp letexp) {
        this.letexp = letexp;
    }
    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}
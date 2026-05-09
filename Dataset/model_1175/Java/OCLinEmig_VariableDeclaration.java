





import java.util.List;
import java.util.ArrayList;

public class OCLinEmig_VariableDeclaration extends LocatedElement {

    private String varName;
    private String id;





    private OCLinEmig_OclExpression oclinemig_oclexpression;




    private OCLinEmig_OclType oclinemig_ocltype;




    private OCLinEmig_OclExpression oclinemig_oclexpression;




    private OCLinEmig_OclType oclinemig_ocltype;


    public OCLinEmig_VariableDeclaration(
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

    public OCLinEmig_OclExpression getOclinemig_oclexpression() {
        return oclinemig_oclexpression;
    }

    public void setOclinemig_oclexpression(OCLinEmig_OclExpression oclinemig_oclexpression) {
        this.oclinemig_oclexpression = oclinemig_oclexpression;
    }
    public OCLinEmig_OclType getOclinemig_ocltype() {
        return oclinemig_ocltype;
    }

    public void setOclinemig_ocltype(OCLinEmig_OclType oclinemig_ocltype) {
        this.oclinemig_ocltype = oclinemig_ocltype;
    }
    public OCLinEmig_OclExpression getOclinemig_oclexpression() {
        return oclinemig_oclexpression;
    }

    public void setOclinemig_oclexpression(OCLinEmig_OclExpression oclinemig_oclexpression) {
        this.oclinemig_oclexpression = oclinemig_oclexpression;
    }
    public OCLinEmig_OclType getOclinemig_ocltype() {
        return oclinemig_ocltype;
    }

    public void setOclinemig_ocltype(OCLinEmig_OclType oclinemig_ocltype) {
        this.oclinemig_ocltype = oclinemig_ocltype;
    }

}
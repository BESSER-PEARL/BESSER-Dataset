





import java.util.List;
import java.util.ArrayList;

public class atl_n_ocl_OCL_VariableDeclaration  {

    private String id;
    private String varName;





    private OclExpression oclexpression;




    private OclType ocltype;


    public atl_n_ocl_OCL_VariableDeclaration(
        String id,        String varName    ) {
        this.id = id;
        this.varName = varName;
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

    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }
    public OclType getOcltype() {
        return ocltype;
    }

    public void setOcltype(OclType ocltype) {
        this.ocltype = ocltype;
    }

}
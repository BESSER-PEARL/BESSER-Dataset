





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_VariableCS extends CSTNode {

    private String name;





    private TypeCS typecs;




    private OCLExpressionCS oclexpressioncs;


    public ocl_cst_VariableCS(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public TypeCS getTypecs() {
        return typecs;
    }

    public void setTypecs(TypeCS typecs) {
        this.typecs = typecs;
    }
    public OCLExpressionCS getOclexpressioncs() {
        return oclexpressioncs;
    }

    public void setOclexpressioncs(OCLExpressionCS oclexpressioncs) {
        this.oclexpressioncs = oclexpressioncs;
    }

}
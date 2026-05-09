





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_DefExpressionCS extends CSTNode {






    private OCLExpressionCS oclexpressioncs;




    private OperationCS operationcs;


    public ocl_cst_DefExpressionCS(
    ) {
        super(
        );
    }



    public OCLExpressionCS getOclexpressioncs() {
        return oclexpressioncs;
    }

    public void setOclexpressioncs(OCLExpressionCS oclexpressioncs) {
        this.oclexpressioncs = oclexpressioncs;
    }
    public OperationCS getOperationcs() {
        return operationcs;
    }

    public void setOperationcs(OperationCS operationcs) {
        this.operationcs = operationcs;
    }

}






import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_VariableInitializationCS extends StatementCS {

    private boolean withResult;





    private OCLExpressionCS oclexpressioncs;




    private SimpleNameCS simplenamecs;




    private TypeCS typecs;


    public qvtoperational_cst_VariableInitializationCS(
        boolean withResult    ) {
        super(
        );
        this.withResult = withResult;
    }


    public boolean getWithresult() {
        return withResult;
    }

    public void setWithresult(boolean withResult) {
        this.withResult = withResult;
    }

    public OCLExpressionCS getOclexpressioncs() {
        return oclexpressioncs;
    }

    public void setOclexpressioncs(OCLExpressionCS oclexpressioncs) {
        this.oclexpressioncs = oclexpressioncs;
    }
    public SimpleNameCS getSimplenamecs() {
        return simplenamecs;
    }

    public void setSimplenamecs(SimpleNameCS simplenamecs) {
        this.simplenamecs = simplenamecs;
    }
    public TypeCS getTypecs() {
        return typecs;
    }

    public void setTypecs(TypeCS typecs) {
        this.typecs = typecs;
    }

}
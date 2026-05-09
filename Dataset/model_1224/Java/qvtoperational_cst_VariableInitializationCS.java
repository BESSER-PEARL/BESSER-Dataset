





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_VariableInitializationCS extends StatementCS {

    private boolean withResult;





    private TypeCS typecs;




    private SimpleNameCS simplenamecs;




    private OCLExpressionCS oclexpressioncs;


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

    public TypeCS getTypecs() {
        return typecs;
    }

    public void setTypecs(TypeCS typecs) {
        this.typecs = typecs;
    }
    public SimpleNameCS getSimplenamecs() {
        return simplenamecs;
    }

    public void setSimplenamecs(SimpleNameCS simplenamecs) {
        this.simplenamecs = simplenamecs;
    }
    public OCLExpressionCS getOclexpressioncs() {
        return oclexpressioncs;
    }

    public void setOclexpressioncs(OCLExpressionCS oclexpressioncs) {
        this.oclexpressioncs = oclexpressioncs;
    }

}
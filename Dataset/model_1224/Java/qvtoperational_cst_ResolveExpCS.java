





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_ResolveExpCS extends CallExpCS {

    private boolean isDeferred;
    private boolean isInverse;
    private boolean one;





    private OCLExpressionCS oclexpressioncs;




    private VariableCS variablecs;


    public qvtoperational_cst_ResolveExpCS(
        boolean isDeferred,        boolean isInverse,        boolean one    ) {
        super(
        );
        this.isDeferred = isDeferred;
        this.isInverse = isInverse;
        this.one = one;
    }


    public boolean getIsdeferred() {
        return isDeferred;
    }

    public void setIsdeferred(boolean isDeferred) {
        this.isDeferred = isDeferred;
    }
    public boolean getIsinverse() {
        return isInverse;
    }

    public void setIsinverse(boolean isInverse) {
        this.isInverse = isInverse;
    }
    public boolean getOne() {
        return one;
    }

    public void setOne(boolean one) {
        this.one = one;
    }

    public OCLExpressionCS getOclexpressioncs() {
        return oclexpressioncs;
    }

    public void setOclexpressioncs(OCLExpressionCS oclexpressioncs) {
        this.oclexpressioncs = oclexpressioncs;
    }
    public VariableCS getVariablecs() {
        return variablecs;
    }

    public void setVariablecs(VariableCS variablecs) {
        this.variablecs = variablecs;
    }

}
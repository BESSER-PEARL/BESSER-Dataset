





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_ResolveExp extends CallExp, ImperativeExpression {

    private String isDeferred;
    private String isInverse;
    private String one;





    private Variable variable;




    private OclExpression oclexpression;


    public QVTOperational_ResolveExp(
        String isDeferred,        String isInverse,        String one    ) {
        super(
        );
        this.isDeferred = isDeferred;
        this.isInverse = isInverse;
        this.one = one;
    }


    public String getIsdeferred() {
        return isDeferred;
    }

    public void setIsdeferred(String isDeferred) {
        this.isDeferred = isDeferred;
    }
    public String getIsinverse() {
        return isInverse;
    }

    public void setIsinverse(String isInverse) {
        this.isInverse = isInverse;
    }
    public String getOne() {
        return one;
    }

    public void setOne(String one) {
        this.one = one;
    }

    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }
    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}
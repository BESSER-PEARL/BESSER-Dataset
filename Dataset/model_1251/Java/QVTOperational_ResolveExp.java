





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_ResolveExp extends CallExp, ImperativeExpression {

    private String one;
    private String isInverse;
    private String isDeferred;





    private OclExpression oclexpression;


    public QVTOperational_ResolveExp(
        String one,        String isInverse,        String isDeferred    ) {
        super(
        );
        this.one = one;
        this.isInverse = isInverse;
        this.isDeferred = isDeferred;
    }


    public String getOne() {
        return one;
    }

    public void setOne(String one) {
        this.one = one;
    }
    public String getIsinverse() {
        return isInverse;
    }

    public void setIsinverse(String isInverse) {
        this.isInverse = isInverse;
    }
    public String getIsdeferred() {
        return isDeferred;
    }

    public void setIsdeferred(String isDeferred) {
        this.isDeferred = isDeferred;
    }

    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}
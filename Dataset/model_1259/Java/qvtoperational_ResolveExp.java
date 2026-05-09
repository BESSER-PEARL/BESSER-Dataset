





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_ResolveExp extends ImperativeExpression, CallExp {

    private String one;
    private String isInverse;
    private String isDeferred;





    private qvtoperational_OCLExpression qvtoperational_oclexpression;


    public qvtoperational_ResolveExp(
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

    public qvtoperational_OCLExpression getQvtoperational_oclexpression() {
        return qvtoperational_oclexpression;
    }

    public void setQvtoperational_oclexpression(qvtoperational_OCLExpression qvtoperational_oclexpression) {
        this.qvtoperational_oclexpression = qvtoperational_oclexpression;
    }

}
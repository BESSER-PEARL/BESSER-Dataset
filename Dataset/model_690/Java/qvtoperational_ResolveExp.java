





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_ResolveExp extends CallExp {

    private String isInverse;
    private String one;
    private String isDeferred;





    private OclExpression oclexpression;


    public qvtoperational_ResolveExp(
        String isInverse,        String one,        String isDeferred    ) {
        super(
        );
        this.isInverse = isInverse;
        this.one = one;
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
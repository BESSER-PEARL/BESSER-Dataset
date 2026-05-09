





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_ResolveExp extends ImperativeExpression, CallExp {

    private String isInverse;
    private String isDeferred;
    private String one;



    public QVTOperational_ResolveExp(
        String isInverse,        String isDeferred,        String one    ) {
        super(
        );
        this.isInverse = isInverse;
        this.isDeferred = isDeferred;
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
    public String getOne() {
        return one;
    }

    public void setOne(String one) {
        this.one = one;
    }


}
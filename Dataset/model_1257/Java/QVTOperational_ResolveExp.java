





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_ResolveExp  {

    private String isInverse;
    private String one;
    private String isDeferred;



    public QVTOperational_ResolveExp(
        String isInverse,        String one,        String isDeferred    ) {
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


}
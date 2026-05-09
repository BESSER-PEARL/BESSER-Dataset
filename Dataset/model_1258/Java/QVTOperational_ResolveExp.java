





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_ResolveExp  {

    private String one;
    private String isDeferred;
    private String isInverse;



    public QVTOperational_ResolveExp(
        String one,        String isDeferred,        String isInverse    ) {
        this.one = one;
        this.isDeferred = isDeferred;
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
    public String getIsinverse() {
        return isInverse;
    }

    public void setIsinverse(String isInverse) {
        this.isInverse = isInverse;
    }


}
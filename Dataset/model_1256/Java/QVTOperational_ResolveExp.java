





import java.util.List;
import java.util.ArrayList;

public class QVTOperational_ResolveExp  {

    private String isDeferred;
    private String one;
    private String isInverse;



    public QVTOperational_ResolveExp(
        String isDeferred,        String one,        String isInverse    ) {
        this.isDeferred = isDeferred;
        this.one = one;
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
    public String getIsinverse() {
        return isInverse;
    }

    public void setIsinverse(String isInverse) {
        this.isInverse = isInverse;
    }


}






import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_ResolveExpCS extends CallExpCS {

    private boolean isInverse;
    private boolean one;
    private boolean isDeferred;



    public qvtoperational_cst_ResolveExpCS(
        boolean isInverse,        boolean one,        boolean isDeferred    ) {
        super(
        );
        this.isInverse = isInverse;
        this.one = one;
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
    public boolean getIsdeferred() {
        return isDeferred;
    }

    public void setIsdeferred(boolean isDeferred) {
        this.isDeferred = isDeferred;
    }


}
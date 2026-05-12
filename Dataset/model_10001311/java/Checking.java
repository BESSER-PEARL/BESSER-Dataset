





import java.util.List;
import java.util.ArrayList;

public class Checking  {

    private float OVERDRAFT_FEE;
    private float OVERDRAFT_LIMIT;
    private boolean isActive;



    public Checking(
        float OVERDRAFT_FEE,        float OVERDRAFT_LIMIT,        boolean isActive    ) {
        this.OVERDRAFT_FEE = OVERDRAFT_FEE;
        this.OVERDRAFT_LIMIT = OVERDRAFT_LIMIT;
        this.isActive = isActive;
    }


    public float getOverdraft_fee() {
        return OVERDRAFT_FEE;
    }

    public void setOverdraft_fee(float OVERDRAFT_FEE) {
        this.OVERDRAFT_FEE = OVERDRAFT_FEE;
    }
    public float getOverdraft_limit() {
        return OVERDRAFT_LIMIT;
    }

    public void setOverdraft_limit(float OVERDRAFT_LIMIT) {
        this.OVERDRAFT_LIMIT = OVERDRAFT_LIMIT;
    }
    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }


}
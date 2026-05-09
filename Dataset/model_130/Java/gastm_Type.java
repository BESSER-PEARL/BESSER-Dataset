





import java.util.List;
import java.util.ArrayList;

public class gastm_Type extends GASTMSyntaxObject {

    private boolean isVolatile;
    private boolean isConst;



    public gastm_Type(
        boolean isVolatile,        boolean isConst    ) {
        super(
        );
        this.isVolatile = isVolatile;
        this.isConst = isConst;
    }


    public boolean getIsvolatile() {
        return isVolatile;
    }

    public void setIsvolatile(boolean isVolatile) {
        this.isVolatile = isVolatile;
    }
    public boolean getIsconst() {
        return isConst;
    }

    public void setIsconst(boolean isConst) {
        this.isConst = isConst;
    }


}
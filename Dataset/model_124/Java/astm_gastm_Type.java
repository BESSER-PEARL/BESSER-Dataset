





import java.util.List;
import java.util.ArrayList;

public class astm_gastm_Type extends GASTMSyntaxObject {

    private boolean isConst;
    private boolean isVolatile;



    public astm_gastm_Type(
        boolean isConst,        boolean isVolatile    ) {
        super(
        );
        this.isConst = isConst;
        this.isVolatile = isVolatile;
    }


    public boolean getIsconst() {
        return isConst;
    }

    public void setIsconst(boolean isConst) {
        this.isConst = isConst;
    }
    public boolean getIsvolatile() {
        return isVolatile;
    }

    public void setIsvolatile(boolean isVolatile) {
        this.isVolatile = isVolatile;
    }


}
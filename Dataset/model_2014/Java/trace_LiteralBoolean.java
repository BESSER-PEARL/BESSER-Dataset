





import java.util.List;
import java.util.ArrayList;

public class trace_LiteralBoolean extends LiteralValue {

    private boolean boolvalue;



    public trace_LiteralBoolean(
        boolean boolvalue    ) {
        super(
        );
        this.boolvalue = boolvalue;
    }


    public boolean getBoolvalue() {
        return boolvalue;
    }

    public void setBoolvalue(boolean boolvalue) {
        this.boolvalue = boolvalue;
    }


}






import java.util.List;
import java.util.ArrayList;

public class AsmL_StringConstant extends Constant {

    private String val;



    public AsmL_StringConstant(
        String val    ) {
        super(
        );
        this.val = val;
    }


    public String getVal() {
        return val;
    }

    public void setVal(String val) {
        this.val = val;
    }


}
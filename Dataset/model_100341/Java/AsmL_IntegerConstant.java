





import java.util.List;
import java.util.ArrayList;

public class AsmL_IntegerConstant extends Constant {

    private String val;



    public AsmL_IntegerConstant(
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
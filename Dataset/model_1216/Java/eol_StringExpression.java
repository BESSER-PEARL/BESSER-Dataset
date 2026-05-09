





import java.util.List;
import java.util.ArrayList;

public class eol_StringExpression extends PrimitiveExpression {

    private String val;



    public eol_StringExpression(
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
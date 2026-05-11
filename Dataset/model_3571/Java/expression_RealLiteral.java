





import java.util.List;
import java.util.ArrayList;

public class expression_RealLiteral extends Literal {

    private String val;



    public expression_RealLiteral(
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
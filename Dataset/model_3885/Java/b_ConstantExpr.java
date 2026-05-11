





import java.util.List;
import java.util.ArrayList;

public class b_ConstantExpr extends LogicalExpr {

    private String constant;



    public b_ConstantExpr(
        String constant    ) {
        super(
        );
        this.constant = constant;
    }


    public String getConstant() {
        return constant;
    }

    public void setConstant(String constant) {
        this.constant = constant;
    }


}
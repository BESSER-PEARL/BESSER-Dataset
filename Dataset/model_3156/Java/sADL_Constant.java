





import java.util.List;
import java.util.ArrayList;

public class sADL_Constant extends Expression {

    private String constant;



    public sADL_Constant(
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
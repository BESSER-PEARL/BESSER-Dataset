





import java.util.List;
import java.util.ArrayList;

public class ocl_exp_EIntegerLiteralExp extends ENumericLiteralExp {

    private String integerValue;



    public ocl_exp_EIntegerLiteralExp(
        String integerValue    ) {
        super(
        );
        this.integerValue = integerValue;
    }


    public String getIntegervalue() {
        return integerValue;
    }

    public void setIntegervalue(String integerValue) {
        this.integerValue = integerValue;
    }


}
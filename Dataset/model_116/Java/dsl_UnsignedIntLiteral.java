





import java.util.List;
import java.util.ArrayList;

public class dsl_UnsignedIntLiteral  {

    private String sign;





    private dsl_DecimalNumber dsl_decimalnumber;


    public dsl_UnsignedIntLiteral(
        String sign    ) {
        this.sign = sign;
    }


    public String getSign() {
        return sign;
    }

    public void setSign(String sign) {
        this.sign = sign;
    }

    public dsl_DecimalNumber getDsl_decimalnumber() {
        return dsl_decimalnumber;
    }

    public void setDsl_decimalnumber(dsl_DecimalNumber dsl_decimalnumber) {
        this.dsl_decimalnumber = dsl_decimalnumber;
    }

}
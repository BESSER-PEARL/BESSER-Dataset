





import java.util.List;
import java.util.ArrayList;

public class gDSL_MExp extends AExp {

    private String sign;





    private gDSL_MExp gdsl_mexp;


    public gDSL_MExp(
        String sign    ) {
        super(
        );
        this.sign = sign;
    }


    public String getSign() {
        return sign;
    }

    public void setSign(String sign) {
        this.sign = sign;
    }

    public gDSL_MExp getGdsl_mexp() {
        return gdsl_mexp;
    }

    public void setGdsl_mexp(gDSL_MExp gdsl_mexp) {
        this.gdsl_mexp = gdsl_mexp;
    }

}






import java.util.List;
import java.util.ArrayList;

public class coCoMM_HardLimitDRExpression  {

    private String op;
    private String value;





    private coCoMM_HardLimitDR cocomm_hardlimitdr;


    public coCoMM_HardLimitDRExpression(
        String op,        String value    ) {
        this.op = op;
        this.value = value;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public coCoMM_HardLimitDR getCocomm_hardlimitdr() {
        return cocomm_hardlimitdr;
    }

    public void setCocomm_hardlimitdr(coCoMM_HardLimitDR cocomm_hardlimitdr) {
        this.cocomm_hardlimitdr = cocomm_hardlimitdr;
    }

}
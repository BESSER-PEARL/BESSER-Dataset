





import java.util.List;
import java.util.ArrayList;

public class coCoMM_HardLimitCCExpression  {

    private String value;
    private String op;





    private coCoMM_HardLimitCC cocomm_hardlimitcc;


    public coCoMM_HardLimitCCExpression(
        String value,        String op    ) {
        this.value = value;
        this.op = op;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public coCoMM_HardLimitCC getCocomm_hardlimitcc() {
        return cocomm_hardlimitcc;
    }

    public void setCocomm_hardlimitcc(coCoMM_HardLimitCC cocomm_hardlimitcc) {
        this.cocomm_hardlimitcc = cocomm_hardlimitcc;
    }

}
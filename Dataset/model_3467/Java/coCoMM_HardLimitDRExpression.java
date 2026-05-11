





import java.util.List;
import java.util.ArrayList;

public class coCoMM_HardLimitDRExpression  {

    private String value;
    private String op;





    private coCoMM_HardLimitSC cocomm_hardlimitsc;


    public coCoMM_HardLimitDRExpression(
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

    public coCoMM_HardLimitSC getCocomm_hardlimitsc() {
        return cocomm_hardlimitsc;
    }

    public void setCocomm_hardlimitsc(coCoMM_HardLimitSC cocomm_hardlimitsc) {
        this.cocomm_hardlimitsc = cocomm_hardlimitsc;
    }

}
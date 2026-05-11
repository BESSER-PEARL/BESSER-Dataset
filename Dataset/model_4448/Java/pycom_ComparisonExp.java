





import java.util.List;
import java.util.ArrayList;

public class pycom_ComparisonExp  {

    private String op;





    private pycom_LogicExp pycom_logicexp;


    public pycom_ComparisonExp(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public pycom_LogicExp getPycom_logicexp() {
        return pycom_logicexp;
    }

    public void setPycom_logicexp(pycom_LogicExp pycom_logicexp) {
        this.pycom_logicexp = pycom_logicexp;
    }

}
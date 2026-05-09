





import java.util.List;
import java.util.ArrayList;

public class analysis_scheduling_FSMOperation  {

    private String var;
    private String val;
    private String op;



    public analysis_scheduling_FSMOperation(
        String var,        String val,        String op    ) {
        this.var = var;
        this.val = val;
        this.op = op;
    }


    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }
    public String getVal() {
        return val;
    }

    public void setVal(String val) {
        this.val = val;
    }
    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }


}
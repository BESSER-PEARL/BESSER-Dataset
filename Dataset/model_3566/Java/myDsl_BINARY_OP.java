





import java.util.List;
import java.util.ArrayList;

public class myDsl_BINARY_OP  {

    private String aDD_OP;
    private String rEL_OP;



    public myDsl_BINARY_OP(
        String aDD_OP,        String rEL_OP    ) {
        this.aDD_OP = aDD_OP;
        this.rEL_OP = rEL_OP;
    }


    public String getAdd_op() {
        return aDD_OP;
    }

    public void setAdd_op(String aDD_OP) {
        this.aDD_OP = aDD_OP;
    }
    public String getRel_op() {
        return rEL_OP;
    }

    public void setRel_op(String rEL_OP) {
        this.rEL_OP = rEL_OP;
    }


}
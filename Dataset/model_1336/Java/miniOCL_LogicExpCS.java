





import java.util.List;
import java.util.ArrayList;

public class miniOCL_LogicExpCS extends ExpCS {

    private String op;





    private miniOCL_LogicExpCS miniocl_logicexpcs;


    public miniOCL_LogicExpCS(
        String op    ) {
        super(
        );
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public miniOCL_LogicExpCS getMiniocl_logicexpcs() {
        return miniocl_logicexpcs;
    }

    public void setMiniocl_logicexpcs(miniOCL_LogicExpCS miniocl_logicexpcs) {
        this.miniocl_logicexpcs = miniocl_logicexpcs;
    }

}
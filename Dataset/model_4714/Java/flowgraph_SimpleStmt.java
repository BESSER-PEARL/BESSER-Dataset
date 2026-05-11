





import java.util.List;
import java.util.ArrayList;

public class flowgraph_SimpleStmt extends FlowInstr, Stmt {

    private String type;
    private String functionAccess;
    private String valiableAccess;



    public flowgraph_SimpleStmt(
        String type,        String functionAccess,        String valiableAccess    ) {
        super(
        );
        this.type = type;
        this.functionAccess = functionAccess;
        this.valiableAccess = valiableAccess;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getFunctionaccess() {
        return functionAccess;
    }

    public void setFunctionaccess(String functionAccess) {
        this.functionAccess = functionAccess;
    }
    public String getValiableaccess() {
        return valiableAccess;
    }

    public void setValiableaccess(String valiableAccess) {
        this.valiableAccess = valiableAccess;
    }


}
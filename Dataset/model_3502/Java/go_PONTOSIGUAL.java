





import java.util.List;
import java.util.ArrayList;

public class go_PONTOSIGUAL  {

    private String op;





    private go_VarDecl go_vardecl;


    public go_PONTOSIGUAL(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public go_VarDecl getGo_vardecl() {
        return go_vardecl;
    }

    public void setGo_vardecl(go_VarDecl go_vardecl) {
        this.go_vardecl = go_vardecl;
    }

}
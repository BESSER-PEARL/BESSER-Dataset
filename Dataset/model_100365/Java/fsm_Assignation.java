





import java.util.List;
import java.util.ArrayList;

public class fsm_Assignation extends Statement {






    private fsm_VarDecl fsm_vardecl;


    public fsm_Assignation(
    ) {
        super(
        );
    }



    public fsm_VarDecl getFsm_vardecl() {
        return fsm_vardecl;
    }

    public void setFsm_vardecl(fsm_VarDecl fsm_vardecl) {
        this.fsm_vardecl = fsm_vardecl;
    }

}
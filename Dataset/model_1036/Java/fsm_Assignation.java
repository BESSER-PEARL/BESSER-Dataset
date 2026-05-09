





import java.util.List;
import java.util.ArrayList;

public class fsm_Assignation extends Statement {






    private fsm_Expression fsm_expression;




    private fsm_VarDecl fsm_vardecl;


    public fsm_Assignation(
    ) {
        super(
        );
    }



    public fsm_Expression getFsm_expression() {
        return fsm_expression;
    }

    public void setFsm_expression(fsm_Expression fsm_expression) {
        this.fsm_expression = fsm_expression;
    }
    public fsm_VarDecl getFsm_vardecl() {
        return fsm_vardecl;
    }

    public void setFsm_vardecl(fsm_VarDecl fsm_vardecl) {
        this.fsm_vardecl = fsm_vardecl;
    }

}
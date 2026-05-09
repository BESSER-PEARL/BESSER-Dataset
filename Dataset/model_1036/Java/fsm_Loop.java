





import java.util.List;
import java.util.ArrayList;

public class fsm_Loop extends Statement {






    private fsm_Expression fsm_expression;




    private fsm_Program fsm_program;


    public fsm_Loop(
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
    public fsm_Program getFsm_program() {
        return fsm_program;
    }

    public void setFsm_program(fsm_Program fsm_program) {
        this.fsm_program = fsm_program;
    }

}






import java.util.List;
import java.util.ArrayList;

public class fsm_VarDecl extends Statement {

    private String key;





    private fsm_Expression fsm_expression;


    public fsm_VarDecl(
        String key    ) {
        super(
        );
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public fsm_Expression getFsm_expression() {
        return fsm_expression;
    }

    public void setFsm_expression(fsm_Expression fsm_expression) {
        this.fsm_expression = fsm_expression;
    }

}
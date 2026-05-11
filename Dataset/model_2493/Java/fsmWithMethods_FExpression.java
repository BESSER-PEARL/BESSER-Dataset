





import java.util.List;
import java.util.ArrayList;

public class fsmWithMethods_FExpression extends Referentiable {

    private String name;





    private fsmWithMethods_Fsm fsmwithmethods_fsm;


    public fsmWithMethods_FExpression(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fsmWithMethods_Fsm getFsmwithmethods_fsm() {
        return fsmwithmethods_fsm;
    }

    public void setFsmwithmethods_fsm(fsmWithMethods_Fsm fsmwithmethods_fsm) {
        this.fsmwithmethods_fsm = fsmwithmethods_fsm;
    }

}
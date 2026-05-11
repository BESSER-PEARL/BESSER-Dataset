





import java.util.List;
import java.util.ArrayList;

public class cstat1_Action  {

    private String expression;
    private String mode;





    private cstat1_AbstractState cstat1_abstractstate;


    public cstat1_Action(
        String expression,        String mode    ) {
        this.expression = expression;
        this.mode = mode;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public cstat1_AbstractState getCstat1_abstractstate() {
        return cstat1_abstractstate;
    }

    public void setCstat1_abstractstate(cstat1_AbstractState cstat1_abstractstate) {
        this.cstat1_abstractstate = cstat1_abstractstate;
    }

}






import java.util.List;
import java.util.ArrayList;

public class HALL_FSMActions_Let extends ActionExpression {

    private String name;





    private FSMActions_ActionExpression fsmactions_actionexpression;




    private FSMActions_ActionExpression fsmactions_actionexpression;




    private Type type;


    public HALL_FSMActions_Let(
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

    public FSMActions_ActionExpression getFsmactions_actionexpression() {
        return fsmactions_actionexpression;
    }

    public void setFsmactions_actionexpression(FSMActions_ActionExpression fsmactions_actionexpression) {
        this.fsmactions_actionexpression = fsmactions_actionexpression;
    }
    public FSMActions_ActionExpression getFsmactions_actionexpression() {
        return fsmactions_actionexpression;
    }

    public void setFsmactions_actionexpression(FSMActions_ActionExpression fsmactions_actionexpression) {
        this.fsmactions_actionexpression = fsmactions_actionexpression;
    }
    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

}
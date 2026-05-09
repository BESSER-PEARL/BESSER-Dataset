





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMActions_DomainPropertySet extends ActionExpression {

    private String name;





    private FSMActions_ActionExpression fsmactions_actionexpression;


    public HALL_FSMActions_DomainPropertySet(
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

}






import java.util.List;
import java.util.ArrayList;

public class gfsm_IntVarAssign extends IntOperation {

    private String name;





    private gfsm_IntExpression gfsm_intexpression;


    public gfsm_IntVarAssign(
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

    public gfsm_IntExpression getGfsm_intexpression() {
        return gfsm_intexpression;
    }

    public void setGfsm_intexpression(gfsm_IntExpression gfsm_intexpression) {
        this.gfsm_intexpression = gfsm_intexpression;
    }

}
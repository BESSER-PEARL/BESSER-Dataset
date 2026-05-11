





import java.util.List;
import java.util.ArrayList;

public class jpdl31_AssignmentType extends Delegation {

    private String pooledActors;
    private String expression;
    private String actorId;



    public jpdl31_AssignmentType(
        String pooledActors,        String expression,        String actorId    ) {
        super(
        );
        this.pooledActors = pooledActors;
        this.expression = expression;
        this.actorId = actorId;
    }


    public String getPooledactors() {
        return pooledActors;
    }

    public void setPooledactors(String pooledActors) {
        this.pooledActors = pooledActors;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getActorid() {
        return actorId;
    }

    public void setActorid(String actorId) {
        this.actorId = actorId;
    }


}
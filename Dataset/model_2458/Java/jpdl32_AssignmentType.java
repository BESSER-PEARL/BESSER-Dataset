





import java.util.List;
import java.util.ArrayList;

public class jpdl32_AssignmentType extends Delegation {

    private String actorId;
    private String expression;
    private String pooledActors;



    public jpdl32_AssignmentType(
        String actorId,        String expression,        String pooledActors    ) {
        super(
        );
        this.actorId = actorId;
        this.expression = expression;
        this.pooledActors = pooledActors;
    }


    public String getActorid() {
        return actorId;
    }

    public void setActorid(String actorId) {
        this.actorId = actorId;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getPooledactors() {
        return pooledActors;
    }

    public void setPooledactors(String pooledActors) {
        this.pooledActors = pooledActors;
    }


}
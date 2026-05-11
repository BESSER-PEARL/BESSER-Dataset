





import java.util.List;
import java.util.ArrayList;

public class jpdl32_AssignmentType extends Delegation {

    private String expression;
    private String actorId;
    private String pooledActors;



    public jpdl32_AssignmentType(
        String expression,        String actorId,        String pooledActors    ) {
        super(
        );
        this.expression = expression;
        this.actorId = actorId;
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
    public String getPooledactors() {
        return pooledActors;
    }

    public void setPooledactors(String pooledActors) {
        this.pooledActors = pooledActors;
    }


}
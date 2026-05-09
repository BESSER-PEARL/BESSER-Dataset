





import java.util.List;
import java.util.ArrayList;

public class state_OpaqueExpression  {

    private String body;





    private state_Constraint state_constraint;


    public state_OpaqueExpression(
        String body    ) {
        this.body = body;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public state_Constraint getState_constraint() {
        return state_constraint;
    }

    public void setState_constraint(state_Constraint state_constraint) {
        this.state_constraint = state_constraint;
    }

}
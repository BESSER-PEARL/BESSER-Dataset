





import java.util.List;
import java.util.ArrayList;

public class statemachine_StatePropertyExpression extends Expression {

    private String property;





    private statemachine_State statemachine_state;


    public statemachine_StatePropertyExpression(
        String property    ) {
        super(
        );
        this.property = property;
    }


    public String getProperty() {
        return property;
    }

    public void setProperty(String property) {
        this.property = property;
    }

    public statemachine_State getStatemachine_state() {
        return statemachine_state;
    }

    public void setStatemachine_state(statemachine_State statemachine_state) {
        this.statemachine_state = statemachine_state;
    }

}
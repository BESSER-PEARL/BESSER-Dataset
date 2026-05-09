





import java.util.List;
import java.util.ArrayList;

public class martinfowlerdsl_AbstractEvent  {

    private String code;
    private String name;





    private martinfowlerdsl_StateMachine martinfowlerdsl_statemachine;


    public martinfowlerdsl_AbstractEvent(
        String code,        String name    ) {
        this.code = code;
        this.name = name;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public martinfowlerdsl_StateMachine getMartinfowlerdsl_statemachine() {
        return martinfowlerdsl_statemachine;
    }

    public void setMartinfowlerdsl_statemachine(martinfowlerdsl_StateMachine martinfowlerdsl_statemachine) {
        this.martinfowlerdsl_statemachine = martinfowlerdsl_statemachine;
    }

}
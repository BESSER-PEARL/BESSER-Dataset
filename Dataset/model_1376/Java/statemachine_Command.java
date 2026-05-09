





import java.util.List;
import java.util.ArrayList;

public class statemachine_Command extends NamedElement {

    private String code;





    private statemachine_Statemachine statemachine_statemachine;


    public statemachine_Command(
        String code    ) {
        super(
        );
        this.code = code;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public statemachine_Statemachine getStatemachine_statemachine() {
        return statemachine_statemachine;
    }

    public void setStatemachine_statemachine(statemachine_Statemachine statemachine_statemachine) {
        this.statemachine_statemachine = statemachine_statemachine;
    }

}






import java.util.List;
import java.util.ArrayList;

public class dsl_Command  {

    private String code;
    private String name;





    private dsl_Statemachine dsl_statemachine;




    private dsl_State dsl_state;


    public dsl_Command(
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

    public dsl_Statemachine getDsl_statemachine() {
        return dsl_statemachine;
    }

    public void setDsl_statemachine(dsl_Statemachine dsl_statemachine) {
        this.dsl_statemachine = dsl_statemachine;
    }
    public dsl_State getDsl_state() {
        return dsl_state;
    }

    public void setDsl_state(dsl_State dsl_state) {
        this.dsl_state = dsl_state;
    }

}
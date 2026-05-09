





import java.util.List;
import java.util.ArrayList;

public class nicoLang_State  {

    private String name;





    private nicoLang_Transition nicolang_transition;




    private nicoLang_Transition nicolang_transition;




    private nicoLang_FSM nicolang_fsm;


    public nicoLang_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public nicoLang_Transition getNicolang_transition() {
        return nicolang_transition;
    }

    public void setNicolang_transition(nicoLang_Transition nicolang_transition) {
        this.nicolang_transition = nicolang_transition;
    }
    public nicoLang_Transition getNicolang_transition() {
        return nicolang_transition;
    }

    public void setNicolang_transition(nicoLang_Transition nicolang_transition) {
        this.nicolang_transition = nicolang_transition;
    }
    public nicoLang_FSM getNicolang_fsm() {
        return nicolang_fsm;
    }

    public void setNicolang_fsm(nicoLang_FSM nicolang_fsm) {
        this.nicolang_fsm = nicolang_fsm;
    }

}
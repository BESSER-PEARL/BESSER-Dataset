





import java.util.List;
import java.util.ArrayList;

public class nicoLang_Transition  {

    private String name;
    private String trigger;





    private nicoLang_FSM nicolang_fsm;


    public nicoLang_Transition(
        String name,        String trigger    ) {
        this.name = name;
        this.trigger = trigger;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }

    public nicoLang_FSM getNicolang_fsm() {
        return nicolang_fsm;
    }

    public void setNicolang_fsm(nicoLang_FSM nicolang_fsm) {
        this.nicolang_fsm = nicolang_fsm;
    }

}
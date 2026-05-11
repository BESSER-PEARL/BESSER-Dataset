





import java.util.List;
import java.util.ArrayList;

public class smDsl_EventHandlingDescription  {






    private smDsl_State smdsl_state;




    private smDsl_Event smdsl_event;




    private List<smDsl_Command> smdsl_commands;




    private smDsl_State smdsl_state;


    public smDsl_EventHandlingDescription(
    ) {
        this.smdsl_commands = new ArrayList<>();
    }

    public smDsl_EventHandlingDescription(
        ArrayList<smDsl_Command> smdsl_commands    ) {
        this.smdsl_commands = smdsl_commands;
    }


    public smDsl_State getSmdsl_state() {
        return smdsl_state;
    }

    public void setSmdsl_state(smDsl_State smdsl_state) {
        this.smdsl_state = smdsl_state;
    }
    public smDsl_Event getSmdsl_event() {
        return smdsl_event;
    }

    public void setSmdsl_event(smDsl_Event smdsl_event) {
        this.smdsl_event = smdsl_event;
    }
    public List<smDsl_Command> getSmdsl_commands() {
        return smdsl_commands;
    }

    public void addSmdsl_command(Smdsl_command smdsl_command) {
        this.smdsl_commands.add(smdsl_command);
    }
    public smDsl_State getSmdsl_state() {
        return smdsl_state;
    }

    public void setSmdsl_state(smDsl_State smdsl_state) {
        this.smdsl_state = smdsl_state;
    }

}
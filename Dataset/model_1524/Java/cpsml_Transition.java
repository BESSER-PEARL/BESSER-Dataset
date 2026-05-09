





import java.util.List;
import java.util.ArrayList;

public class cpsml_Transition  {

    private String name;
    private String action;
    private String guard;
    private String event;





    private cpsml_System cpsml_system;




    private cpsml_Variable cpsml_variable;




    private cpsml_State cpsml_state;


    public cpsml_Transition(
        String name,        String action,        String guard,        String event    ) {
        this.name = name;
        this.action = action;
        this.guard = guard;
        this.event = event;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }

    public cpsml_System getCpsml_system() {
        return cpsml_system;
    }

    public void setCpsml_system(cpsml_System cpsml_system) {
        this.cpsml_system = cpsml_system;
    }
    public cpsml_Variable getCpsml_variable() {
        return cpsml_variable;
    }

    public void setCpsml_variable(cpsml_Variable cpsml_variable) {
        this.cpsml_variable = cpsml_variable;
    }
    public cpsml_State getCpsml_state() {
        return cpsml_state;
    }

    public void setCpsml_state(cpsml_State cpsml_state) {
        this.cpsml_state = cpsml_state;
    }

}
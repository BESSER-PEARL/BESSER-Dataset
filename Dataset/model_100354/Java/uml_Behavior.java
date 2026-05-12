





import java.util.List;
import java.util.ArrayList;

public class uml_Behavior  {

    private String name;





    private uml_Transition uml_transition;


    public uml_Behavior(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public uml_Transition getUml_transition() {
        return uml_transition;
    }

    public void setUml_transition(uml_Transition uml_transition) {
        this.uml_transition = uml_transition;
    }

}
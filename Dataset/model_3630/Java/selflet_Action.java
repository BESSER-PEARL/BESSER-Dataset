





import java.util.List;
import java.util.ArrayList;

public class selflet_Action  {

    private String file;





    private selflet_AbilityState selflet_abilitystate;




    private selflet_Actions selflet_actions;


    public selflet_Action(
        String file    ) {
        this.file = file;
    }


    public String getFile() {
        return file;
    }

    public void setFile(String file) {
        this.file = file;
    }

    public selflet_AbilityState getSelflet_abilitystate() {
        return selflet_abilitystate;
    }

    public void setSelflet_abilitystate(selflet_AbilityState selflet_abilitystate) {
        this.selflet_abilitystate = selflet_abilitystate;
    }
    public selflet_Actions getSelflet_actions() {
        return selflet_actions;
    }

    public void setSelflet_actions(selflet_Actions selflet_actions) {
        this.selflet_actions = selflet_actions;
    }

}
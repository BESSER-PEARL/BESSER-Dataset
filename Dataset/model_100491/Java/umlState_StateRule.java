





import java.util.List;
import java.util.ArrayList;

public class umlState_StateRule  {

    private String name;





    private umlState_DoRule umlstate_dorule;




    private umlState_SubmachineRule umlstate_submachinerule;




    private umlState_ExitRule umlstate_exitrule;




    private umlState_EntryRule umlstate_entryrule;


    public umlState_StateRule(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public umlState_DoRule getUmlstate_dorule() {
        return umlstate_dorule;
    }

    public void setUmlstate_dorule(umlState_DoRule umlstate_dorule) {
        this.umlstate_dorule = umlstate_dorule;
    }
    public umlState_SubmachineRule getUmlstate_submachinerule() {
        return umlstate_submachinerule;
    }

    public void setUmlstate_submachinerule(umlState_SubmachineRule umlstate_submachinerule) {
        this.umlstate_submachinerule = umlstate_submachinerule;
    }
    public umlState_ExitRule getUmlstate_exitrule() {
        return umlstate_exitrule;
    }

    public void setUmlstate_exitrule(umlState_ExitRule umlstate_exitrule) {
        this.umlstate_exitrule = umlstate_exitrule;
    }
    public umlState_EntryRule getUmlstate_entryrule() {
        return umlstate_entryrule;
    }

    public void setUmlstate_entryrule(umlState_EntryRule umlstate_entryrule) {
        this.umlstate_entryrule = umlstate_entryrule;
    }

}
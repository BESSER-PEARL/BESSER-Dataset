





import java.util.List;
import java.util.ArrayList;

public class dsl_ActorList  {

    private String trigger;





    private dsl_Actor dsl_actor;




    private dsl_ModelActor dsl_modelactor;


    public dsl_ActorList(
        String trigger    ) {
        this.trigger = trigger;
    }


    public String getTrigger() {
        return trigger;
    }

    public void setTrigger(String trigger) {
        this.trigger = trigger;
    }

    public dsl_Actor getDsl_actor() {
        return dsl_actor;
    }

    public void setDsl_actor(dsl_Actor dsl_actor) {
        this.dsl_actor = dsl_actor;
    }
    public dsl_ModelActor getDsl_modelactor() {
        return dsl_modelactor;
    }

    public void setDsl_modelactor(dsl_ModelActor dsl_modelactor) {
        this.dsl_modelactor = dsl_modelactor;
    }

}
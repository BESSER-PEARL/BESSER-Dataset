





import java.util.List;
import java.util.ArrayList;

public class caltrop_CaltropActorImpl  {






    private caltrop_Schedule caltrop_schedule;




    private List<caltrop_ReAction> caltrop_reactions;




    private List<caltrop_StateVariable> caltrop_statevariables;


    public caltrop_CaltropActorImpl(
    ) {
        this.caltrop_reactions = new ArrayList<>();
        this.caltrop_statevariables = new ArrayList<>();
    }

    public caltrop_CaltropActorImpl(
        ArrayList<caltrop_ReAction> caltrop_reactions,        ArrayList<caltrop_StateVariable> caltrop_statevariables    ) {
        this.caltrop_reactions = caltrop_reactions;
        this.caltrop_statevariables = caltrop_statevariables;
    }


    public caltrop_Schedule getCaltrop_schedule() {
        return caltrop_schedule;
    }

    public void setCaltrop_schedule(caltrop_Schedule caltrop_schedule) {
        this.caltrop_schedule = caltrop_schedule;
    }
    public List<caltrop_ReAction> getCaltrop_reactions() {
        return caltrop_reactions;
    }

    public void addCaltrop_reaction(Caltrop_reaction caltrop_reaction) {
        this.caltrop_reactions.add(caltrop_reaction);
    }
    public List<caltrop_StateVariable> getCaltrop_statevariables() {
        return caltrop_statevariables;
    }

    public void addCaltrop_statevariable(Caltrop_statevariable caltrop_statevariable) {
        this.caltrop_statevariables.add(caltrop_statevariable);
    }

}






import java.util.List;
import java.util.ArrayList;

public class actions_ActionReference extends PreGenerationAction {






    private actions_StandAloneAction actions_standaloneaction;




    private List<actions_EObject> actions_eobjects;


    public actions_ActionReference(
    ) {
        super(
        );
        this.actions_eobjects = new ArrayList<>();
    }

    public actions_ActionReference(
        ArrayList<actions_EObject> actions_eobjects    ) {
        this.actions_eobjects = actions_eobjects;
    }


    public actions_StandAloneAction getActions_standaloneaction() {
        return actions_standaloneaction;
    }

    public void setActions_standaloneaction(actions_StandAloneAction actions_standaloneaction) {
        this.actions_standaloneaction = actions_standaloneaction;
    }
    public List<actions_EObject> getActions_eobjects() {
        return actions_eobjects;
    }

    public void addActions_eobject(Actions_eobject actions_eobject) {
        this.actions_eobjects.add(actions_eobject);
    }

}
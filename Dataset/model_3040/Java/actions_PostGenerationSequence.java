





import java.util.List;
import java.util.ArrayList;

public class actions_PostGenerationSequence extends PostGenerationAction {






    private List<actions_PostGenerationAction> actions_postgenerationactions;


    public actions_PostGenerationSequence(
    ) {
        super(
        );
        this.actions_postgenerationactions = new ArrayList<>();
    }

    public actions_PostGenerationSequence(
        ArrayList<actions_PostGenerationAction> actions_postgenerationactions    ) {
        this.actions_postgenerationactions = actions_postgenerationactions;
    }


    public List<actions_PostGenerationAction> getActions_postgenerationactions() {
        return actions_postgenerationactions;
    }

    public void addActions_postgenerationaction(Actions_postgenerationaction actions_postgenerationaction) {
        this.actions_postgenerationactions.add(actions_postgenerationaction);
    }

}
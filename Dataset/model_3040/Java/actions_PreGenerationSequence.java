





import java.util.List;
import java.util.ArrayList;

public class actions_PreGenerationSequence extends PreGenerationAction {






    private List<actions_PreGenerationAction> actions_pregenerationactions;


    public actions_PreGenerationSequence(
    ) {
        super(
        );
        this.actions_pregenerationactions = new ArrayList<>();
    }

    public actions_PreGenerationSequence(
        ArrayList<actions_PreGenerationAction> actions_pregenerationactions    ) {
        this.actions_pregenerationactions = actions_pregenerationactions;
    }


    public List<actions_PreGenerationAction> getActions_pregenerationactions() {
        return actions_pregenerationactions;
    }

    public void addActions_pregenerationaction(Actions_pregenerationaction actions_pregenerationaction) {
        this.actions_pregenerationactions.add(actions_pregenerationaction);
    }

}
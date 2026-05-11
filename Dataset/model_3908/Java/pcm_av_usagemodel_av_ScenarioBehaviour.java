





import java.util.List;
import java.util.ArrayList;

public class pcm_av_usagemodel_av_ScenarioBehaviour extends Entity {






    private List<AbstractUserAction> abstractuseractions;


    public pcm_av_usagemodel_av_ScenarioBehaviour(
    ) {
        super(
        );
        this.abstractuseractions = new ArrayList<>();
    }

    public pcm_av_usagemodel_av_ScenarioBehaviour(
        ArrayList<AbstractUserAction> abstractuseractions    ) {
        this.abstractuseractions = abstractuseractions;
    }


    public List<AbstractUserAction> getAbstractuseractions() {
        return abstractuseractions;
    }

    public void addAbstractuseraction(Abstractuseraction abstractuseraction) {
        this.abstractuseractions.add(abstractuseraction);
    }

}
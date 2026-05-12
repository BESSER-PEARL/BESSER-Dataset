





import java.util.List;
import java.util.ArrayList;

public class rdal_SystemContext extends AbstractContractualElement {






    private List<rdal_ActorReference> rdal_actorreferences;


    public rdal_SystemContext(
    ) {
        super(
        );
        this.rdal_actorreferences = new ArrayList<>();
    }

    public rdal_SystemContext(
        ArrayList<rdal_ActorReference> rdal_actorreferences    ) {
        this.rdal_actorreferences = rdal_actorreferences;
    }


    public List<rdal_ActorReference> getRdal_actorreferences() {
        return rdal_actorreferences;
    }

    public void addRdal_actorreference(Rdal_actorreference rdal_actorreference) {
        this.rdal_actorreferences.add(rdal_actorreference);
    }

}
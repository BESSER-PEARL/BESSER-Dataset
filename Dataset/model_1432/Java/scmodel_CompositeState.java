





import java.util.List;
import java.util.ArrayList;

public class scmodel_CompositeState extends AbstractState {






    private List<scmodel_AbstractState> scmodel_abstractstates;


    public scmodel_CompositeState(
    ) {
        super(
        );
        this.scmodel_abstractstates = new ArrayList<>();
    }

    public scmodel_CompositeState(
        ArrayList<scmodel_AbstractState> scmodel_abstractstates    ) {
        this.scmodel_abstractstates = scmodel_abstractstates;
    }


    public List<scmodel_AbstractState> getScmodel_abstractstates() {
        return scmodel_abstractstates;
    }

    public void addScmodel_abstractstate(Scmodel_abstractstate scmodel_abstractstate) {
        this.scmodel_abstractstates.add(scmodel_abstractstate);
    }

}
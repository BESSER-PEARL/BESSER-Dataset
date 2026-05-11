





import java.util.List;
import java.util.ArrayList;

public class smif_constraints_Rule extends Proposition {






    private List<IdentifiableEntity> identifiableentitys;


    public smif_constraints_Rule(
    ) {
        super(
        );
        this.identifiableentitys = new ArrayList<>();
    }

    public smif_constraints_Rule(
        ArrayList<IdentifiableEntity> identifiableentitys    ) {
        this.identifiableentitys = identifiableentitys;
    }


    public List<IdentifiableEntity> getIdentifiableentitys() {
        return identifiableentitys;
    }

    public void addIdentifiableentity(Identifiableentity identifiableentity) {
        this.identifiableentitys.add(identifiableentity);
    }

}
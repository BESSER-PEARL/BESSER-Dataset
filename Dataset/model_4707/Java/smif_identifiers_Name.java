





import java.util.List;
import java.util.ArrayList;

public class smif_identifiers_Name extends TextIdentifier {






    private List<IdentifiableEntity> identifiableentitys;


    public smif_identifiers_Name(
    ) {
        super(
        );
        this.identifiableentitys = new ArrayList<>();
    }

    public smif_identifiers_Name(
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
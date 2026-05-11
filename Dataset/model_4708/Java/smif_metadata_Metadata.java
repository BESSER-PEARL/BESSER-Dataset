





import java.util.List;
import java.util.ArrayList;

public class smif_metadata_Metadata extends Record {






    private List<IdentifiableEntity> identifiableentitys;


    public smif_metadata_Metadata(
    ) {
        super(
        );
        this.identifiableentitys = new ArrayList<>();
    }

    public smif_metadata_Metadata(
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
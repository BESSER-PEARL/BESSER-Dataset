





import java.util.List;
import java.util.ArrayList;

public class smif_metadata_InformationSource extends metadata_Metadata, toplevel_ActualEntity {






    private List<IdentifiableEntity> identifiableentitys;


    public smif_metadata_InformationSource(
    ) {
        super(
        );
        this.identifiableentitys = new ArrayList<>();
    }

    public smif_metadata_InformationSource(
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






import java.util.List;
import java.util.ArrayList;

public class esmodel_events_ShowHistoryEvent extends Event {






    private versioning_PrimaryVersionSpec versioning_primaryversionspec;




    private versioning_PrimaryVersionSpec versioning_primaryversionspec;




    private List<ModelElementId> modelelementids;


    public esmodel_events_ShowHistoryEvent(
    ) {
        super(
        );
        this.modelelementids = new ArrayList<>();
    }

    public esmodel_events_ShowHistoryEvent(
        ArrayList<ModelElementId> modelelementids    ) {
        this.modelelementids = modelelementids;
    }


    public versioning_PrimaryVersionSpec getVersioning_primaryversionspec() {
        return versioning_primaryversionspec;
    }

    public void setVersioning_primaryversionspec(versioning_PrimaryVersionSpec versioning_primaryversionspec) {
        this.versioning_primaryversionspec = versioning_primaryversionspec;
    }
    public versioning_PrimaryVersionSpec getVersioning_primaryversionspec() {
        return versioning_primaryversionspec;
    }

    public void setVersioning_primaryversionspec(versioning_PrimaryVersionSpec versioning_primaryversionspec) {
        this.versioning_primaryversionspec = versioning_primaryversionspec;
    }
    public List<ModelElementId> getModelelementids() {
        return modelelementids;
    }

    public void addModelelementid(Modelelementid modelelementid) {
        this.modelelementids.add(modelelementid);
    }

}






import java.util.List;
import java.util.ArrayList;

public class persistence_ModelLabel extends Label, NamedElement {

    private boolean customise;
    private String format;





    private persistence_EntityOrView persistence_entityorview;




    private List<persistence_SerializationGroup> persistence_serializationgroups;




    private persistence_EntityOrView persistence_entityorview;


    public persistence_ModelLabel(
        boolean customise,        String format    ) {
        super(
        );
        this.customise = customise;
        this.format = format;
        this.persistence_serializationgroups = new ArrayList<>();
    }

    public persistence_ModelLabel(
        boolean customise,        String format        ArrayList<persistence_SerializationGroup> persistence_serializationgroups    ) {
        this.customise = customise;
        this.format = format;
        this.persistence_serializationgroups = persistence_serializationgroups;
    }

    public boolean getCustomise() {
        return customise;
    }

    public void setCustomise(boolean customise) {
        this.customise = customise;
    }
    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }

    public persistence_EntityOrView getPersistence_entityorview() {
        return persistence_entityorview;
    }

    public void setPersistence_entityorview(persistence_EntityOrView persistence_entityorview) {
        this.persistence_entityorview = persistence_entityorview;
    }
    public List<persistence_SerializationGroup> getPersistence_serializationgroups() {
        return persistence_serializationgroups;
    }

    public void addPersistence_serializationgroup(Persistence_serializationgroup persistence_serializationgroup) {
        this.persistence_serializationgroups.add(persistence_serializationgroup);
    }
    public persistence_EntityOrView getPersistence_entityorview() {
        return persistence_entityorview;
    }

    public void setPersistence_entityorview(persistence_EntityOrView persistence_entityorview) {
        this.persistence_entityorview = persistence_entityorview;
    }

}
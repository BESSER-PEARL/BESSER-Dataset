





import java.util.List;
import java.util.ArrayList;

public class persistence_ModelLabel extends NamedElement, Label {

    private String format;
    private boolean customise;





    private persistence_Entity persistence_entity;




    private List<persistence_SerializationGroup> persistence_serializationgroups;




    private persistence_Entity persistence_entity;


    public persistence_ModelLabel(
        String format,        boolean customise    ) {
        super(
        );
        this.format = format;
        this.customise = customise;
        this.persistence_serializationgroups = new ArrayList<>();
    }

    public persistence_ModelLabel(
        String format,        boolean customise        ArrayList<persistence_SerializationGroup> persistence_serializationgroups    ) {
        this.format = format;
        this.customise = customise;
        this.persistence_serializationgroups = persistence_serializationgroups;
    }

    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }
    public boolean getCustomise() {
        return customise;
    }

    public void setCustomise(boolean customise) {
        this.customise = customise;
    }

    public persistence_Entity getPersistence_entity() {
        return persistence_entity;
    }

    public void setPersistence_entity(persistence_Entity persistence_entity) {
        this.persistence_entity = persistence_entity;
    }
    public List<persistence_SerializationGroup> getPersistence_serializationgroups() {
        return persistence_serializationgroups;
    }

    public void addPersistence_serializationgroup(Persistence_serializationgroup persistence_serializationgroup) {
        this.persistence_serializationgroups.add(persistence_serializationgroup);
    }
    public persistence_Entity getPersistence_entity() {
        return persistence_entity;
    }

    public void setPersistence_entity(persistence_Entity persistence_entity) {
        this.persistence_entity = persistence_entity;
    }

}
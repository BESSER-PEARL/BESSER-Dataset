





import java.util.List;
import java.util.ArrayList;

public class dbca_Relationship extends NamedElement {

    private boolean isNullable;
    private String type;
    private String isContainment;





    private dbca_Entity dbca_entity;




    private dbca_Entity dbca_entity;




    private List<dbca_Property> dbca_propertys;


    public dbca_Relationship(
        boolean isNullable,        String type,        String isContainment    ) {
        super(
        );
        this.isNullable = isNullable;
        this.type = type;
        this.isContainment = isContainment;
        this.dbca_propertys = new ArrayList<>();
    }

    public dbca_Relationship(
        boolean isNullable,        String type,        String isContainment        ArrayList<dbca_Property> dbca_propertys    ) {
        this.isNullable = isNullable;
        this.type = type;
        this.isContainment = isContainment;
        this.dbca_propertys = dbca_propertys;
    }

    public boolean getIsnullable() {
        return isNullable;
    }

    public void setIsnullable(boolean isNullable) {
        this.isNullable = isNullable;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getIscontainment() {
        return isContainment;
    }

    public void setIscontainment(String isContainment) {
        this.isContainment = isContainment;
    }

    public dbca_Entity getDbca_entity() {
        return dbca_entity;
    }

    public void setDbca_entity(dbca_Entity dbca_entity) {
        this.dbca_entity = dbca_entity;
    }
    public dbca_Entity getDbca_entity() {
        return dbca_entity;
    }

    public void setDbca_entity(dbca_Entity dbca_entity) {
        this.dbca_entity = dbca_entity;
    }
    public List<dbca_Property> getDbca_propertys() {
        return dbca_propertys;
    }

    public void addDbca_property(Dbca_property dbca_property) {
        this.dbca_propertys.add(dbca_property);
    }

}
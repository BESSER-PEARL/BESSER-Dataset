





import java.util.List;
import java.util.ArrayList;

public class dbca_Property extends Attribute {

    private boolean isNullable;
    private String defaultValue;





    private dbca_Entity dbca_entity;


    public dbca_Property(
        boolean isNullable,        String defaultValue    ) {
        super(
        );
        this.isNullable = isNullable;
        this.defaultValue = defaultValue;
    }


    public boolean getIsnullable() {
        return isNullable;
    }

    public void setIsnullable(boolean isNullable) {
        this.isNullable = isNullable;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }

    public dbca_Entity getDbca_entity() {
        return dbca_entity;
    }

    public void setDbca_entity(dbca_Entity dbca_entity) {
        this.dbca_entity = dbca_entity;
    }

}
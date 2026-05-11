





import java.util.List;
import java.util.ArrayList;

public class dbschema_Column extends NamedElement {

    private boolean primary;
    private String type;
    private int size;





    private dbschema_Table dbschema_table;


    public dbschema_Column(
        boolean primary,        String type,        int size    ) {
        super(
        );
        this.primary = primary;
        this.type = type;
        this.size = size;
    }


    public boolean getPrimary() {
        return primary;
    }

    public void setPrimary(boolean primary) {
        this.primary = primary;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public dbschema_Table getDbschema_table() {
        return dbschema_table;
    }

    public void setDbschema_table(dbschema_Table dbschema_table) {
        this.dbschema_table = dbschema_table;
    }

}






import java.util.List;
import java.util.ArrayList;

public class dbschema_Column extends NamedElement {

    private int size;
    private String type;
    private boolean primary;





    private dbschema_Table dbschema_table;


    public dbschema_Column(
        int size,        String type,        boolean primary    ) {
        super(
        );
        this.size = size;
        this.type = type;
        this.primary = primary;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getPrimary() {
        return primary;
    }

    public void setPrimary(boolean primary) {
        this.primary = primary;
    }

    public dbschema_Table getDbschema_table() {
        return dbschema_table;
    }

    public void setDbschema_table(dbschema_Table dbschema_table) {
        this.dbschema_table = dbschema_table;
    }

}
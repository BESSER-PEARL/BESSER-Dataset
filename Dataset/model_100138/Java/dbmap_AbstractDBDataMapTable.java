





import java.util.List;
import java.util.ArrayList;

public class dbmap_AbstractDBDataMapTable  {

    private String name;
    private boolean readonly;
    private boolean minimized;
    private String tableName;



    public dbmap_AbstractDBDataMapTable(
        String name,        boolean readonly,        boolean minimized,        String tableName    ) {
        this.name = name;
        this.readonly = readonly;
        this.minimized = minimized;
        this.tableName = tableName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getReadonly() {
        return readonly;
    }

    public void setReadonly(boolean readonly) {
        this.readonly = readonly;
    }
    public boolean getMinimized() {
        return minimized;
    }

    public void setMinimized(boolean minimized) {
        this.minimized = minimized;
    }
    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }


}
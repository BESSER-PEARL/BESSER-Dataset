





import java.util.List;
import java.util.ArrayList;

public class mm_rdb_Column  {

    private String type;
    private String name;
    private String isNillable;
    private String defaultValue;





    private Table table;


    public mm_rdb_Column(
        String type,        String name,        String isNillable,        String defaultValue    ) {
        this.type = type;
        this.name = name;
        this.isNillable = isNillable;
        this.defaultValue = defaultValue;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIsnillable() {
        return isNillable;
    }

    public void setIsnillable(String isNillable) {
        this.isNillable = isNillable;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}
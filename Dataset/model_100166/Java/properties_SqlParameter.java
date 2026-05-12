





import java.util.List;
import java.util.ArrayList;

public class properties_SqlParameter  {

    private String type;
    private String name;
    private String index;





    private properties_Sql properties_sql;


    public properties_SqlParameter(
        String type,        String name,        String index    ) {
        this.type = type;
        this.name = name;
        this.index = index;
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
    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }

    public properties_Sql getProperties_sql() {
        return properties_sql;
    }

    public void setProperties_sql(properties_Sql properties_sql) {
        this.properties_sql = properties_sql;
    }

}
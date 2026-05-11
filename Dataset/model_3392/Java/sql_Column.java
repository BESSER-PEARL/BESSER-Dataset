





import java.util.List;
import java.util.ArrayList;

public class sql_Column  {

    private boolean PrimaryKey;
    private String name;
    private String type;





    private sql_Table sql_table;


    public sql_Column(
        boolean PrimaryKey,        String name,        String type    ) {
        this.PrimaryKey = PrimaryKey;
        this.name = name;
        this.type = type;
    }


    public boolean getPrimarykey() {
        return PrimaryKey;
    }

    public void setPrimarykey(boolean PrimaryKey) {
        this.PrimaryKey = PrimaryKey;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public sql_Table getSql_table() {
        return sql_table;
    }

    public void setSql_table(sql_Table sql_table) {
        this.sql_table = sql_table;
    }

}
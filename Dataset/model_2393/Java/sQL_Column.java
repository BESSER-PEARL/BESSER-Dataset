





import java.util.List;
import java.util.ArrayList;

public class sQL_Column  {

    private String type;
    private boolean isNull;
    private String name;





    private sQL_Table sql_table;


    public sQL_Column(
        String type,        boolean isNull,        String name    ) {
        this.type = type;
        this.isNull = isNull;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getIsnull() {
        return isNull;
    }

    public void setIsnull(boolean isNull) {
        this.isNull = isNull;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sQL_Table getSql_table() {
        return sql_table;
    }

    public void setSql_table(sQL_Table sql_table) {
        this.sql_table = sql_table;
    }

}
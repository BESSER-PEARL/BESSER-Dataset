





import java.util.List;
import java.util.ArrayList;

public class genSql_Column  {

    private String SQLType;
    private String name;





    private genSql_Table gensql_table;


    public genSql_Column(
        String SQLType,        String name    ) {
        this.SQLType = SQLType;
        this.name = name;
    }


    public String getSqltype() {
        return SQLType;
    }

    public void setSqltype(String SQLType) {
        this.SQLType = SQLType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public genSql_Table getGensql_table() {
        return gensql_table;
    }

    public void setGensql_table(genSql_Table gensql_table) {
        this.gensql_table = gensql_table;
    }

}
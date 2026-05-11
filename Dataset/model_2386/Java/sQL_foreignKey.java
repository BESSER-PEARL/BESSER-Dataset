





import java.util.List;
import java.util.ArrayList;

public class sQL_foreignKey  {

    private String name;





    private sQL_column sql_column;


    public sQL_foreignKey(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sQL_column getSql_column() {
        return sql_column;
    }

    public void setSql_column(sQL_column sql_column) {
        this.sql_column = sql_column;
    }

}
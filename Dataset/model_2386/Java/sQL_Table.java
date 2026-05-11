





import java.util.List;
import java.util.ArrayList;

public class sQL_Table  {

    private String name;





    private List<sQL_foreignKey> sql_foreignkeys;




    private sQL_DataBase sql_database;




    private sQL_primaryKey sql_primarykey;




    private List<sQL_column> sql_columns;




    private sQL_foreignKey sql_foreignkey;


    public sQL_Table(
        String name    ) {
        this.name = name;
        this.sql_foreignkeys = new ArrayList<>();
        this.sql_columns = new ArrayList<>();
    }

    public sQL_Table(
        String name        ArrayList<sQL_foreignKey> sql_foreignkeys,        ArrayList<sQL_column> sql_columns    ) {
        this.name = name;
        this.sql_foreignkeys = sql_foreignkeys;
        this.sql_columns = sql_columns;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<sQL_foreignKey> getSql_foreignkeys() {
        return sql_foreignkeys;
    }

    public void addSql_foreignkey(Sql_foreignkey sql_foreignkey) {
        this.sql_foreignkeys.add(sql_foreignkey);
    }
    public sQL_DataBase getSql_database() {
        return sql_database;
    }

    public void setSql_database(sQL_DataBase sql_database) {
        this.sql_database = sql_database;
    }
    public sQL_primaryKey getSql_primarykey() {
        return sql_primarykey;
    }

    public void setSql_primarykey(sQL_primaryKey sql_primarykey) {
        this.sql_primarykey = sql_primarykey;
    }
    public List<sQL_column> getSql_columns() {
        return sql_columns;
    }

    public void addSql_column(Sql_column sql_column) {
        this.sql_columns.add(sql_column);
    }
    public sQL_foreignKey getSql_foreignkey() {
        return sql_foreignkey;
    }

    public void setSql_foreignkey(sQL_foreignKey sql_foreignkey) {
        this.sql_foreignkey = sql_foreignkey;
    }

}
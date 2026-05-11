





import java.util.List;
import java.util.ArrayList;

public class sQL_Table  {

    private String name;





    private List<sQL_ForeignKey> sql_foreignkeys;




    private sQL_ForeignKey sql_foreignkey;




    private sQL_Database sql_database;


    public sQL_Table(
        String name    ) {
        this.name = name;
        this.sql_foreignkeys = new ArrayList<>();
    }

    public sQL_Table(
        String name        ArrayList<sQL_ForeignKey> sql_foreignkeys    ) {
        this.name = name;
        this.sql_foreignkeys = sql_foreignkeys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<sQL_ForeignKey> getSql_foreignkeys() {
        return sql_foreignkeys;
    }

    public void addSql_foreignkey(Sql_foreignkey sql_foreignkey) {
        this.sql_foreignkeys.add(sql_foreignkey);
    }
    public sQL_ForeignKey getSql_foreignkey() {
        return sql_foreignkey;
    }

    public void setSql_foreignkey(sQL_ForeignKey sql_foreignkey) {
        this.sql_foreignkey = sql_foreignkey;
    }
    public sQL_Database getSql_database() {
        return sql_database;
    }

    public void setSql_database(sQL_Database sql_database) {
        this.sql_database = sql_database;
    }

}
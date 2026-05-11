





import java.util.List;
import java.util.ArrayList;

public class Sql_Table extends NamedElement {






    private Sql_Database sql_database;


    public Sql_Table(
    ) {
        super(
        );
    }



    public Sql_Database getSql_database() {
        return sql_database;
    }

    public void setSql_database(Sql_Database sql_database) {
        this.sql_database = sql_database;
    }

}
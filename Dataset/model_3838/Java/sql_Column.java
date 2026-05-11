





import java.util.List;
import java.util.ArrayList;

public class sql_Column extends NamedElement {






    private sql_SelectQuery sql_selectquery;




    private sql_Table sql_table;


    public sql_Column(
    ) {
        super(
        );
    }



    public sql_SelectQuery getSql_selectquery() {
        return sql_selectquery;
    }

    public void setSql_selectquery(sql_SelectQuery sql_selectquery) {
        this.sql_selectquery = sql_selectquery;
    }
    public sql_Table getSql_table() {
        return sql_table;
    }

    public void setSql_table(sql_Table sql_table) {
        this.sql_table = sql_table;
    }

}
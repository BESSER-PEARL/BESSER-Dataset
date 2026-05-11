





import java.util.List;
import java.util.ArrayList;

public class sql_Table extends NamedElement {






    private sql_SelectQuery sql_selectquery;




    private sql_Model sql_model;


    public sql_Table(
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
    public sql_Model getSql_model() {
        return sql_model;
    }

    public void setSql_model(sql_Model sql_model) {
        this.sql_model = sql_model;
    }

}
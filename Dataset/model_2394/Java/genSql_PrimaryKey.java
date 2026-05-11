





import java.util.List;
import java.util.ArrayList;

public class genSql_PrimaryKey  {






    private genSql_Table gensql_table;




    private List<genSql_Column> gensql_columns;


    public genSql_PrimaryKey(
    ) {
        this.gensql_columns = new ArrayList<>();
    }

    public genSql_PrimaryKey(
        ArrayList<genSql_Column> gensql_columns    ) {
        this.gensql_columns = gensql_columns;
    }


    public genSql_Table getGensql_table() {
        return gensql_table;
    }

    public void setGensql_table(genSql_Table gensql_table) {
        this.gensql_table = gensql_table;
    }
    public List<genSql_Column> getGensql_columns() {
        return gensql_columns;
    }

    public void addGensql_column(Gensql_column gensql_column) {
        this.gensql_columns.add(gensql_column);
    }

}
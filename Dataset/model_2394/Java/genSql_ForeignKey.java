





import java.util.List;
import java.util.ArrayList;

public class genSql_ForeignKey  {






    private List<genSql_Column> gensql_columns;




    private List<genSql_Column> gensql_columns;




    private genSql_Table gensql_table;




    private genSql_Table gensql_table;


    public genSql_ForeignKey(
    ) {
        this.gensql_columns = new ArrayList<>();
        this.gensql_columns = new ArrayList<>();
    }

    public genSql_ForeignKey(
        ArrayList<genSql_Column> gensql_columns,        ArrayList<genSql_Column> gensql_columns    ) {
        this.gensql_columns = gensql_columns;
        this.gensql_columns = gensql_columns;
    }


    public List<genSql_Column> getGensql_columns() {
        return gensql_columns;
    }

    public void addGensql_column(Gensql_column gensql_column) {
        this.gensql_columns.add(gensql_column);
    }
    public List<genSql_Column> getGensql_columns() {
        return gensql_columns;
    }

    public void addGensql_column(Gensql_column gensql_column) {
        this.gensql_columns.add(gensql_column);
    }
    public genSql_Table getGensql_table() {
        return gensql_table;
    }

    public void setGensql_table(genSql_Table gensql_table) {
        this.gensql_table = gensql_table;
    }
    public genSql_Table getGensql_table() {
        return gensql_table;
    }

    public void setGensql_table(genSql_Table gensql_table) {
        this.gensql_table = gensql_table;
    }

}
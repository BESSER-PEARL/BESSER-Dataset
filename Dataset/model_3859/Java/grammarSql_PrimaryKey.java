





import java.util.List;
import java.util.ArrayList;

public class grammarSql_PrimaryKey  {






    private List<grammarSql_Column> grammarsql_columns;


    public grammarSql_PrimaryKey(
    ) {
        this.grammarsql_columns = new ArrayList<>();
    }

    public grammarSql_PrimaryKey(
        ArrayList<grammarSql_Column> grammarsql_columns    ) {
        this.grammarsql_columns = grammarsql_columns;
    }


    public List<grammarSql_Column> getGrammarsql_columns() {
        return grammarsql_columns;
    }

    public void addGrammarsql_column(Grammarsql_column grammarsql_column) {
        this.grammarsql_columns.add(grammarsql_column);
    }

}






import java.util.List;
import java.util.ArrayList;

public class grammarSql_Reference  {






    private grammarSql_ForeignKey grammarsql_foreignkey;




    private List<grammarSql_Column> grammarsql_columns;




    private List<grammarSql_Table> grammarsql_tables;


    public grammarSql_Reference(
    ) {
        this.grammarsql_columns = new ArrayList<>();
        this.grammarsql_tables = new ArrayList<>();
    }

    public grammarSql_Reference(
        ArrayList<grammarSql_Column> grammarsql_columns,        ArrayList<grammarSql_Table> grammarsql_tables    ) {
        this.grammarsql_columns = grammarsql_columns;
        this.grammarsql_tables = grammarsql_tables;
    }


    public grammarSql_ForeignKey getGrammarsql_foreignkey() {
        return grammarsql_foreignkey;
    }

    public void setGrammarsql_foreignkey(grammarSql_ForeignKey grammarsql_foreignkey) {
        this.grammarsql_foreignkey = grammarsql_foreignkey;
    }
    public List<grammarSql_Column> getGrammarsql_columns() {
        return grammarsql_columns;
    }

    public void addGrammarsql_column(Grammarsql_column grammarsql_column) {
        this.grammarsql_columns.add(grammarsql_column);
    }
    public List<grammarSql_Table> getGrammarsql_tables() {
        return grammarsql_tables;
    }

    public void addGrammarsql_table(Grammarsql_table grammarsql_table) {
        this.grammarsql_tables.add(grammarsql_table);
    }

}
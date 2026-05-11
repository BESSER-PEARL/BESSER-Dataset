





import java.util.List;
import java.util.ArrayList;

public class sqlCrudGenerator_PrimaryKey  {






    private List<sqlCrudGenerator_Column> sqlcrudgenerator_columns;




    private sqlCrudGenerator_Table sqlcrudgenerator_table;


    public sqlCrudGenerator_PrimaryKey(
    ) {
        this.sqlcrudgenerator_columns = new ArrayList<>();
    }

    public sqlCrudGenerator_PrimaryKey(
        ArrayList<sqlCrudGenerator_Column> sqlcrudgenerator_columns    ) {
        this.sqlcrudgenerator_columns = sqlcrudgenerator_columns;
    }


    public List<sqlCrudGenerator_Column> getSqlcrudgenerator_columns() {
        return sqlcrudgenerator_columns;
    }

    public void addSqlcrudgenerator_column(Sqlcrudgenerator_column sqlcrudgenerator_column) {
        this.sqlcrudgenerator_columns.add(sqlcrudgenerator_column);
    }
    public sqlCrudGenerator_Table getSqlcrudgenerator_table() {
        return sqlcrudgenerator_table;
    }

    public void setSqlcrudgenerator_table(sqlCrudGenerator_Table sqlcrudgenerator_table) {
        this.sqlcrudgenerator_table = sqlcrudgenerator_table;
    }

}
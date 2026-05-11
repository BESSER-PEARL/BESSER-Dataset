





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_AlterTableAddColumnStatement extends DDLStatement {






    private sqliteModel_ColumnSource sqlitemodel_columnsource;


    public sqliteModel_AlterTableAddColumnStatement(
    ) {
        super(
        );
    }



    public sqliteModel_ColumnSource getSqlitemodel_columnsource() {
        return sqlitemodel_columnsource;
    }

    public void setSqlitemodel_columnsource(sqliteModel_ColumnSource sqlitemodel_columnsource) {
        this.sqlitemodel_columnsource = sqlitemodel_columnsource;
    }

}
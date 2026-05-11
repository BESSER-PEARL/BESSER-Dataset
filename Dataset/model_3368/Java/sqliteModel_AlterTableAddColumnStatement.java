





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_AlterTableAddColumnStatement extends DDLStatement {






    private sqliteModel_TableDefinition sqlitemodel_tabledefinition;




    private sqliteModel_ColumnSource sqlitemodel_columnsource;


    public sqliteModel_AlterTableAddColumnStatement(
    ) {
        super(
        );
    }



    public sqliteModel_TableDefinition getSqlitemodel_tabledefinition() {
        return sqlitemodel_tabledefinition;
    }

    public void setSqlitemodel_tabledefinition(sqliteModel_TableDefinition sqlitemodel_tabledefinition) {
        this.sqlitemodel_tabledefinition = sqlitemodel_tabledefinition;
    }
    public sqliteModel_ColumnSource getSqlitemodel_columnsource() {
        return sqlitemodel_columnsource;
    }

    public void setSqlitemodel_columnsource(sqliteModel_ColumnSource sqlitemodel_columnsource) {
        this.sqlitemodel_columnsource = sqlitemodel_columnsource;
    }

}






import java.util.List;
import java.util.ArrayList;

public class sqliteModel_InitBlock  {






    private sqliteModel_DatabaseBlock sqlitemodel_databaseblock;




    private List<sqliteModel_DDLStatement> sqlitemodel_ddlstatements;


    public sqliteModel_InitBlock(
    ) {
        this.sqlitemodel_ddlstatements = new ArrayList<>();
    }

    public sqliteModel_InitBlock(
        ArrayList<sqliteModel_DDLStatement> sqlitemodel_ddlstatements    ) {
        this.sqlitemodel_ddlstatements = sqlitemodel_ddlstatements;
    }


    public sqliteModel_DatabaseBlock getSqlitemodel_databaseblock() {
        return sqlitemodel_databaseblock;
    }

    public void setSqlitemodel_databaseblock(sqliteModel_DatabaseBlock sqlitemodel_databaseblock) {
        this.sqlitemodel_databaseblock = sqlitemodel_databaseblock;
    }
    public List<sqliteModel_DDLStatement> getSqlitemodel_ddlstatements() {
        return sqlitemodel_ddlstatements;
    }

    public void addSqlitemodel_ddlstatement(Sqlitemodel_ddlstatement sqlitemodel_ddlstatement) {
        this.sqlitemodel_ddlstatements.add(sqlitemodel_ddlstatement);
    }

}
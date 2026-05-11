





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_ConfigBlock  {






    private List<sqliteModel_ConfigurationStatement> sqlitemodel_configurationstatements;




    private sqliteModel_DatabaseBlock sqlitemodel_databaseblock;


    public sqliteModel_ConfigBlock(
    ) {
        this.sqlitemodel_configurationstatements = new ArrayList<>();
    }

    public sqliteModel_ConfigBlock(
        ArrayList<sqliteModel_ConfigurationStatement> sqlitemodel_configurationstatements    ) {
        this.sqlitemodel_configurationstatements = sqlitemodel_configurationstatements;
    }


    public List<sqliteModel_ConfigurationStatement> getSqlitemodel_configurationstatements() {
        return sqlitemodel_configurationstatements;
    }

    public void addSqlitemodel_configurationstatement(Sqlitemodel_configurationstatement sqlitemodel_configurationstatement) {
        this.sqlitemodel_configurationstatements.add(sqlitemodel_configurationstatement);
    }
    public sqliteModel_DatabaseBlock getSqlitemodel_databaseblock() {
        return sqlitemodel_databaseblock;
    }

    public void setSqlitemodel_databaseblock(sqliteModel_DatabaseBlock sqlitemodel_databaseblock) {
        this.sqlitemodel_databaseblock = sqlitemodel_databaseblock;
    }

}
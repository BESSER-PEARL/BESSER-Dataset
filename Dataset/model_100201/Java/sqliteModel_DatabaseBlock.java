





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_DatabaseBlock  {

    private String name;





    private sqliteModel_ConfigBlock sqlitemodel_configblock;




    private List<sqliteModel_MigrationBlock> sqlitemodel_migrationblocks;




    private sqliteModel_InitBlock sqlitemodel_initblock;




    private sqliteModel_Model sqlitemodel_model;


    public sqliteModel_DatabaseBlock(
        String name    ) {
        this.name = name;
        this.sqlitemodel_migrationblocks = new ArrayList<>();
    }

    public sqliteModel_DatabaseBlock(
        String name        ArrayList<sqliteModel_MigrationBlock> sqlitemodel_migrationblocks    ) {
        this.name = name;
        this.sqlitemodel_migrationblocks = sqlitemodel_migrationblocks;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sqliteModel_ConfigBlock getSqlitemodel_configblock() {
        return sqlitemodel_configblock;
    }

    public void setSqlitemodel_configblock(sqliteModel_ConfigBlock sqlitemodel_configblock) {
        this.sqlitemodel_configblock = sqlitemodel_configblock;
    }
    public List<sqliteModel_MigrationBlock> getSqlitemodel_migrationblocks() {
        return sqlitemodel_migrationblocks;
    }

    public void addSqlitemodel_migrationblock(Sqlitemodel_migrationblock sqlitemodel_migrationblock) {
        this.sqlitemodel_migrationblocks.add(sqlitemodel_migrationblock);
    }
    public sqliteModel_InitBlock getSqlitemodel_initblock() {
        return sqlitemodel_initblock;
    }

    public void setSqlitemodel_initblock(sqliteModel_InitBlock sqlitemodel_initblock) {
        this.sqlitemodel_initblock = sqlitemodel_initblock;
    }
    public sqliteModel_Model getSqlitemodel_model() {
        return sqlitemodel_model;
    }

    public void setSqlitemodel_model(sqliteModel_Model sqlitemodel_model) {
        this.sqlitemodel_model = sqlitemodel_model;
    }

}
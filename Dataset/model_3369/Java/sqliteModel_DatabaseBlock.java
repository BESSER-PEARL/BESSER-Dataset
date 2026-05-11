





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_DatabaseBlock  {

    private String name;





    private sqliteModel_Model sqlitemodel_model;




    private List<sqliteModel_MigrationBlock> sqlitemodel_migrationblocks;


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

    public sqliteModel_Model getSqlitemodel_model() {
        return sqlitemodel_model;
    }

    public void setSqlitemodel_model(sqliteModel_Model sqlitemodel_model) {
        this.sqlitemodel_model = sqlitemodel_model;
    }
    public List<sqliteModel_MigrationBlock> getSqlitemodel_migrationblocks() {
        return sqlitemodel_migrationblocks;
    }

    public void addSqlitemodel_migrationblock(Sqlitemodel_migrationblock sqlitemodel_migrationblock) {
        this.sqlitemodel_migrationblocks.add(sqlitemodel_migrationblock);
    }

}
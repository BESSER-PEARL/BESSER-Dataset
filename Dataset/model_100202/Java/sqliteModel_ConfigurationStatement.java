





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_ConfigurationStatement  {

    private String name;





    private sqliteModel_ConfigBlock sqlitemodel_configblock;


    public sqliteModel_ConfigurationStatement(
        String name    ) {
        this.name = name;
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

}
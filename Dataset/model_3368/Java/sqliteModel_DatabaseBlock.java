





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_DatabaseBlock  {

    private String name;





    private sqliteModel_Model sqlitemodel_model;


    public sqliteModel_DatabaseBlock(
        String name    ) {
        this.name = name;
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

}
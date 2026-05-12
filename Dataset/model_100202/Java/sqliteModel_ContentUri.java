





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_ContentUri  {

    private String type;





    private sqliteModel_ActionStatement sqlitemodel_actionstatement;


    public sqliteModel_ContentUri(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public sqliteModel_ActionStatement getSqlitemodel_actionstatement() {
        return sqlitemodel_actionstatement;
    }

    public void setSqlitemodel_actionstatement(sqliteModel_ActionStatement sqlitemodel_actionstatement) {
        this.sqlitemodel_actionstatement = sqlitemodel_actionstatement;
    }

}
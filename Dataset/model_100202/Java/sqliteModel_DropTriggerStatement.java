





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_DropTriggerStatement extends DDLStatement {

    private boolean ifExists;





    private sqliteModel_CreateTriggerStatement sqlitemodel_createtriggerstatement;


    public sqliteModel_DropTriggerStatement(
        boolean ifExists    ) {
        super(
        );
        this.ifExists = ifExists;
    }


    public boolean getIfexists() {
        return ifExists;
    }

    public void setIfexists(boolean ifExists) {
        this.ifExists = ifExists;
    }

    public sqliteModel_CreateTriggerStatement getSqlitemodel_createtriggerstatement() {
        return sqlitemodel_createtriggerstatement;
    }

    public void setSqlitemodel_createtriggerstatement(sqliteModel_CreateTriggerStatement sqlitemodel_createtriggerstatement) {
        this.sqlitemodel_createtriggerstatement = sqlitemodel_createtriggerstatement;
    }

}






import java.util.List;
import java.util.ArrayList;

public class sqliteModel_DropIndexStatement extends DDLStatement {

    private boolean ifExists;





    private sqliteModel_CreateIndexStatement sqlitemodel_createindexstatement;


    public sqliteModel_DropIndexStatement(
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

    public sqliteModel_CreateIndexStatement getSqlitemodel_createindexstatement() {
        return sqlitemodel_createindexstatement;
    }

    public void setSqlitemodel_createindexstatement(sqliteModel_CreateIndexStatement sqlitemodel_createindexstatement) {
        this.sqlitemodel_createindexstatement = sqlitemodel_createindexstatement;
    }

}
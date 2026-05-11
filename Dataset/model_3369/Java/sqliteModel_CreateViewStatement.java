





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_CreateViewStatement extends TableDefinition {

    private boolean temporary;





    private sqliteModel_SelectStatement sqlitemodel_selectstatement;




    private sqliteModel_DropViewStatement sqlitemodel_dropviewstatement;


    public sqliteModel_CreateViewStatement(
        boolean temporary    ) {
        super(
        );
        this.temporary = temporary;
    }


    public boolean getTemporary() {
        return temporary;
    }

    public void setTemporary(boolean temporary) {
        this.temporary = temporary;
    }

    public sqliteModel_SelectStatement getSqlitemodel_selectstatement() {
        return sqlitemodel_selectstatement;
    }

    public void setSqlitemodel_selectstatement(sqliteModel_SelectStatement sqlitemodel_selectstatement) {
        this.sqlitemodel_selectstatement = sqlitemodel_selectstatement;
    }
    public sqliteModel_DropViewStatement getSqlitemodel_dropviewstatement() {
        return sqlitemodel_dropviewstatement;
    }

    public void setSqlitemodel_dropviewstatement(sqliteModel_DropViewStatement sqlitemodel_dropviewstatement) {
        this.sqlitemodel_dropviewstatement = sqlitemodel_dropviewstatement;
    }

}
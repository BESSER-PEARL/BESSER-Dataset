





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_TableDefinition extends DDLStatement {

    private String name;





    private sqliteModel_DropTableStatement sqlitemodel_droptablestatement;




    private sqliteModel_DeleteStatement sqlitemodel_deletestatement;




    private sqliteModel_AlterTableAddColumnStatement sqlitemodel_altertableaddcolumnstatement;




    private sqliteModel_UpdateStatement sqlitemodel_updatestatement;




    private sqliteModel_InsertStatement sqlitemodel_insertstatement;


    public sqliteModel_TableDefinition(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sqliteModel_DropTableStatement getSqlitemodel_droptablestatement() {
        return sqlitemodel_droptablestatement;
    }

    public void setSqlitemodel_droptablestatement(sqliteModel_DropTableStatement sqlitemodel_droptablestatement) {
        this.sqlitemodel_droptablestatement = sqlitemodel_droptablestatement;
    }
    public sqliteModel_DeleteStatement getSqlitemodel_deletestatement() {
        return sqlitemodel_deletestatement;
    }

    public void setSqlitemodel_deletestatement(sqliteModel_DeleteStatement sqlitemodel_deletestatement) {
        this.sqlitemodel_deletestatement = sqlitemodel_deletestatement;
    }
    public sqliteModel_AlterTableAddColumnStatement getSqlitemodel_altertableaddcolumnstatement() {
        return sqlitemodel_altertableaddcolumnstatement;
    }

    public void setSqlitemodel_altertableaddcolumnstatement(sqliteModel_AlterTableAddColumnStatement sqlitemodel_altertableaddcolumnstatement) {
        this.sqlitemodel_altertableaddcolumnstatement = sqlitemodel_altertableaddcolumnstatement;
    }
    public sqliteModel_UpdateStatement getSqlitemodel_updatestatement() {
        return sqlitemodel_updatestatement;
    }

    public void setSqlitemodel_updatestatement(sqliteModel_UpdateStatement sqlitemodel_updatestatement) {
        this.sqlitemodel_updatestatement = sqlitemodel_updatestatement;
    }
    public sqliteModel_InsertStatement getSqlitemodel_insertstatement() {
        return sqlitemodel_insertstatement;
    }

    public void setSqlitemodel_insertstatement(sqliteModel_InsertStatement sqlitemodel_insertstatement) {
        this.sqlitemodel_insertstatement = sqlitemodel_insertstatement;
    }

}
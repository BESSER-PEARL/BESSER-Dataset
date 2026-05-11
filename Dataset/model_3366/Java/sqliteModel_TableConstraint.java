





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_TableConstraint  {

    private String name;





    private sqliteModel_CreateTableStatement sqlitemodel_createtablestatement;


    public sqliteModel_TableConstraint(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sqliteModel_CreateTableStatement getSqlitemodel_createtablestatement() {
        return sqlitemodel_createtablestatement;
    }

    public void setSqlitemodel_createtablestatement(sqliteModel_CreateTableStatement sqlitemodel_createtablestatement) {
        this.sqlitemodel_createtablestatement = sqlitemodel_createtablestatement;
    }

}
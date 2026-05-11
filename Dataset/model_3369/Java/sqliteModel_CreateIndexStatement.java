





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_CreateIndexStatement extends DDLStatement {

    private boolean unique;
    private String name;





    private sqliteModel_TableDefinition sqlitemodel_tabledefinition;




    private sqliteModel_DropIndexStatement sqlitemodel_dropindexstatement;


    public sqliteModel_CreateIndexStatement(
        boolean unique,        String name    ) {
        super(
        );
        this.unique = unique;
        this.name = name;
    }


    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sqliteModel_TableDefinition getSqlitemodel_tabledefinition() {
        return sqlitemodel_tabledefinition;
    }

    public void setSqlitemodel_tabledefinition(sqliteModel_TableDefinition sqlitemodel_tabledefinition) {
        this.sqlitemodel_tabledefinition = sqlitemodel_tabledefinition;
    }
    public sqliteModel_DropIndexStatement getSqlitemodel_dropindexstatement() {
        return sqlitemodel_dropindexstatement;
    }

    public void setSqlitemodel_dropindexstatement(sqliteModel_DropIndexStatement sqlitemodel_dropindexstatement) {
        this.sqlitemodel_dropindexstatement = sqlitemodel_dropindexstatement;
    }

}
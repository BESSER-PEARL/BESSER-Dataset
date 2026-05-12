





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_CreateIndexStatement extends DDLStatement {

    private String name;
    private boolean unique;





    private sqliteModel_DropIndexStatement sqlitemodel_dropindexstatement;




    private sqliteModel_TableDefinition sqlitemodel_tabledefinition;


    public sqliteModel_CreateIndexStatement(
        String name,        boolean unique    ) {
        super(
        );
        this.name = name;
        this.unique = unique;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }

    public sqliteModel_DropIndexStatement getSqlitemodel_dropindexstatement() {
        return sqlitemodel_dropindexstatement;
    }

    public void setSqlitemodel_dropindexstatement(sqliteModel_DropIndexStatement sqlitemodel_dropindexstatement) {
        this.sqlitemodel_dropindexstatement = sqlitemodel_dropindexstatement;
    }
    public sqliteModel_TableDefinition getSqlitemodel_tabledefinition() {
        return sqlitemodel_tabledefinition;
    }

    public void setSqlitemodel_tabledefinition(sqliteModel_TableDefinition sqlitemodel_tabledefinition) {
        this.sqlitemodel_tabledefinition = sqlitemodel_tabledefinition;
    }

}
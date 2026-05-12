





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_ColumnSource  {

    private String name;





    private sqliteModel_AlterTableAddColumnStatement sqlitemodel_altertableaddcolumnstatement;




    private sqliteModel_CreateTableStatement sqlitemodel_createtablestatement;




    private sqliteModel_ColumnSourceRef sqlitemodel_columnsourceref;




    private sqliteModel_OldColumn sqlitemodel_oldcolumn;




    private sqliteModel_SelectList sqlitemodel_selectlist;




    private sqliteModel_NewColumn sqlitemodel_newcolumn;


    public sqliteModel_ColumnSource(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sqliteModel_AlterTableAddColumnStatement getSqlitemodel_altertableaddcolumnstatement() {
        return sqlitemodel_altertableaddcolumnstatement;
    }

    public void setSqlitemodel_altertableaddcolumnstatement(sqliteModel_AlterTableAddColumnStatement sqlitemodel_altertableaddcolumnstatement) {
        this.sqlitemodel_altertableaddcolumnstatement = sqlitemodel_altertableaddcolumnstatement;
    }
    public sqliteModel_CreateTableStatement getSqlitemodel_createtablestatement() {
        return sqlitemodel_createtablestatement;
    }

    public void setSqlitemodel_createtablestatement(sqliteModel_CreateTableStatement sqlitemodel_createtablestatement) {
        this.sqlitemodel_createtablestatement = sqlitemodel_createtablestatement;
    }
    public sqliteModel_ColumnSourceRef getSqlitemodel_columnsourceref() {
        return sqlitemodel_columnsourceref;
    }

    public void setSqlitemodel_columnsourceref(sqliteModel_ColumnSourceRef sqlitemodel_columnsourceref) {
        this.sqlitemodel_columnsourceref = sqlitemodel_columnsourceref;
    }
    public sqliteModel_OldColumn getSqlitemodel_oldcolumn() {
        return sqlitemodel_oldcolumn;
    }

    public void setSqlitemodel_oldcolumn(sqliteModel_OldColumn sqlitemodel_oldcolumn) {
        this.sqlitemodel_oldcolumn = sqlitemodel_oldcolumn;
    }
    public sqliteModel_SelectList getSqlitemodel_selectlist() {
        return sqlitemodel_selectlist;
    }

    public void setSqlitemodel_selectlist(sqliteModel_SelectList sqlitemodel_selectlist) {
        this.sqlitemodel_selectlist = sqlitemodel_selectlist;
    }
    public sqliteModel_NewColumn getSqlitemodel_newcolumn() {
        return sqlitemodel_newcolumn;
    }

    public void setSqlitemodel_newcolumn(sqliteModel_NewColumn sqlitemodel_newcolumn) {
        this.sqlitemodel_newcolumn = sqlitemodel_newcolumn;
    }

}
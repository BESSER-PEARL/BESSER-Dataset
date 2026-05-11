





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_ColumnSourceRef extends Expression {

    private boolean all;





    private sqliteModel_SelectSource sqlitemodel_selectsource;




    private sqliteModel_ColumnSource sqlitemodel_columnsource;


    public sqliteModel_ColumnSourceRef(
        boolean all    ) {
        super(
        );
        this.all = all;
    }


    public boolean getAll() {
        return all;
    }

    public void setAll(boolean all) {
        this.all = all;
    }

    public sqliteModel_SelectSource getSqlitemodel_selectsource() {
        return sqlitemodel_selectsource;
    }

    public void setSqlitemodel_selectsource(sqliteModel_SelectSource sqlitemodel_selectsource) {
        this.sqlitemodel_selectsource = sqlitemodel_selectsource;
    }
    public sqliteModel_ColumnSource getSqlitemodel_columnsource() {
        return sqlitemodel_columnsource;
    }

    public void setSqlitemodel_columnsource(sqliteModel_ColumnSource sqlitemodel_columnsource) {
        this.sqlitemodel_columnsource = sqlitemodel_columnsource;
    }

}
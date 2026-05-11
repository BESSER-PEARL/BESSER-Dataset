





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_ColumnSource  {

    private String name;





    private sqliteModel_SelectList sqlitemodel_selectlist;


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

    public sqliteModel_SelectList getSqlitemodel_selectlist() {
        return sqlitemodel_selectlist;
    }

    public void setSqlitemodel_selectlist(sqliteModel_SelectList sqlitemodel_selectlist) {
        this.sqlitemodel_selectlist = sqlitemodel_selectlist;
    }

}






import java.util.List;
import java.util.ArrayList;

public class sqls_SelectList  {






    private sqls_Select sqls_select;




    private List<sqls_ResultColumn> sqls_resultcolumns;


    public sqls_SelectList(
    ) {
        this.sqls_resultcolumns = new ArrayList<>();
    }

    public sqls_SelectList(
        ArrayList<sqls_ResultColumn> sqls_resultcolumns    ) {
        this.sqls_resultcolumns = sqls_resultcolumns;
    }


    public sqls_Select getSqls_select() {
        return sqls_select;
    }

    public void setSqls_select(sqls_Select sqls_select) {
        this.sqls_select = sqls_select;
    }
    public List<sqls_ResultColumn> getSqls_resultcolumns() {
        return sqls_resultcolumns;
    }

    public void addSqls_resultcolumn(Sqls_resultcolumn sqls_resultcolumn) {
        this.sqls_resultcolumns.add(sqls_resultcolumn);
    }

}
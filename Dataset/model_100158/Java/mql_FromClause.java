





import java.util.List;
import java.util.ArrayList;

public class mql_FromClause  {






    private List<mql_FromEntry> mql_fromentrys;




    private mql_SelectFromClause mql_selectfromclause;




    private mql_DeleteClause mql_deleteclause;


    public mql_FromClause(
    ) {
        this.mql_fromentrys = new ArrayList<>();
    }

    public mql_FromClause(
        ArrayList<mql_FromEntry> mql_fromentrys    ) {
        this.mql_fromentrys = mql_fromentrys;
    }


    public List<mql_FromEntry> getMql_fromentrys() {
        return mql_fromentrys;
    }

    public void addMql_fromentry(Mql_fromentry mql_fromentry) {
        this.mql_fromentrys.add(mql_fromentry);
    }
    public mql_SelectFromClause getMql_selectfromclause() {
        return mql_selectfromclause;
    }

    public void setMql_selectfromclause(mql_SelectFromClause mql_selectfromclause) {
        this.mql_selectfromclause = mql_selectfromclause;
    }
    public mql_DeleteClause getMql_deleteclause() {
        return mql_deleteclause;
    }

    public void setMql_deleteclause(mql_DeleteClause mql_deleteclause) {
        this.mql_deleteclause = mql_deleteclause;
    }

}






import java.util.List;
import java.util.ArrayList;

public class mql_UpdateClause  {






    private mql_UpdateStatement mql_updatestatement;




    private List<mql_FromEntry> mql_fromentrys;


    public mql_UpdateClause(
    ) {
        this.mql_fromentrys = new ArrayList<>();
    }

    public mql_UpdateClause(
        ArrayList<mql_FromEntry> mql_fromentrys    ) {
        this.mql_fromentrys = mql_fromentrys;
    }


    public mql_UpdateStatement getMql_updatestatement() {
        return mql_updatestatement;
    }

    public void setMql_updatestatement(mql_UpdateStatement mql_updatestatement) {
        this.mql_updatestatement = mql_updatestatement;
    }
    public List<mql_FromEntry> getMql_fromentrys() {
        return mql_fromentrys;
    }

    public void addMql_fromentry(Mql_fromentry mql_fromentry) {
        this.mql_fromentrys.add(mql_fromentry);
    }

}
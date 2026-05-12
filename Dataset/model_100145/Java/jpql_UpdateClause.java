





import java.util.List;
import java.util.ArrayList;

public class jpql_UpdateClause  {






    private List<jpql_FromEntry> jpql_fromentrys;




    private jpql_UpdateStatement jpql_updatestatement;


    public jpql_UpdateClause(
    ) {
        this.jpql_fromentrys = new ArrayList<>();
    }

    public jpql_UpdateClause(
        ArrayList<jpql_FromEntry> jpql_fromentrys    ) {
        this.jpql_fromentrys = jpql_fromentrys;
    }


    public List<jpql_FromEntry> getJpql_fromentrys() {
        return jpql_fromentrys;
    }

    public void addJpql_fromentry(Jpql_fromentry jpql_fromentry) {
        this.jpql_fromentrys.add(jpql_fromentry);
    }
    public jpql_UpdateStatement getJpql_updatestatement() {
        return jpql_updatestatement;
    }

    public void setJpql_updatestatement(jpql_UpdateStatement jpql_updatestatement) {
        this.jpql_updatestatement = jpql_updatestatement;
    }

}
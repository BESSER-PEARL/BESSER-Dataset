





import java.util.List;
import java.util.ArrayList;

public class jPQL_UpdateClause  {






    private jPQL_UpdateStatement jpql_updatestatement;




    private List<jPQL_FromEntry> jpql_fromentrys;


    public jPQL_UpdateClause(
    ) {
        this.jpql_fromentrys = new ArrayList<>();
    }

    public jPQL_UpdateClause(
        ArrayList<jPQL_FromEntry> jpql_fromentrys    ) {
        this.jpql_fromentrys = jpql_fromentrys;
    }


    public jPQL_UpdateStatement getJpql_updatestatement() {
        return jpql_updatestatement;
    }

    public void setJpql_updatestatement(jPQL_UpdateStatement jpql_updatestatement) {
        this.jpql_updatestatement = jpql_updatestatement;
    }
    public List<jPQL_FromEntry> getJpql_fromentrys() {
        return jpql_fromentrys;
    }

    public void addJpql_fromentry(Jpql_fromentry jpql_fromentry) {
        this.jpql_fromentrys.add(jpql_fromentry);
    }

}
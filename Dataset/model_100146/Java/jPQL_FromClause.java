





import java.util.List;
import java.util.ArrayList;

public class jPQL_FromClause  {






    private jPQL_SelectStatement jpql_selectstatement;




    private List<jPQL_FromEntry> jpql_fromentrys;


    public jPQL_FromClause(
    ) {
        this.jpql_fromentrys = new ArrayList<>();
    }

    public jPQL_FromClause(
        ArrayList<jPQL_FromEntry> jpql_fromentrys    ) {
        this.jpql_fromentrys = jpql_fromentrys;
    }


    public jPQL_SelectStatement getJpql_selectstatement() {
        return jpql_selectstatement;
    }

    public void setJpql_selectstatement(jPQL_SelectStatement jpql_selectstatement) {
        this.jpql_selectstatement = jpql_selectstatement;
    }
    public List<jPQL_FromEntry> getJpql_fromentrys() {
        return jpql_fromentrys;
    }

    public void addJpql_fromentry(Jpql_fromentry jpql_fromentry) {
        this.jpql_fromentrys.add(jpql_fromentry);
    }

}
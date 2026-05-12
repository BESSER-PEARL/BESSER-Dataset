





import java.util.List;
import java.util.ArrayList;

public class jpql_QueryModule  {






    private List<jpql_NamedQuery> jpql_namedquerys;




    private jpql_JPQLQuery jpql_jpqlquery;


    public jpql_QueryModule(
    ) {
        this.jpql_namedquerys = new ArrayList<>();
    }

    public jpql_QueryModule(
        ArrayList<jpql_NamedQuery> jpql_namedquerys    ) {
        this.jpql_namedquerys = jpql_namedquerys;
    }


    public List<jpql_NamedQuery> getJpql_namedquerys() {
        return jpql_namedquerys;
    }

    public void addJpql_namedquery(Jpql_namedquery jpql_namedquery) {
        this.jpql_namedquerys.add(jpql_namedquery);
    }
    public jpql_JPQLQuery getJpql_jpqlquery() {
        return jpql_jpqlquery;
    }

    public void setJpql_jpqlquery(jpql_JPQLQuery jpql_jpqlquery) {
        this.jpql_jpqlquery = jpql_jpqlquery;
    }

}






import java.util.List;
import java.util.ArrayList;

public class jpql_NamedQuery  {

    private String name;





    private jpql_JPQLQuery jpql_jpqlquery;


    public jpql_NamedQuery(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public jpql_JPQLQuery getJpql_jpqlquery() {
        return jpql_jpqlquery;
    }

    public void setJpql_jpqlquery(jpql_JPQLQuery jpql_jpqlquery) {
        this.jpql_jpqlquery = jpql_jpqlquery;
    }

}
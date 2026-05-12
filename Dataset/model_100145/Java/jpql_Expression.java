





import java.util.List;
import java.util.ArrayList;

public class jpql_Expression  {






    private jpql_WhereClause jpql_whereclause;




    private jpql_HavingClause jpql_havingclause;


    public jpql_Expression(
    ) {
    }



    public jpql_WhereClause getJpql_whereclause() {
        return jpql_whereclause;
    }

    public void setJpql_whereclause(jpql_WhereClause jpql_whereclause) {
        this.jpql_whereclause = jpql_whereclause;
    }
    public jpql_HavingClause getJpql_havingclause() {
        return jpql_havingclause;
    }

    public void setJpql_havingclause(jpql_HavingClause jpql_havingclause) {
        this.jpql_havingclause = jpql_havingclause;
    }

}
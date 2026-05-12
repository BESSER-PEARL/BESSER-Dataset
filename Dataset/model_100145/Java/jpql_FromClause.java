





import java.util.List;
import java.util.ArrayList;

public class jpql_FromClause  {






    private jpql_DeleteClause jpql_deleteclause;




    private jpql_SelectFromClause jpql_selectfromclause;


    public jpql_FromClause(
    ) {
    }



    public jpql_DeleteClause getJpql_deleteclause() {
        return jpql_deleteclause;
    }

    public void setJpql_deleteclause(jpql_DeleteClause jpql_deleteclause) {
        this.jpql_deleteclause = jpql_deleteclause;
    }
    public jpql_SelectFromClause getJpql_selectfromclause() {
        return jpql_selectfromclause;
    }

    public void setJpql_selectfromclause(jpql_SelectFromClause jpql_selectfromclause) {
        this.jpql_selectfromclause = jpql_selectfromclause;
    }

}
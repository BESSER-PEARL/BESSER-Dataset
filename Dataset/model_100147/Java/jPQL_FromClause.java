





import java.util.List;
import java.util.ArrayList;

public class jPQL_FromClause  {






    private jPQL_SelectFromClause jpql_selectfromclause;




    private jPQL_DeleteClause jpql_deleteclause;


    public jPQL_FromClause(
    ) {
    }



    public jPQL_SelectFromClause getJpql_selectfromclause() {
        return jpql_selectfromclause;
    }

    public void setJpql_selectfromclause(jPQL_SelectFromClause jpql_selectfromclause) {
        this.jpql_selectfromclause = jpql_selectfromclause;
    }
    public jPQL_DeleteClause getJpql_deleteclause() {
        return jpql_deleteclause;
    }

    public void setJpql_deleteclause(jPQL_DeleteClause jpql_deleteclause) {
        this.jpql_deleteclause = jpql_deleteclause;
    }

}
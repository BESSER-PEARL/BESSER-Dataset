





import java.util.List;
import java.util.ArrayList;

public class jPQL_DeleteClause  {






    private jPQL_DeleteStatement jpql_deletestatement;




    private jPQL_FromClause jpql_fromclause;


    public jPQL_DeleteClause(
    ) {
    }



    public jPQL_DeleteStatement getJpql_deletestatement() {
        return jpql_deletestatement;
    }

    public void setJpql_deletestatement(jPQL_DeleteStatement jpql_deletestatement) {
        this.jpql_deletestatement = jpql_deletestatement;
    }
    public jPQL_FromClause getJpql_fromclause() {
        return jpql_fromclause;
    }

    public void setJpql_fromclause(jPQL_FromClause jpql_fromclause) {
        this.jpql_fromclause = jpql_fromclause;
    }

}
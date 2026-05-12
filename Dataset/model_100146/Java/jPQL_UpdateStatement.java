





import java.util.List;
import java.util.ArrayList;

public class jPQL_UpdateStatement extends JPQLQuery {






    private jPQL_SetClause jpql_setclause;


    public jPQL_UpdateStatement(
    ) {
        super(
        );
    }



    public jPQL_SetClause getJpql_setclause() {
        return jpql_setclause;
    }

    public void setJpql_setclause(jPQL_SetClause jpql_setclause) {
        this.jpql_setclause = jpql_setclause;
    }

}






import java.util.List;
import java.util.ArrayList;

public class mql_Expression  {






    private mql_HavingClause mql_havingclause;




    private mql_WhereClause mql_whereclause;


    public mql_Expression(
    ) {
    }



    public mql_HavingClause getMql_havingclause() {
        return mql_havingclause;
    }

    public void setMql_havingclause(mql_HavingClause mql_havingclause) {
        this.mql_havingclause = mql_havingclause;
    }
    public mql_WhereClause getMql_whereclause() {
        return mql_whereclause;
    }

    public void setMql_whereclause(mql_WhereClause mql_whereclause) {
        this.mql_whereclause = mql_whereclause;
    }

}
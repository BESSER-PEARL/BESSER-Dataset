





import java.util.List;
import java.util.ArrayList;

public class jPQL_SelectClause  {

    private boolean isDistinct;





    private jPQL_SelectFromClause jpql_selectfromclause;


    public jPQL_SelectClause(
        boolean isDistinct    ) {
        this.isDistinct = isDistinct;
    }


    public boolean getIsdistinct() {
        return isDistinct;
    }

    public void setIsdistinct(boolean isDistinct) {
        this.isDistinct = isDistinct;
    }

    public jPQL_SelectFromClause getJpql_selectfromclause() {
        return jpql_selectfromclause;
    }

    public void setJpql_selectfromclause(jPQL_SelectFromClause jpql_selectfromclause) {
        this.jpql_selectfromclause = jpql_selectfromclause;
    }

}
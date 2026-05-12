





import java.util.List;
import java.util.ArrayList;

public class jpql_SelectClause  {

    private boolean isDistinct;





    private jpql_SelectFromClause jpql_selectfromclause;


    public jpql_SelectClause(
        boolean isDistinct    ) {
        this.isDistinct = isDistinct;
    }


    public boolean getIsdistinct() {
        return isDistinct;
    }

    public void setIsdistinct(boolean isDistinct) {
        this.isDistinct = isDistinct;
    }

    public jpql_SelectFromClause getJpql_selectfromclause() {
        return jpql_selectfromclause;
    }

    public void setJpql_selectfromclause(jpql_SelectFromClause jpql_selectfromclause) {
        this.jpql_selectfromclause = jpql_selectfromclause;
    }

}
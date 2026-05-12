





import java.util.List;
import java.util.ArrayList;

public class mql_SelectClause  {

    private boolean isDistinct;





    private mql_SelectFromClause mql_selectfromclause;




    private List<mql_SelectExpression> mql_selectexpressions;


    public mql_SelectClause(
        boolean isDistinct    ) {
        this.isDistinct = isDistinct;
        this.mql_selectexpressions = new ArrayList<>();
    }

    public mql_SelectClause(
        boolean isDistinct        ArrayList<mql_SelectExpression> mql_selectexpressions    ) {
        this.isDistinct = isDistinct;
        this.mql_selectexpressions = mql_selectexpressions;
    }

    public boolean getIsdistinct() {
        return isDistinct;
    }

    public void setIsdistinct(boolean isDistinct) {
        this.isDistinct = isDistinct;
    }

    public mql_SelectFromClause getMql_selectfromclause() {
        return mql_selectfromclause;
    }

    public void setMql_selectfromclause(mql_SelectFromClause mql_selectfromclause) {
        this.mql_selectfromclause = mql_selectfromclause;
    }
    public List<mql_SelectExpression> getMql_selectexpressions() {
        return mql_selectexpressions;
    }

    public void addMql_selectexpression(Mql_selectexpression mql_selectexpression) {
        this.mql_selectexpressions.add(mql_selectexpression);
    }

}
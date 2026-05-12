





import java.util.List;
import java.util.ArrayList;

public class jPQL_SelectClause  {

    private boolean isDistinct;





    private jPQL_SelectStatement jpql_selectstatement;


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

    public jPQL_SelectStatement getJpql_selectstatement() {
        return jpql_selectstatement;
    }

    public void setJpql_selectstatement(jPQL_SelectStatement jpql_selectstatement) {
        this.jpql_selectstatement = jpql_selectstatement;
    }

}
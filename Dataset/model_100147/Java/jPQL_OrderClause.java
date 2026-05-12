





import java.util.List;
import java.util.ArrayList;

public class jPQL_OrderClause  {

    private boolean isDesc;
    private boolean isAsc;





    private jPQL_SelectStatement jpql_selectstatement;


    public jPQL_OrderClause(
        boolean isDesc,        boolean isAsc    ) {
        this.isDesc = isDesc;
        this.isAsc = isAsc;
    }


    public boolean getIsdesc() {
        return isDesc;
    }

    public void setIsdesc(boolean isDesc) {
        this.isDesc = isDesc;
    }
    public boolean getIsasc() {
        return isAsc;
    }

    public void setIsasc(boolean isAsc) {
        this.isAsc = isAsc;
    }

    public jPQL_SelectStatement getJpql_selectstatement() {
        return jpql_selectstatement;
    }

    public void setJpql_selectstatement(jPQL_SelectStatement jpql_selectstatement) {
        this.jpql_selectstatement = jpql_selectstatement;
    }

}
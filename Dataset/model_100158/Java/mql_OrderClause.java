





import java.util.List;
import java.util.ArrayList;

public class mql_OrderClause  {

    private boolean isAsc;
    private boolean isDesc;





    private mql_SelectStatement mql_selectstatement;




    private List<mql_OrderItem> mql_orderitems;


    public mql_OrderClause(
        boolean isAsc,        boolean isDesc    ) {
        this.isAsc = isAsc;
        this.isDesc = isDesc;
        this.mql_orderitems = new ArrayList<>();
    }

    public mql_OrderClause(
        boolean isAsc,        boolean isDesc        ArrayList<mql_OrderItem> mql_orderitems    ) {
        this.isAsc = isAsc;
        this.isDesc = isDesc;
        this.mql_orderitems = mql_orderitems;
    }

    public boolean getIsasc() {
        return isAsc;
    }

    public void setIsasc(boolean isAsc) {
        this.isAsc = isAsc;
    }
    public boolean getIsdesc() {
        return isDesc;
    }

    public void setIsdesc(boolean isDesc) {
        this.isDesc = isDesc;
    }

    public mql_SelectStatement getMql_selectstatement() {
        return mql_selectstatement;
    }

    public void setMql_selectstatement(mql_SelectStatement mql_selectstatement) {
        this.mql_selectstatement = mql_selectstatement;
    }
    public List<mql_OrderItem> getMql_orderitems() {
        return mql_orderitems;
    }

    public void addMql_orderitem(Mql_orderitem mql_orderitem) {
        this.mql_orderitems.add(mql_orderitem);
    }

}
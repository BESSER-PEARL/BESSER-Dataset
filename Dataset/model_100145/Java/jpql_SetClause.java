





import java.util.List;
import java.util.ArrayList;

public class jpql_SetClause  {






    private List<jpql_UpdateItem> jpql_updateitems;




    private jpql_UpdateStatement jpql_updatestatement;


    public jpql_SetClause(
    ) {
        this.jpql_updateitems = new ArrayList<>();
    }

    public jpql_SetClause(
        ArrayList<jpql_UpdateItem> jpql_updateitems    ) {
        this.jpql_updateitems = jpql_updateitems;
    }


    public List<jpql_UpdateItem> getJpql_updateitems() {
        return jpql_updateitems;
    }

    public void addJpql_updateitem(Jpql_updateitem jpql_updateitem) {
        this.jpql_updateitems.add(jpql_updateitem);
    }
    public jpql_UpdateStatement getJpql_updatestatement() {
        return jpql_updatestatement;
    }

    public void setJpql_updatestatement(jpql_UpdateStatement jpql_updatestatement) {
        this.jpql_updatestatement = jpql_updatestatement;
    }

}
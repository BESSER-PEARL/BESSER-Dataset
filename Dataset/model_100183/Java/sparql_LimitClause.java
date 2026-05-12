





import java.util.List;
import java.util.ArrayList;

public class sparql_LimitClause  {

    private int limit;





    private sparql_SelectionQuery sparql_selectionquery;


    public sparql_LimitClause(
        int limit    ) {
        this.limit = limit;
    }


    public int getLimit() {
        return limit;
    }

    public void setLimit(int limit) {
        this.limit = limit;
    }

    public sparql_SelectionQuery getSparql_selectionquery() {
        return sparql_selectionquery;
    }

    public void setSparql_selectionquery(sparql_SelectionQuery sparql_selectionquery) {
        this.sparql_selectionquery = sparql_selectionquery;
    }

}






import java.util.List;
import java.util.ArrayList;

public class r1_SortClause extends Element {






    private List<r1_SortByItem> r1_sortbyitems;




    private r1_Query r1_query;


    public r1_SortClause(
    ) {
        super(
        );
        this.r1_sortbyitems = new ArrayList<>();
    }

    public r1_SortClause(
        ArrayList<r1_SortByItem> r1_sortbyitems    ) {
        this.r1_sortbyitems = r1_sortbyitems;
    }


    public List<r1_SortByItem> getR1_sortbyitems() {
        return r1_sortbyitems;
    }

    public void addR1_sortbyitem(R1_sortbyitem r1_sortbyitem) {
        this.r1_sortbyitems.add(r1_sortbyitem);
    }
    public r1_Query getR1_query() {
        return r1_query;
    }

    public void setR1_query(r1_Query r1_query) {
        this.r1_query = r1_query;
    }

}
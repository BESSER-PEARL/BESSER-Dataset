





import java.util.List;
import java.util.ArrayList;

public class r1_SortByItem extends Element {

    private String direction;





    private r1_SortClause r1_sortclause;




    private r1_Sort r1_sort;


    public r1_SortByItem(
        String direction    ) {
        super(
        );
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public r1_SortClause getR1_sortclause() {
        return r1_sortclause;
    }

    public void setR1_sortclause(r1_SortClause r1_sortclause) {
        this.r1_sortclause = r1_sortclause;
    }
    public r1_Sort getR1_sort() {
        return r1_sort;
    }

    public void setR1_sort(r1_Sort r1_sort) {
        this.r1_sort = r1_sort;
    }

}
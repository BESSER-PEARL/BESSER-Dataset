





import java.util.List;
import java.util.ArrayList;

public class rdb_constraints_IndexedColumn extends NamedElement {

    private boolean ascending;



    public rdb_constraints_IndexedColumn(
        boolean ascending    ) {
        super(
        );
        this.ascending = ascending;
    }


    public boolean getAscending() {
        return ascending;
    }

    public void setAscending(boolean ascending) {
        this.ascending = ascending;
    }


}
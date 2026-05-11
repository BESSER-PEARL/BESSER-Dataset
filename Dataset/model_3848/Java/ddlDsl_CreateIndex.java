





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_CreateIndex extends Create {

    private boolean unique;
    private String sortOrders;





    private List<ddlDsl_Column> ddldsl_columns;


    public ddlDsl_CreateIndex(
        boolean unique,        String sortOrders    ) {
        super(
        );
        this.unique = unique;
        this.sortOrders = sortOrders;
        this.ddldsl_columns = new ArrayList<>();
    }

    public ddlDsl_CreateIndex(
        boolean unique,        String sortOrders        ArrayList<ddlDsl_Column> ddldsl_columns    ) {
        this.unique = unique;
        this.sortOrders = sortOrders;
        this.ddldsl_columns = ddldsl_columns;
    }

    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public String getSortorders() {
        return sortOrders;
    }

    public void setSortorders(String sortOrders) {
        this.sortOrders = sortOrders;
    }

    public List<ddlDsl_Column> getDdldsl_columns() {
        return ddldsl_columns;
    }

    public void addDdldsl_column(Ddldsl_column ddldsl_column) {
        this.ddldsl_columns.add(ddldsl_column);
    }

}
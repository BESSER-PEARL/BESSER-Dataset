





import java.util.List;
import java.util.ArrayList;

public class ddlDsl_CreateIndex extends Create {

    private String sortOrders;
    private boolean unique;





    private ddlDsl_CreateTable ddldsl_createtable;




    private List<ddlDsl_Column> ddldsl_columns;


    public ddlDsl_CreateIndex(
        String sortOrders,        boolean unique    ) {
        super(
        );
        this.sortOrders = sortOrders;
        this.unique = unique;
        this.ddldsl_columns = new ArrayList<>();
    }

    public ddlDsl_CreateIndex(
        String sortOrders,        boolean unique        ArrayList<ddlDsl_Column> ddldsl_columns    ) {
        this.sortOrders = sortOrders;
        this.unique = unique;
        this.ddldsl_columns = ddldsl_columns;
    }

    public String getSortorders() {
        return sortOrders;
    }

    public void setSortorders(String sortOrders) {
        this.sortOrders = sortOrders;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }

    public ddlDsl_CreateTable getDdldsl_createtable() {
        return ddldsl_createtable;
    }

    public void setDdldsl_createtable(ddlDsl_CreateTable ddldsl_createtable) {
        this.ddldsl_createtable = ddldsl_createtable;
    }
    public List<ddlDsl_Column> getDdldsl_columns() {
        return ddldsl_columns;
    }

    public void addDdldsl_column(Ddldsl_column ddldsl_column) {
        this.ddldsl_columns.add(ddldsl_column);
    }

}
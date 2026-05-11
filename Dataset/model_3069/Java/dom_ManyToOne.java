





import java.util.List;
import java.util.ArrayList;

public class dom_ManyToOne extends DaoFeature {

    private boolean derived;
    private String columnName;





    private List<dom_Column> dom_columns;




    private dom_Dao dom_dao;




    private dom_Type dom_type;


    public dom_ManyToOne(
        boolean derived,        String columnName    ) {
        super(
        );
        this.derived = derived;
        this.columnName = columnName;
        this.dom_columns = new ArrayList<>();
    }

    public dom_ManyToOne(
        boolean derived,        String columnName        ArrayList<dom_Column> dom_columns    ) {
        this.derived = derived;
        this.columnName = columnName;
        this.dom_columns = dom_columns;
    }

    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }

    public List<dom_Column> getDom_columns() {
        return dom_columns;
    }

    public void addDom_column(Dom_column dom_column) {
        this.dom_columns.add(dom_column);
    }
    public dom_Dao getDom_dao() {
        return dom_dao;
    }

    public void setDom_dao(dom_Dao dom_dao) {
        this.dom_dao = dom_dao;
    }
    public dom_Type getDom_type() {
        return dom_type;
    }

    public void setDom_type(dom_Type dom_type) {
        this.dom_type = dom_type;
    }

}
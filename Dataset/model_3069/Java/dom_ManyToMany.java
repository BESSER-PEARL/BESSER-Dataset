





import java.util.List;
import java.util.ArrayList;

public class dom_ManyToMany extends DaoFeature {

    private boolean inverse;
    private String tableName;
    private String columnName;





    private dom_Dao dom_dao;


    public dom_ManyToMany(
        boolean inverse,        String tableName,        String columnName    ) {
        super(
        );
        this.inverse = inverse;
        this.tableName = tableName;
        this.columnName = columnName;
    }


    public boolean getInverse() {
        return inverse;
    }

    public void setInverse(boolean inverse) {
        this.inverse = inverse;
    }
    public String getTablename() {
        return tableName;
    }

    public void setTablename(String tableName) {
        this.tableName = tableName;
    }
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }

    public dom_Dao getDom_dao() {
        return dom_dao;
    }

    public void setDom_dao(dom_Dao dom_dao) {
        this.dom_dao = dom_dao;
    }

}
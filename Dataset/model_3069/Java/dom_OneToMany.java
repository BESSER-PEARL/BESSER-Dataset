





import java.util.List;
import java.util.ArrayList;

public class dom_OneToMany extends DaoFeature {

    private String columnName;





    private dom_Dao dom_dao;


    public dom_OneToMany(
        String columnName    ) {
        super(
        );
        this.columnName = columnName;
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
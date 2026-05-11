





import java.util.List;
import java.util.ArrayList;

public class dom_Column extends DaoFeature {

    private String columnName;





    private dom_DataTypeAndTypeParameter dom_datatypeandtypeparameter;




    private dom_Type dom_type;




    private dom_Dao dom_dao;




    private dom_Dao dom_dao;




    private dom_Dao dom_dao;




    private dom_OneToMany dom_onetomany;




    private List<dom_Column> dom_columns;




    private dom_Dao dom_dao;


    public dom_Column(
        String columnName    ) {
        super(
        );
        this.columnName = columnName;
        this.dom_columns = new ArrayList<>();
    }

    public dom_Column(
        String columnName        ArrayList<dom_Column> dom_columns    ) {
        this.columnName = columnName;
        this.dom_columns = dom_columns;
    }

    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }

    public dom_DataTypeAndTypeParameter getDom_datatypeandtypeparameter() {
        return dom_datatypeandtypeparameter;
    }

    public void setDom_datatypeandtypeparameter(dom_DataTypeAndTypeParameter dom_datatypeandtypeparameter) {
        this.dom_datatypeandtypeparameter = dom_datatypeandtypeparameter;
    }
    public dom_Type getDom_type() {
        return dom_type;
    }

    public void setDom_type(dom_Type dom_type) {
        this.dom_type = dom_type;
    }
    public dom_Dao getDom_dao() {
        return dom_dao;
    }

    public void setDom_dao(dom_Dao dom_dao) {
        this.dom_dao = dom_dao;
    }
    public dom_Dao getDom_dao() {
        return dom_dao;
    }

    public void setDom_dao(dom_Dao dom_dao) {
        this.dom_dao = dom_dao;
    }
    public dom_Dao getDom_dao() {
        return dom_dao;
    }

    public void setDom_dao(dom_Dao dom_dao) {
        this.dom_dao = dom_dao;
    }
    public dom_OneToMany getDom_onetomany() {
        return dom_onetomany;
    }

    public void setDom_onetomany(dom_OneToMany dom_onetomany) {
        this.dom_onetomany = dom_onetomany;
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

}
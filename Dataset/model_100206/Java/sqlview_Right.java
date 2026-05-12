





import java.util.List;
import java.util.ArrayList;

public class sqlview_Right  {

    private String value;





    private sqlview_Attribute sqlview_attribute;




    private sqlview_Comparison sqlview_comparison;




    private List<sqlview_Class> sqlview_classs;




    private List<sqlview_MetamodelName> sqlview_metamodelnames;


    public sqlview_Right(
        String value    ) {
        this.value = value;
        this.sqlview_classs = new ArrayList<>();
        this.sqlview_metamodelnames = new ArrayList<>();
    }

    public sqlview_Right(
        String value        ArrayList<sqlview_Class> sqlview_classs,        ArrayList<sqlview_MetamodelName> sqlview_metamodelnames    ) {
        this.value = value;
        this.sqlview_classs = sqlview_classs;
        this.sqlview_metamodelnames = sqlview_metamodelnames;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public sqlview_Attribute getSqlview_attribute() {
        return sqlview_attribute;
    }

    public void setSqlview_attribute(sqlview_Attribute sqlview_attribute) {
        this.sqlview_attribute = sqlview_attribute;
    }
    public sqlview_Comparison getSqlview_comparison() {
        return sqlview_comparison;
    }

    public void setSqlview_comparison(sqlview_Comparison sqlview_comparison) {
        this.sqlview_comparison = sqlview_comparison;
    }
    public List<sqlview_Class> getSqlview_classs() {
        return sqlview_classs;
    }

    public void addSqlview_class(Sqlview_class sqlview_class) {
        this.sqlview_classs.add(sqlview_class);
    }
    public List<sqlview_MetamodelName> getSqlview_metamodelnames() {
        return sqlview_metamodelnames;
    }

    public void addSqlview_metamodelname(Sqlview_metamodelname sqlview_metamodelname) {
        this.sqlview_metamodelnames.add(sqlview_metamodelname);
    }

}
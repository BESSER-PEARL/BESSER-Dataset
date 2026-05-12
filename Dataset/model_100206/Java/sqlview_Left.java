





import java.util.List;
import java.util.ArrayList;

public class sqlview_Left  {






    private List<sqlview_MetamodelName> sqlview_metamodelnames;




    private List<sqlview_Class> sqlview_classs;




    private sqlview_Comparison sqlview_comparison;




    private sqlview_Attribute sqlview_attribute;


    public sqlview_Left(
    ) {
        this.sqlview_metamodelnames = new ArrayList<>();
        this.sqlview_classs = new ArrayList<>();
    }

    public sqlview_Left(
        ArrayList<sqlview_MetamodelName> sqlview_metamodelnames,        ArrayList<sqlview_Class> sqlview_classs    ) {
        this.sqlview_metamodelnames = sqlview_metamodelnames;
        this.sqlview_classs = sqlview_classs;
    }


    public List<sqlview_MetamodelName> getSqlview_metamodelnames() {
        return sqlview_metamodelnames;
    }

    public void addSqlview_metamodelname(Sqlview_metamodelname sqlview_metamodelname) {
        this.sqlview_metamodelnames.add(sqlview_metamodelname);
    }
    public List<sqlview_Class> getSqlview_classs() {
        return sqlview_classs;
    }

    public void addSqlview_class(Sqlview_class sqlview_class) {
        this.sqlview_classs.add(sqlview_class);
    }
    public sqlview_Comparison getSqlview_comparison() {
        return sqlview_comparison;
    }

    public void setSqlview_comparison(sqlview_Comparison sqlview_comparison) {
        this.sqlview_comparison = sqlview_comparison;
    }
    public sqlview_Attribute getSqlview_attribute() {
        return sqlview_attribute;
    }

    public void setSqlview_attribute(sqlview_Attribute sqlview_attribute) {
        this.sqlview_attribute = sqlview_attribute;
    }

}
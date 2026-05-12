





import java.util.List;
import java.util.ArrayList;

public class sqlview_JoinRight  {






    private List<sqlview_MetamodelName> sqlview_metamodelnames;


    public sqlview_JoinRight(
    ) {
        this.sqlview_metamodelnames = new ArrayList<>();
    }

    public sqlview_JoinRight(
        ArrayList<sqlview_MetamodelName> sqlview_metamodelnames    ) {
        this.sqlview_metamodelnames = sqlview_metamodelnames;
    }


    public List<sqlview_MetamodelName> getSqlview_metamodelnames() {
        return sqlview_metamodelnames;
    }

    public void addSqlview_metamodelname(Sqlview_metamodelname sqlview_metamodelname) {
        this.sqlview_metamodelnames.add(sqlview_metamodelname);
    }

}
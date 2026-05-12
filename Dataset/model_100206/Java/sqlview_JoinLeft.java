





import java.util.List;
import java.util.ArrayList;

public class sqlview_JoinLeft  {






    private List<sqlview_MetamodelName> sqlview_metamodelnames;


    public sqlview_JoinLeft(
    ) {
        this.sqlview_metamodelnames = new ArrayList<>();
    }

    public sqlview_JoinLeft(
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
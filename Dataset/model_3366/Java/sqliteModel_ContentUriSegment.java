





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_ContentUriSegment  {

    private String name;





    private sqliteModel_ContentUri sqlitemodel_contenturi;


    public sqliteModel_ContentUriSegment(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sqliteModel_ContentUri getSqlitemodel_contenturi() {
        return sqlitemodel_contenturi;
    }

    public void setSqlitemodel_contenturi(sqliteModel_ContentUri sqlitemodel_contenturi) {
        this.sqlitemodel_contenturi = sqlitemodel_contenturi;
    }

}
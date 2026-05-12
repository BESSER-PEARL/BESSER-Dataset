





import java.util.List;
import java.util.ArrayList;

public class dbmap_InputTable extends AbstaceDBInOutTable {

    private String joinType;
    private String alias;





    private dbmap_DBMapData dbmap_dbmapdata;


    public dbmap_InputTable(
        String joinType,        String alias    ) {
        super(
        );
        this.joinType = joinType;
        this.alias = alias;
    }


    public String getJointype() {
        return joinType;
    }

    public void setJointype(String joinType) {
        this.joinType = joinType;
    }
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }

    public dbmap_DBMapData getDbmap_dbmapdata() {
        return dbmap_dbmapdata;
    }

    public void setDbmap_dbmapdata(dbmap_DBMapData dbmap_dbmapdata) {
        this.dbmap_dbmapdata = dbmap_dbmapdata;
    }

}